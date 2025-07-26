import requests
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from apps.models import StreamConfig


class BrasletTemplate(TemplateView):
    template_name = 'braslet.html'



@csrf_exempt
def send_order_to_100k(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Eng oxirgi is_active=True bo‘lgan sozlama
            config = StreamConfig.objects.filter(is_active=True).last()
            if not config:
                return JsonResponse({"error": "StreamConfig topilmadi"}, status=400)

            payload = {
                "client_full_name": data.get("name"),
                "customer_phone": data.get("phone"),
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
