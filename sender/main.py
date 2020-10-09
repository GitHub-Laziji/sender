from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from resources.config import SEGMENTFAULT_USERNAME, SEGMENTFAULT_PASSWORD

options = Options()
# options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=os.path.abspath('../resources/chromedriver.exe'), options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

driver.get("https://segmentfault.com/")
driver.implicitly_wait(1)
driver.set_window_size(1366, 768)
driver.implicitly_wait(1)
driver.find_element_by_css_selector(".SFRegister.btn-signin").click()
driver.implicitly_wait(1)
driver.find_element_by_css_selector("input[name='username']").send_keys(SEGMENTFAULT_USERNAME)
driver.find_element_by_css_selector("input[name='password']").send_keys(SEGMENTFAULT_PASSWORD)
driver.implicitly_wait(1)
driver.find_element_by_css_selector(".btn-block.btn.btn-primary.pull-right.pl20.pr20").click()
