import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver

# Function to detect the object using Roboflow

def detect_object(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(40)  # Wait for Roboflow detection
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    detected_object = None
    confidence = 0.0
    predictions = json.loads(soup.find("pre").text)
    if predictions['predictions'][0]['confidence'] >= 0.5:
        detected_object = predictions['predictions'][0]['class']
        confidence = predictions['predictions'][0]['confidence']
    driver.quit()
    return detected_object, confidence

# Function to scrape prices from Flipkart
def scrape_flipkart_price(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10)  # Allow time for page to load
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    price_element = soup.find("div", {"class": "_30jeq3"})
    if price_element:
        return price_element.text.strip()
    driver.quit()
    return None

# Function to scrape prices from Amazon
def scrape_amazon_price(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10)  # Allow time for page to load
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    price_element = soup.find("span", {"class": "a-price-whole"})
    if price_element:
        return price_element.text.strip()
    driver.quit()
    return None

# Function to scrape prices from Reliance Digital
def scrape_reliance_digital_price(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10)  # Allow time for page to load
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    script_tags = soup.find_all('script', type='application/ld+json')
    for script_tag in script_tags:
        script_content = script_tag.string
        if script_content:
            data = json.loads(script_content)
            if 'offers' in data and 'price' in data['offers']:
                return data['offers']['price']
    driver.quit()
    return None

# Function for Apple Watch price comparison
def main_apple_watch():
    # URLs for scraping prices
    flipkart_url = "https://www.flipkart.com/apple-watch-series-8-gps/p/itm327ac7d359019"
    amazon_url = "https://www.amazon.in/Apple-Starlight-Aluminium-Fitness-Resistant/dp/B0BDKFJVTL/ref=sr_1_4?crid=H4V7XV4O0G8Y&dib=eyJ2IjoiMSJ9.b9k1RMSl1P7INNm9UQq0fiZz0no9pv_iHOOmx-bTEM-IIwo1SNp-9PXFcPg-bs3mmNj2fPLTe6_aQUvmpqoN11ft8MtmPKEgxqq2TGBDL1j5s89TtsBL2SerR5xLdYSY9ouDgYs2A0flIfpta19nOUkkFQrVH2Vlt7UlI2RTEpKbL92q6Dfhd4yBfB7fIRGKaTazLehlgQsKAZx4Wqy5ObEKElDmU0bz1UNAn08oEMo.YvlCeXapWtDoVrEWrT3pdy6iu_QtWDOumQiLe-IaOwo&dib_tag=se&keywords=apple+watch+series+8&qid=1711712093&sprefix=apple+watch+series+8%2Caps%2C293&sr=8-4"
    reliance_digital_url = "https://www.reliancedigital.in/apple-watch-series-8-gps-45mm-starlight-aluminium-case-with-starlight-sport-band-water-resistant-50-metres-dust-resistant-ip6x-fast-charge-3rd-gen-optical-heart-sensor-emergency-sos-crash-detection-fall-detection/p/493177909"

    # Scrape prices
    flipkart_price = scrape_flipkart_price(flipkart_url)
    amazon_price = scrape_amazon_price(amazon_url)
    reliance_digital_price = scrape_reliance_digital_price(reliance_digital_url)

    # Print prices
    print("Apple Watch Prices:")
    print("Flipkart:", flipkart_price)
    print("Amazon:", amazon_price)
    print("Reliance Digital:", reliance_digital_price)

    # Find the minimum price
    prices = [(flipkart_price, "Flipkart"), (amazon_price, "Amazon"), (reliance_digital_price, "Reliance Digital")]
    prices = [(price.replace("₹", "").replace(",", ""), website) for price, website in prices if price is not None]
    if prices:
        min_price, min_website = min(prices, key=lambda x: float(x[0]))
        print("Minimum price found at", min_website + ":", min_price)
        time.sleep(7)
        # Redirect to the website with the lowest price
        if min_website == "Flipkart":
            driver = webdriver.Chrome()
            driver.get(flipkart_url)
        elif min_website == "Amazon":
            driver = webdriver.Chrome()
            driver.get(amazon_url)
        elif min_website == "Reliance Digital":
            driver = webdriver.Chrome()
            driver.get(reliance_digital_url)

        time.sleep(40)  # Keep the window open for 30 seconds
        # driver.quit()  # Uncomment this line if you want to close the browser window automatically
    else:
        print("Failed to find the minimum price for Apple Watch.")

# Function for iPhone price comparison
def main_iphone():
    # URLs for scraping prices
    flipkart_url = "https://www.flipkart.com/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4?otracker=undefined_footer"
    amazon_url = "https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX2F5QT"
    reliance_digital_url = "https://www.reliancedigital.in/apple-iphone-15-128gb-blue/p/493839312"

    # Scrape prices
    flipkart_price = scrape_flipkart_price(flipkart_url)
    amazon_price = scrape_amazon_price(amazon_url)
    reliance_digital_price = scrape_reliance_digital_price(reliance_digital_url)

    # Print prices
    print("\n\niPhone Prices:")
    print("Flipkart:", flipkart_price)
    print("Amazon:", amazon_price)
    print("Reliance Digital:", reliance_digital_price)

    # Find the minimum price
    prices = [(flipkart_price, "Flipkart"), (amazon_price, "Amazon"), (reliance_digital_price, "Reliance Digital")]
    prices = [(price.replace("₹", "").replace(",", ""), website) for price, website in prices if price is not None]
    if prices:
        min_price, min_website = min(prices, key=lambda x: float(x[0]))
        print("Minimum price found at", min_website + ":", min_price)
        time.sleep(7)
        # Redirect to the website with the lowest price
        if min_website == "Flipkart":
            driver = webdriver.Chrome()
            driver.get(flipkart_url)
        elif min_website == "Amazon":
            driver = webdriver.Chrome()
            driver.get(amazon_url)
        elif min_website == "Reliance Digital":
            driver = webdriver.Chrome()
            driver.get(reliance_digital_url)

        time.sleep(40)  # Keep the window open for 30 seconds
        # driver.quit()  # Uncomment this line if you want to close the browser window automatically
    else:
        print("Failed to find the minimum price for iPhone.")

# Function for PS5 price comparison
def main_ps5():
    # URLs for scraping prices
    flipkart_url = "https://www.flipkart.com/sony-playstation-5-digital-825-gb-astro-s-playroom/p/itm3c6e8c91e0941?pid=GMCFYTWSM9Q9SN3C&lid=LSTGMCFYTWSM9Q9SN3CKRLRPQ&marketplace=FLIPKART&q=ps5+console&store=4rr%2Fx1m%2Fogz&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&fm=organic&iid=51627e56-7a1e-4449-9ae8-63c83912edaf.GMCFYTWSM9Q9SN3C.SEARCH&ppt=pp&ppn=pp&ssid=gqwt601nkg0000001711991382283&qH=63cbe5d6e6345fd8"
    amazon_url = "https://www.amazon.in/Sony-PS5-Console-Modern-Warfare/dp/B0CMQPPMB1/ref=sr_1_1?crid=22GKGBGIOTURU&dib=eyJ2IjoiMSJ9.BC66k2xO-SAbYyl4T9reOvDpYSXbz99fesnzvA4y5WpWXFUXi-R9aHSDH7nEjatly-r38UFz1aee2CapSs9z9A1oIfHs5OBXkGBh7OMdYqCACafkOLWhlcsZpDUDre-OI9A5KWJPpWI2onGpzFd972YVWdQekGqCaUJgf83HKhNhbeJu9RjrNx4VmFvb1vLmjTPNjGXmP4r64cOblIQEcfjJOrUfCsyvYCxlzfvGIjE.2U2Ww82hcE8WVJsKR8v_vpDFHCkGmKGQh0ezjx0syTU&dib_tag=se&keywords=ps5&qid=1711991412&sprefix=ps5%2Caps%2C244&sr=8-1"
    reliance_digital_url = "https://www.reliancedigital.in/sony-playstation-5-console-ps5-/p/491936180"

    # Scrape prices
    flipkart_price = scrape_flipkart_price(flipkart_url)
    amazon_price = scrape_amazon_price(amazon_url)
    reliance_digital_price = scrape_reliance_digital_price(reliance_digital_url)

    # Print prices
    print("\n\nPS5 Prices:")
    print("Flipkart:", flipkart_price)
    print("Amazon:", amazon_price)
    print("Reliance Digital:", reliance_digital_price)

    # Find the minimum price
    prices = [(flipkart_price, "Flipkart"), (amazon_price, "Amazon"), (reliance_digital_price, "Reliance Digital")]
    prices = [(price.replace("₹", "").replace(",", ""), website) for price, website in prices if price is not None]
    if prices:
        min_price, min_website = min(prices, key=lambda x: float(x[0]))
        print("Minimum price found at", min_website + ":", min_price)
        time.sleep(7)
        # Redirect to the website with the lowest price
        if min_website == "Flipkart":
            driver = webdriver.Chrome()
            driver.get(flipkart_url)
        elif min_website == "Amazon":
            driver = webdriver.Chrome()
            driver.get(amazon_url)
        elif min_website == "Reliance Digital":
            driver = webdriver.Chrome()
            driver.get(reliance_digital_url)

        time.sleep(40)  # Keep the window open for 30 seconds
        # driver.quit()  # Uncomment this line if you want to close the browser window automatically
    else:
        print("Failed to find the minimum price for PS5.")

# Main function to run all comparisons
def main():
    roboflow_url = "https://detect.roboflow.com/?model=apple-watch-detection&version=3&api_key=9Jbw3IaQ98XxRQ6eUzh9"
    detected_object, confidence = detect_object(roboflow_url)

    if detected_object == "iwatch" and confidence >= 0.5:
        main_apple_watch()
    elif detected_object == "iphone" and confidence >= 0.5:
        main_iphone()
    elif detected_object == "ps5" and confidence >= 0.5:
        main_ps5()
    else:
        print("Unknown object detected or detection failed.")

if __name__ == "__main__":
    main()
