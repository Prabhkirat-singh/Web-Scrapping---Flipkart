from bs4 import BeautifulSoup as bs
import requests


def fetchingInfo(product):
    url = f"https://www.flipkart.com/search?q={str(product)}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    response = requests.get(url)
    all_data = {
        "url": [],
        "products_Name": [],
        "products_Price": [],
    }
    soup = bs(response.content, "html.parser")
    soup.prettify()
    images = soup.find_all("img", class_="DByuf4")
    Names = soup.find_all("div", class_="KzDlHZ")
    Prices = soup.find_all("div", class_="Nx9bqj")
    for image in images:
        all_data["url"].append(image["src"])
    for name in Names:
        all_data["products_Name"].append(name.text)
    for price in Prices:
        all_data["products_Price"].append(price.text)
    return all_data
