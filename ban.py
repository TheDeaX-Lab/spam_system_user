from module import VKManager
from models import *
from pprint import *
from vk_api.utils import get_random_id
import time
import random
import json

with open("config.json") as f:
    data = json.load(f)
manager = VKManager()
vk = manager.get_api()
browser = manager.get_browser()

attack_target = data["attack_id"]

vk.account.ban(owner_id=attack_target)
