import hashlib
import time

import requests
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from apps.models import StreamConfig

PIXEL_ID = '875192411363522'
ACCESS_TOKEN = 'EAAgTEBZCty3IBPDkBlBuU9r6wdUdhq2RzEoKfztDByldQjBJZAfkwrc6cQs2thTRRdCpQ396IPi4PnSyWDTntLcuSRk1olfwRsNAeW2EJZAqtQmHDarTEJZB3kvZCybZAoxpsrvKaOdF3ZBFEQDD7lb9dZBLesS3FdpN5NNlbqpdu4XaHfK2TrBt7GFu6fe006dZBfQZDZD'


class BrasletTemplate(TemplateView):
    template_name = 'braslet.html'


@csrf_exempt
def send_order_to_100k(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            config = StreamConfig.objects.filter(is_active=True).last()
            if not config:
                return JsonResponse({"error": "StreamConfig topilmadi"}, status=400)

            payload = {
                "client_full_name": data.get("client_full_name"),
                "customer_phone": data.get("customer_phone"),
                "stream_id": config.stream_id,
                "region_id": config.region_id,
                "facebook_lead_id": "123456789",
                "facebook_add_id": "987654321",
                "facebook_form_id": "1122334455",
                "facebook_campaign_id": "55667788",
                "fbclid": "fbclid123",
                "fbc": "fb.1.1234567890.abcdef",
                "fbp": "fb.1.0987654321.zxywvu",
                "customer_ip": request.META.get("REMOTE_ADDR"),
                "customer_user_agent": request.META.get("HTTP_USER_AGENT")
            }

            response = requests.post(
                "https://api.100k.uz/api/shop/v1/orders/target",
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                json=payload
            )

            return JsonResponse(response.json(), status=response.status_code)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST method allowed"}, status=405)


def hash_data(value):
    return hashlib.sha256(value.strip().lower().encode()).hexdigest()


@csrf_exempt
def send_lead_event(request):
    if request.method == 'POST':
        try:
            data_json = json.loads(request.body)
            email = data_json.get('email')
            phone = data_json.get('phone')

            if not email or not phone:
                return JsonResponse({'error': 'Email va telefon kerak'}, status=400)

            hashed_email = hash_data(email)
            hashed_phone = hash_data(phone)

            payload = {
                'data': [
                    {
                        'event_name': 'Lead',
                        'event_time': int(time.time()),
                        'action_source': 'website',
                        'user_data': {
                            'em': [hashed_email],
                            'ph': [hashed_phone],
                        }
                    }
                ]
            }

            url = f'https://graph.facebook.com/v18.0/{PIXEL_ID}/events'
            params = {'access_token': ACCESS_TOKEN}

            fb_response = requests.post(url, params=params, json=payload)

            return JsonResponse(fb_response.json(), status=fb_response.status_code)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'POST method only'}, status=405)
