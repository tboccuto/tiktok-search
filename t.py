from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pyautogui as p

class Tik:
  def __init__(self, headless, username, chrome=False):
    opt = Options()
    opt.add_argument("--window-size=1920,1080")
    opt.add_argument("--incognito")
    if headless:
        opt.add_argument('--headless')
    if chrome:
      self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=opt)
    self.username = username
    
  def search_tik_tok(self):
    self.driver.get('https://www.google.com/')
    WebDriverWait(self.driver,5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, \
    'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input'))).send_keys('TikTok '+self.username)
    p.press('enter')
    
    WebDriverWait(self.driver,5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, \
      '#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e > div > a > h3'))).click()
    
    self.driver.get('https://www.google.com/')

  def _repeat(self, times=100_000_000, verbose=True):
    iters = 0
    for iters in range(times):
      self.search_tik_tok()
      if verbose: print(f'iters: {iters}')

