from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

PATH = "/Users/jacobtornes/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)

used_links = {}

def visitpage(url):
    new_url = url.replace('?src=hashtag_click','')
    print("visiting url", new_url)
    driver.get(new_url)
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@href, "src=hashtag")]'))
        )
    #finner  alle hashtaglinks
    hashlinks = driver.find_elements_by_xpath('//a[contains(@href, "src=hashtag")]')

    #loop inn i liste
    hashtag_links = []

    for hasht in hashlinks:
        link = hasht.get_attribute('href')
        if (not link.startswith(new_url) and not link in used_links.keys()):
            hashtag_links.append(link)
    #print(hashtag_links)
    random.shuffle(hashtag_links)
    retval = hashtag_links[0]
    # print('returning', retval)
    used_links[retval] = 1
    return retval

page = "https://twitter.com/search?q=%23Winter"

for counter in range(6):
    page = visitpage(page)
    print("page", page)

driver.quit()