from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://automatetheboringstuff.com/')
elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > div:nth-child(3) > center > a:nth-child(1) > img')
elem
elem.click()

# # elems = browser.find_elements_by_css_selector('p')  #paragraph
# # print(len(elems))
# # searchElem = browser.find_element_by_css_selector('.search-field')
# # searchElem.send_keys('zophie')
# # searchElem.submit()
# # browser.back()
# # browser.forward()
# # browser.refresh()
# # browser.quit()

# browser.get('https://automatetheboringstuff.com/')
# # searchElem = browser.find_element_by_css_selector('.search-field')
# # searchElem.send_keys('zophie')
# # elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > div:nth-child(4) > center > a:nth-child(3) > img')
# # elem1 = browser.find_element_by_css_selector('<h1>Automate the Boring Stuff with Python</h1>')
# elem1 = browser.find_element_by_css_selector('body')
# print(elem1.text)

# # To import selenium, you need to run: "from selenium import webdriver" (and not "import selenium").
# # To open the browser, run: browser = webdriver.Firefox()
# # To send the browser to a URL, run: browser.get(‘https://inventwithpython.com')
# # The browser.find_elements_by_css_selector() method will return a list of WebElement objects:
# #     elems = browser.find_elements_by_css_selector(‘img')
# # WebElement objects have a "text" variable that contains the element's HTML in a string: elems[0].text
# # The click() method will click on an element in the browser.
# # The send_keys() method will type into a specific element in the browser.
# # The submit() method will simulate clicking on the Submit button for a form.
# # The browser can also be controlled with these methods: back(), forward(), refresh(), quit().