import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


def TrendSearch_Google(regions, browser):
    for region in regions:
        for trend in region.getTrends():
            browser.get('http://www.google.com')
            search = browser.find_element_by_name('q')
            search.send_keys(trend)
            search.send_keys(Keys.RETURN)
            time.sleep(5)


def TrendSearchPerRegionThroughSpecificMedia(regions, browser):
    for region in regions:
        for medium in region.getMedia():
            for trend in region.getTrends():
                browser.get(medium)
                articles = browser.find_elements_by_tag_name('article')
                for article in articles:
                    print article.text
