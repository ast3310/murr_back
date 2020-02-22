import requests
import json

from django.http import JsonResponse

base_frontend_url = 'http://127.0.0.1:8080'
base_backend_url = 'http://127.0.0.1:8000'
# base_frontend_url = 'http://murrengan.ru'
# base_backend_url = 'http://murrengan.ru'

recaptcha_server_token = '6LfLNNcUAAAAAC_GSWQztiI2NVqnJbicZI53SCE9'


def check_recaptcha(token):
    recaptcha = {
        'response': token,
        'secret': recaptcha_server_token
    }

    recaptcha_response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=recaptcha)
    recaptcha_response_text = json.loads(recaptcha_response.text)

    if (recaptcha_response_text['success'] is False) or (recaptcha_response_text['score'] < 0.5):
        return JsonResponse({'recaptcha_response_problem': True,
                             'recaptcha_response_text': recaptcha_response_text})
