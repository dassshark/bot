import vk_api
from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json


def home_work(name):
    p = []
    with open(name + '.txt', 'r', encoding="utf-8") as f:
        for line in f:
            p.append(line.strip())
        pp = '\n'.join(p)
    return pp


group_dict = ('Эб1801', 'Эб1802', 'Эб1901', 'Эб1902', 'Эб2001', 'Эб2002', 'Эб2101', 'Эб2102', 'Юб1801', 'Юб1802',
              'Юб1803', 'Юб1901', 'Юб1902', 'Юб1903', 'Юб2001', 'Юб2002', 'Юб2003', 'Юб2101', 'Юб2102', 'Юб2103',
              'Тс1601', 'Тс1602', 'Тс1603', 'Тс1604', 'Тс1701', 'Тс1702', 'Тс1703', 'Тс1704', 'Тс1801', 'Тс1802',
              'Тс1803', 'Тс1804', 'Тс1901', 'Тс1902', 'Тс1903', 'Тс1904', 'Тс2001', 'Тс2002', 'Тс2003', 'Тс2004',
              'Тс2005', 'Тс2101', 'Тс2102', 'Тс2103', 'Тс2104', 'ПИб2001', 'ПИб2101')

GROUP_ID = '209483780'
GROUP_TOKEN = '63e27ad1c3b3e310cf9290047b8b03648c5bbfcc067f2a71dc08f9aa138f9cd8a726713a5c04d5afe5e5d'
API_VERSION = '5.120'

vk_session = VkApi(token=GROUP_TOKEN, api_version=API_VERSION)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id=GROUP_ID)

settings = dict(one_time=False, inline=False)

keyboard1 = VkKeyboard(**settings)

keyboard1.add_button(label='Покажи домашнее задание',
                     color=VkKeyboardColor.POSITIVE)
keyboard1.add_line()

keyboard1.add_button(label='Группа факультета в ВК',
                     color=VkKeyboardColor.SECONDARY)
keyboard1.add_line()

keyboard1.add_button(label='Прикол дня',
                     color=VkKeyboardColor.SECONDARY)

keyboard2 = VkKeyboard(one_time=False, inline=False)
keyboard2.add_button(label='Экономический факультет',
                     color=VkKeyboardColor.POSITIVE)
keyboard2.add_line()
keyboard2.add_button(label='ФТД',
                     color=VkKeyboardColor.POSITIVE)
keyboard2.add_line()
keyboard2.add_button(label='Юридический факультет',
                     color=VkKeyboardColor.POSITIVE)
keyboard2.add_line()
keyboard2.add_button(label='Назад', color=VkKeyboardColor.NEGATIVE)

keyboard3 = VkKeyboard(one_time=False, inline=False)

keyboard3.add_button(label='Эб1801',
                     color=VkKeyboardColor.POSITIVE)
keyboard3.add_button(label='Эб1802',
                     color=VkKeyboardColor.POSITIVE)
keyboard3.add_line()
keyboard3.add_button(label='Эб1901',
                     color=VkKeyboardColor.POSITIVE)
keyboard3.add_button(label='Эб1902',
                     color=VkKeyboardColor.POSITIVE)
keyboard3.add_line()
keyboard3.add_button(label='Эб2001',
                     color=VkKeyboardColor.POSITIVE)
keyboard3.add_button(label='Эб2002',
                     color=VkKeyboardColor.POSITIVE)
keyboard3.add_line()
keyboard3.add_button(label='Эб2101',
                     color=VkKeyboardColor.POSITIVE)
keyboard3.add_button(label='Эб2102',
                     color=VkKeyboardColor.POSITIVE)
keyboard3.add_line()
keyboard3.add_button(label='Назад', color=VkKeyboardColor.NEGATIVE)

keyboard4 = VkKeyboard(one_time=False, inline=False)

keyboard4.add_button(label='Юб1801',
                     color=VkKeyboardColor.POSITIVE)
keyboard4.add_button(label='Юб1802',
                     color=VkKeyboardColor.POSITIVE)
keyboard4.add_button(label='Юб1803',
                     color=VkKeyboardColor.POSITIVE)
keyboard4.add_line()
keyboard4.add_button(label='Юб1901',
                     color=VkKeyboardColor.POSITIVE)
