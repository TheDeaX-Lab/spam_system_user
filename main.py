from module import VKManager
from models import *
from pprint import *
import time
import random
import json

with open("config.json") as f:
    data = json.load(f)
manager = VKManager()
vk = manager.get_api()
browser = manager.get_browser()

attack_target = data["attack_id"]
while True:
    try:
        target_friends = vk.friends.get(user_id=attack_target, fields="""online,
    can_send_friend_request,
    can_write_private_message """.strip())['items']
        with open(f"{attack_target}.json", 'w') as f:
            json.dump(f, target_friends)
    except:
        with open(f"{attack_target}.json") as f:
            target_friends = json.load(f)
    for i in target_friends:
        if i["online"] and i["can_send_friend_request"] and i["can_write_private_message"]:
            if not SendedUser.get_or_none(from_user_id=attack_target, to_user_id=i["id"]):
                try:
                    text = data["text_format"].format(**i, attack_id=attack_target)
                    vk.friends.add(user_id=i["id"], text=text)
                    SendedUser(from_user_id=attack_target, to_user_id=i["id"]).save()
                    time.sleep(random.uniform(0.2, 2))
                except:
                    continue
    time.sleep(1)
