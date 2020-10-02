from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


options = Options()
# options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=os.path.abspath('./chromedriver.exe'), options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

driver.get("https://segmentfault.com/")