keyboard4.add_button(label='Юб1902',
                     color=VkKeyboardColor.POSITIVE)
keyboard4.add_button(label='Юб1903',
                     color=VkKeyboardColor.POSITIVE)
keyboard4.add_line()
keyboard4.add_button(label='Юб2001',
                     color=VkKeyboardColor.POSITIVE)
keyboard4.add_button(label='Юб2002',
                     color=VkKeyboardColor.POSITIVE)
keyboard4.add_button(label='Юб2003',
                     color=VkKeyboardColor.POSITIVE)
keyboard4.add_line()
keyboard4.add_button(label='Юб2101',
                     color=VkKeyboardColor.POSITIVE)
keyboard4.add_button(label='Юб2102',
                     color=VkKeyboardColor.POSITIVE)
keyboard4.add_button(label='Юб2103',
                     color=VkKeyboardColor.POSITIVE)
keyboard4.add_line()
keyboard4.add_button(label='Назад', color=VkKeyboardColor.NEGATIVE)

keyboard5 = VkKeyboard(one_time=False, inline=False)

keyboard5.add_button(label='Тс1701',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_button(label='Тс1702',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_button(label='Тс1703',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_button(label='Тс1704',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_line()
keyboard5.add_button(label='Тс1801',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_button(label='Тс1802',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_button(label='Тс1803',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_button(label='Тс1804',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_line()
keyboard5.add_button(label='Тс1901',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_button(label='Тс1902',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_button(label='Тс1903',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_button(label='Тс1904',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_line()
keyboard5.add_button(label='Тс2001',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_button(label='Тс2002',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_button(label='Тс2003',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_button(label='Тс2004',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_line()
keyboard5.add_button(label='Тс2101',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_button(label='Тс2102',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_button(label='Тс2103',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_button(label='Тс2104',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_line()
keyboard5.add_button(label='Тс2005',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_button(label='ПИб2001',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_button(label='ПИб2101',
                     color=VkKeyboardColor.POSITIVE)
keyboard5.add_line()
keyboard5.add_button(label='Назад', color=VkKeyboardColor.NEGATIVE)

keyboard6 = VkKeyboard(one_time=False, inline=False)
keyboard6.add_callback_button(label='Экономический',
                              color=VkKeyboardColor.POSITIVE,
                              payload={"type": "open_link", "link": "https://vk.com/club153802219"})
keyboard6.add_line()
keyboard6.add_callback_button(label='Таможенное дело',
                              color=VkKeyboardColor.POSITIVE,
                              payload={"type": "open_link", "link": "https://vk.com/club150062116"})
keyboard6.add_line()
keyboard6.add_callback_button(label='Юридический',
                              color=VkKeyboardColor.POSITIVE,
                              payload={"type": "open_link", "link": "https://vk.com/rfrta2018"})
keyboard6.add_line()
keyboard6.add_button(label='Назад', color=VkKeyboardColor.NEGATIVE)

upload = vk_api.VkUpload(vk)
photo = upload.photo_messages('mem.jpg')
owner_id = photo[0]['owner_id']
photo_id = photo[0]['id']
access_key = photo[0]['access_key']
attachment = f'photo{owner_id}_{photo_id}_{access_key}'

f_toggle: bool = False
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_user:
            request = event.obj.message['text']
            if request == 'привет' or request == 'Привет' or request == 'Начать':
                vk.messages.send(
                    user_id=event.obj.message['from_id'],
                    random_id=get_random_id(),
                    peer_id=event.obj.message['from_id'],
                    keyboard=keyboard1.get_keyboard(),
                    message='Приветик! \nЯ попытаюсь помочь тебе :) \nВыбери из списка то, что тебе надо')
            elif request == 'Группа факультета в ВК':
                vk.messages.send(
                    user_id=event.obj.message['from_id'],
                    random_id=get_random_id(),
                    peer_id=event.obj.message['from_id'],
                    keyboard=keyboard6.get_keyboard(),
                    message='Выбери свой факультет')
            elif request == 'Прикол дня':
                vk.messages.send(
                    peer_id=event.obj.message['from_id'],
                    random_id=0,
                    keyboard=keyboard1.get_keyboard(),
                    message='He-he, classic',
                    attachment=attachment)
            elif request == 'Покажи домашнее задание':
                vk.messages.send(
                    user_id=event.obj.message['from_id'],
                    random_id=get_random_id(),
                    peer_id=event.obj.message['from_id'],
                    keyboard=keyboard2.get_keyboard(),
                    message='Выбери свой факультет')
            elif request == 'Экономический факультет':
                vk.messages.send(
                    user_id=event.obj.message['from_id'],
                    random_id=get_random_id(),
                    peer_id=event.obj.message['from_id'],
                    keyboard=keyboard3.get_keyboard(),
                    message='Выбери свою группу')
            elif request == 'Юридический факультет':
                vk.messages.send(
                    user_id=event.obj.message['from_id'],
                    random_id=get_random_id(),
                    peer_id=event.obj.message['from_id'],
                    keyboard=keyboard4.get_keyboard(),
                    message='Выбери свою группу')
            elif request == 'ФТД':
                vk.messages.send(
                    user_id=event.obj.message['from_id'],
                    random_id=get_random_id(),
                    peer_id=event.obj.message['from_id'],
                    keyboard=keyboard5.get_keyboard(),
                    message='Выбери свою группу')
            elif request == 'Назад':
                vk.messages.send(
                    user_id=event.obj.message['from_id'],
                    random_id=get_random_id(),
                    peer_id=event.obj.message['from_id'],
                    keyboard=keyboard1.get_keyboard(),
                    message='Пам-пам. \nВыбирай еще раз :)')
            for group in group_dict:
                if request == group:
                    vk.messages.send(
                        user_id=event.obj.message['from_id'],
                        random_id=get_random_id(),
                        peer_id=event.obj.message['from_id'],
                        keyboard=keyboard1.get_keyboard(),
                        message=home_work(request))
            if request != 'привет' and request != 'Привет' and request != 'Начать' and request != 'Назад' and \
                    request != 'Покажи домашнее задание' and request != 'Экономический факультет' and request != 'Юридический факультет' \
                    and request != 'ФТД' and request != 'Эб1801' and request != 'Эб1802' and request != 'Эб1901' and request != 'Эб1902' and \
                    request != 'Эб2001' and request != 'Эб2002' and request != 'Эб2101' and request != 'Эб2102' and request != 'Юб1801' \
                    and request != 'Юб1802' and request != 'Юб1901' and request != 'Юб1902' and request != 'Юб1903' and request != 'Юб2001' \
                    and request != 'Юб2002' and request != 'Юб2003' and request != 'Юб2101' and request != 'Юб2102' and request != 'Юб2103' \
                    and request != 'Тс1601' and request != 'Тс1602' and request != 'Тс1603' and request != 'Тс1604' and request != 'Тс1701' \
                    and request != 'Тс1702' and request != 'Тс1703' and request != 'Тс1704' and request != 'Тс1801' and request != 'Тс1802' \
                    and request != 'Тс1803' and request != 'Тс1804' and request != 'Тс1901' and request != 'Тс1902' and request != 'Тс1903' \
                    and request != 'Тс1904' and request != 'Тс2001' and request != 'Тс2002' and request != 'Тс2003' and request != 'Тс2004' \
                    and request != 'Тс2005' and request != 'Тс2101' and request != 'Тс2102' and request != 'Тс2103' and request != 'Тс2104' \
                    and request != 'ПИб2001' and request != 'ПИб2101' and request != 'Юб1803' and request != 'Группа факультета в ВК' \
                    and request != 'Прикол дня':
                vk.messages.send(
                    user_id=event.obj.message['from_id'],
                    random_id=get_random_id(),
                    peer_id=event.obj.message['from_id'],
                    keyboard=keyboard1.get_keyboard(),
                    message='Я тебя не понимаю :( \nНапиши мне: \"Привет\"')

    elif event.type == VkBotEventType.MESSAGE_EVENT:
        if event.object.payload.get('type') == "open_link":
            r = vk.messages.sendMessageEventAnswer(
                event_id=event.object.event_id,
                user_id=event.object.user_id,
                peer_id=event.object.peer_id,
                message='',
                event_data=json.dumps(event.object.payload))

if __name__ == '__main__':
    print()
