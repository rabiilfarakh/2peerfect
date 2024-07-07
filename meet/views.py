# views.py

import requests # type: ignore
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import jwt
from datetime import datetime, timedelta
import logging
import json

logger = logging.getLogger(__name__)

@csrf_exempt
def create_meeting(request):
    print(request)  # Affiche l'objet request dans la console
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            access_token = generate_jwt_token()

            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }

            zoom_data = {
                'topic': json_data.get('topic', 'Meeting Title'),
                'type': json_data.get('type', 2),
                'start_time': json_data.get('start_time', '2024-06-15T12:00:00Z'),
                'duration': json_data.get('duration', 60),
                'timezone': json_data.get('timezone', 'Europe/Paris')
            }

            response = requests.post(f'https://api.zoom.us/v2/users/{settings.ZOOM_API_ACCOUNT_ID}/meetings', headers=headers, json=zoom_data)

            if response.status_code == 201:
                return JsonResponse(response.json())
            else:
                error_message = {'error': 'Failed to create meeting'}
                if response.text:
                    error_message['detail'] = response.text
                logger.error(f"Failed to create Zoom meeting: {response.status_code} - {response.text}")
                return JsonResponse(error_message, status=response.status_code)

        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON data: {str(e)}")
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def generate_jwt_token():
    api_key = settings.ZOOM_API_KEY
    api_secret = settings.ZOOM_API_SECRET

    payload = {
        'iss': api_key,
        'exp': datetime.utcnow() + timedelta(seconds=3600) 
    }

    token = jwt.encode(payload, api_secret, algorithm='HS256')
    return token
