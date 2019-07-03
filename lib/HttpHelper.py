# -*-coding:utf-8 -*-
import io
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HttpHelper:
    # 自动化测试核心脚本
    def __init__(self, options, browser_type, path):
        options = self.get_default_options(options)

        if browser_type == 'chrome':
            chrome_options = ChromeOptions()
            if(options['hidden_ui']):
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--disable-gpu')
            self.browser = webdriver.Chrome(chrome_options=chrome_options)
        elif browser_type == 'firefox':
            firefox_options = FirefoxOptions()
            if(options['hidden_ui']):
                firefox_options.set_headless()
            self.browser = webdriver.Firefox(firefox_options=firefox_options)
        elif browser_type == 'chrome360':
            chrome_options = ChromeOptions()
            chrome_options.binary_location = path['360']
            if(options['hidden_ui']):
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--disable-gpu')
            self.browser = webdriver.Chrome(chrome_options=chrome_options)
        elif browser_type == 'ie':
            self.browser = webdriver.Ie()

        self.wait = WebDriverWait(self.browser, options['timeout'])

    # 获取默认配置
    def get_default_options(self, options):
        default_options = {
            'hidden_ui': True,  # 该值指示是否显示ui界面，默认不显示
            'timeout': 100      # 该值指示超时时间，默认100毫秒
        }
        return dict(default_options, **options)

    # 访问页面
    def get(self, url):
        self.browser.get(url)

    # 获取dom元素
    def get_dom(self, xpath):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    # 获取浏览器
    def get_browser(self):
        return self.browser

    # 退出浏览器
    def quit(self):
        self.browser.quit()
