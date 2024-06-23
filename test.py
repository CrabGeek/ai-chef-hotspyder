from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

options.add_argument("--headless")
options.add_argument("--log-level=3")

driver = webdriver.Remote(
   command_executor="http://localhost:4444",
   options=options
)

driver.get("https://www.toutiao.com/trending/7383634462426349577/?category_name=topic_innerflow&event_type=hot_board&log_pb=%7B%22category_name%22%3A%22topic_innerflow%22%2C%22cluster_type%22%3A%222%22%2C%22enter_from%22%3A%22click_category%22%2C%22entrance_hotspot%22%3A%22outside%22%2C%22event_type%22%3A%22hot_board%22%2C%22hot_board_cluster_id%22%3A%227383634462426349577%22%2C%22hot_board_impr_id%22%3A%22202406232030281C589BE4F26AE4153F48%22%2C%22jump_page%22%3A%22hot_board_page%22%2C%22location%22%3A%22news_hot_card%22%2C%22page_location%22%3A%22hot_board_page%22%2C%22rank%22%3A%221%22%2C%22source%22%3A%22trending_tab%22%2C%22style_id%22%3A%2240132%22%2C%22title%22%3A%22%E5%AD%A6%E9%9C%B8%E6%9F%A5%E5%88%86%E6%8E%92%E5%85%A8%E7%9C%81399%E5%90%8D%E7%9E%AC%E9%97%B4%E7%AC%91%E5%AE%B9%E6%B6%88%E5%A4%B1%22%7D&rank=1&style_id=40132&topic_id=7383634462426349577")

WebDriverWait(
            driver, timeout=60
        ).until(lambda b: b.find_element(By.CLASS_NAME, "block-content").is_displayed())



print(driver.title)

driver.close()
driver.quit()
