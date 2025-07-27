from django.urls import path

from apps.views import BrasletTemplate, send_order_to_100k, send_lead_event

urlpatterns = [
       path('', BrasletTemplate.as_view(), name='braslet_template'),
       path('send-order/', send_order_to_100k, name='send_order_to_100k'),
       path('send-lead-event/', send_lead_event, name='send_lead_event'),
]
