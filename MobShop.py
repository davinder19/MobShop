from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

davinder = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
davinder.get("https://rahulshettyacademy.com/angularpractice/")
davinder.maximize_window()  # maximize method maximize your window
# click and open the shop  web page
davinder.implicitly_wait(5)
davinder.find_element_by_css_selector("a[href*=shop]").click()
products = davinder.find_elements_by_xpath("//div[@class='card h-100']")
productAdd = ''
for product in products:
    # print(product.find_element_by_xpath("div/h4").text)
    # don't need to use / before div
    productName = product.find_element_by_xpath("div/h4").text
    # if product name is blackberry than add to card
    if productName == "iphone X":
        productAdd = productName
        # adding to cart using class name
        # product.find_element_by_class_name("btn-info").click()
        # adding to cart using x path
        product.find_element_by_xpath("div/button").click()

# clicking cart button using class name
# davinder.find_element_by_class_name('btn-primary').click()
# clicking cart button using css selector
davinder.find_element_by_css_selector("a[class*='btn-primary']").click()
# clicking checkout button using class name
# davinder.find_element_by_class_name('btn-success').click()
cartItem = davinder.find_element_by_xpath("//h4['link-text = iphone X']").text
# check the item add to the cart
print(cartItem, "Added to the Cart")
# assert checking the cart item is same we add before checkout
assert productAdd == cartItem
# it take cart screen shot which item is added
davinder.get_screenshot_as_file("cart.png")
# clicking checkout button using Xpath
davinder.find_element_by_xpath("//button[@class = 'btn btn-success']").click()
# add country name for delivery
davinder.find_element_by_id('country').send_keys("Uni")
# using explicit wait because it take time to show the drop down after enter value
wait = WebDriverWait(davinder, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "United States of America")))
# how to do using Implicit wait
# davinder.implicitly_wait(5)
davinder.find_element_by_link_text("United States of America").click()
# clicking checkbox button using xpath
davinder.find_element_by_xpath("//div[@class = 'checkbox checkbox-primary']").click()
davinder.find_element_by_css_selector("input[type='submit']").click()
success = davinder.find_element_by_class_name("alert-success").text
print(success)
assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in success
# how to get screen shot
# get-screenshot method used to get a screenshot
davinder.get_screenshot_as_file("success.png")
