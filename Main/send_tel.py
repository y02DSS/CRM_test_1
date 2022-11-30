# # coding: utf-8
# from time import sleep
import requests

# def send_for_sms(email, phone, number, date, organization):
#   text = f'{date} {organization}\nПроведены работы в электроустановках. По ссылке видео отчет.\nhttp://video.energiatrend.ru/post/{str(number)}'
#   for one_phone in phone:
#     requests.post(f'http://ssl.bs00.ru/?method=push_msg&key=6NJ62c5f0cb4785d28150c4a74edc231a53e4e26f917f3d6&text={text}&phone={one_phone}&sender_name=Energiatren')

def send_for_sms(email, phone, number, date, organization):
    text = f'{date} {organization}\nПроведены работы в электроустановках. По ссылке видео отчет.\nhttp://video.energiatrend.ru/post/{str(number)}'
    requests.get(f'https://api.mobizon.kz/service/message/sendsmsmessage?recipient={phone}&text={text}%21&apiKey=kz23c35e56f29982afc325a00c4e014cfd8e0ffc37f8d4a92647875719c2178665c1fa')
    

send_for_sms('za02za02@bk.ru', '87754573563', '4', "2021-07-07 10:00:00", 'My')