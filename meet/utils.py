# # meet/utils.py

# import jwt
# from datetime import datetime, timedelta
# from django.conf import settings

# def generate_jwt_token(api_key, api_secret):
#     payload = {
#         'iss': api_key,
#         'exp': datetime.utcnow() + timedelta(seconds=3600)  # Expiration dans 1 heure
#     }
#     token = jwt.encode(payload, api_secret, algorithm='HS256')
#     return token.decode('utf-8')  # Décodez le token en chaîne UTF-8 si nécessaire
