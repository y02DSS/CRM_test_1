# # coding: utf-8
# import requests

# def send_for_sms(email, phone, number, date, organization):
#   text = f'{date} {organization}\nПроведены работы в электроустановках. Для просмотра видео-результатов проверки нажмите на ссылку.\nhttp://video.energiatrend.ru/post/{str(number)}'
#   for one_phone in phone:
#     return requests.post(f'http://ssl.bs00.ru/?method=push_msg&key=6NJ62c5f0cb4785d28150c4a74edc231a53e4e26f917f3d6&text={text}&phone={one_phone}&sender_name=Energiatren')

