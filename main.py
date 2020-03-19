#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
from datetime import datetime

# Credenciales de API tweeter
CONSUMER_KEY = 'xxxxxxx'
CONSUMER_SECRET = 'xxxxxxx'
ACCESS_TOKEN = 'xxxxxxx'
ACCESS_TOKEN_SECRET = 'xxxxxxx'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Enlace a API
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)


# Mi usuario (reemplaza por tu nombre de usuario)
miusuario = 'El_Masta'

# Obtiene mis seguidores
for user in tweepy.Cursor(api.friends, screen_name=miusuario).items(2):
    print(f'\nSeguidor:\t{user.screen_name}')
    # Obtiene el último estado
    for status in tweepy.Cursor(api.user_timeline, id=user.id).items(1):
        # Verifica la fecha de ultimo estado (aa,m,d)
        if status.created_at < datetime(2019, 12, 1):
            print('Sin actividad reciente')
            # Lo dejamos de seguir
            api.destroy_friendship(id=user.id)
        else:
            print('Activo')
