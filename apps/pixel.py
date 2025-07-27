import requests
import time
import hashlib

# Pixel ma'lumotlari
PIXEL_ID = '875192411363522'
ACCESS_TOKEN = 'EAAgTEBZCty3IBPDkBlBuU9r6wdUdhq2RzEoKfztDByldQjBJZAfkwrc6cQs2thTRRdCpQ396IPi4PnSyWDTntLcuSRk1olfwRsNAeW2EJZAqtQmHDarTEJZB3kvZCybZAoxpsrvKaOdF3ZBFEQDD7lb9dZBLesS3FdpN5NNlbqpdu4XaHfK2TrBt7GFu6fe006dZBfQZDZD'  # bu tokenni Events Manager > Settings dan olasiz

# Foydalanuvchi ma'lumotlari
email = 'shohruxrazakov558@gmail.com'
phone = '+998990009031'


# SHA256 hash
def hash_data(value):
    return hashlib.sha256(value.strip().lower().encode()).hexdigest()


hashed_email = hash_data(email)
hashed_phone = hash_data(phone)

# Hodisa ma'lumotlari
data = {
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

# So‘rov yuborish
url = f'https://graph.facebook.com/v18.0/{PIXEL_ID}/events'
params = {
    'access_token': ACCESS_TOKEN
}
response = requests.post(url, params=params, json=data)

# Natija
print('Status code:', response.status_code)
print('Response:', response.json())
