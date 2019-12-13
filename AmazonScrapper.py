import json
from bs4 import BeautifulSoup
from selenium import webdriver

# Include Path of your Chrome driver
driver = webdriver.Chrome(r"path\to\your\chomedriver.exe")


def getSearchResults(keyword, pageCount=1):
    """ This function searches the Amazon.com based on the keywords Provided,
        It Extacts all data-asins(Unique Id of Products),
        You can Also Provide the Number of top pages """

    FinalData = []

    # Number of top pages from which you want to Extract Information
    for page in range(pageCount):
        # requesting amazon page using selenium
        driver.get(f"https://www.amazon.in/s?k={keyword}&page={page}")

        # driver.page_source saves the page source of requested page into variable
        content = driver.page_source

        # parsing page source content using beautifulsoup
        # here we are using "lxml" parser, we can also use "html.parser" instead
        soup = BeautifulSoup(content, "lxml")

        # finding all div tags in which "data-asin" attribute is Present
        # dataAsins list contains Product Ids for each propduct listed on page
        dataAsins = [div.get("data-asin")
                     for div in soup.findAll('div') if div.has_attr("data-asin")]

        pageData = getProductPage(dataAsins)

        # appending all Products details from particular page to FinalData
        for data in pageData:
            FinalData.append(data)

    with open('result.json', 'w')as f:
        json.dump(FinalData, f)
    driver.close()


def getProductPage(productIds):
    """This function iterates over each Product Page,
    Extracts Information from the product page and returns a dictionary
    You can add Extra fields to Extract by creating Your Own Function And modifying the final dictionary """

    PageData = []
    for productId in productIds:
        try:
            # By Substituting Product Id in This Url form Url for that particular product page
            ProductUrl = f"https://www.amazon.in/dp/{productId}/"

            driver.get(ProductUrl)

            # saving the Page source of product page in content variable
            content = driver.page_source

            # parsing page source using beautifulsoup
            soup = BeautifulSoup(content, "lxml")

            # finding Product Title or name
            ProductName = soup.find("span", id="productTitle").text.strip()

            # finding Product Price
            Price = FindProductPrice(soup)

            # Finding Product Features which is in div tag whose id is feature-bullets
            ProductFeatures = soup.find("div", id="feature-bullets")

            # if the tag is preset we go on and find Features
            if ProductFeatures:
                # Product Features List contains all features of the product
                ProductFeatures = [feature.span.text.strip()
                                   for feature in ProductFeatures.findAll("li") if len(ProductFeatures.findAll("li")) > 0]

            # finding the availibility of product
            # i.e Product is available in stock or is out of stock
            Avalibility = soup.find("div", id="availability")
            if Avalibility:
                Avalibility = Avalibility.span.text.strip()

            # Finding the customer reviews of the product out of five
            CustomerReviews = soup.find('div', id="averageCustomerReviews")

            # if Parent tag Contaning Customer review is present we go on and find reviews
            if CustomerReviews:
                # we get string like "4.5 out of 5 stars" but we need 4.5 so we need to split the string
                # after splitting the string we take out 0th position

                CustomerReviews = [span.get("title") for span in CustomerReviews.findAll(
                    'span')if span.has_attr("title")][0].strip().split(" ")[0]

            # final Output dictionary
            data = {
                "ProductUrl": ProductUrl,
                "ProductName": ProductName,
                "Price": Price,
                "ProductFeatures": ProductFeatures,
                "Availibility": Avalibility,
                "CustomerReviews": CustomerReviews
            }
            PageData.append(data)
        except Exception as e:
            print(e)
            pass
    return PageData


def FindProductPrice(soup):
    """This function Finds the Price Of the particular Product,
    Finding Price is bit tricky because tag for Product in Deal sale and in normal sale is different,
    PriceIds list contains Ids of tag in which Price is Present which can vary"""

    PriceIds = ["priceblock_ourprice", "priceblock_dealprice"]

    for Pid in PriceIds:

        # finding span tag in which Price is Present
        Price = soup.find("span", id=Pid)

        # If Price is Found return the amount after removing unwanted characters
        # Unwanted Character includes Currency symbols and some unicode chars
        if Price:
            return Price.text.strip().replace(
                "\xa0", " ").split(" ")[-1]

    return


if __name__ == "__main__":
    # your keyword on which your search is based
    keyword = "shoes"
    getSearchResults(keyword)
