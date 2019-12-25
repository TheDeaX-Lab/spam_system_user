import random
from vk_api import VkApi, Captcha
import json
from selenium.webdriver import Chrome


class VKManager:
    def __init__(self, login_file="login.json"):
        with open(login_file, "r") as f:
            data = json.load(f)
        self.session = VkApi(**data, auth_handler=self.auth_handler, captcha_handler=self.captcha_handler)
        self.session.auth()
        self.vk = self.session.get_api()

    def auth_handler(self):
        key = input("Напишите код безопасности: ")
        remember_device = True
        return key, remember_device

    def captcha_handler(self, captcha: Captcha):
        self.br.get(captcha.get_url().strip())
        self.br.execute_script("document.body.style.zoom='750%'")
        key = input("Введите каптчу: ")
        return captcha.try_again(key)

    def get_browser(self):
        self.br = Chrome("/usr/bin/chromedriver")
        return self.br

    def get_api(self):
        return self.vk
