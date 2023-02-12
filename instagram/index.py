import requests
from datetime import datetime
from utility.cookieGen import CookieGenerator
from utility.client import ClientSession
from config import ENABLE_INSTAGRAM_SELFBOT, INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD


class InstagramScraper:
    def __init__(self):
        self.session = ClientSession()
        self.loginInfo = None
        if ENABLE_INSTAGRAM_SELFBOT:
            self.loginInfo = self.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)

    def findUsersBySearchQuery(self, query):
        params = {
            'context': 'blended',
            'query': query,
            'include_reel': 'true',
            'search_surface': 'web_top_search',
        }

        response = self.session.get('https://www.instagram.com/api/v1/web/search/topsearch/', params=params)

        if response.status_code == 200:
            return response.json()['users']
        else:
            return {'error': response.status_code, 'msg': response.json()}

    def findUserByName(self, name):
        # cookies = CookieGenerator(self.session)
        # cookies.instagramCookie()

        params = {
            'username': name,
        }

        response = self.session.get(
            'https://www.instagram.com/api/v1/users/web_profile_info/',
            params=params,
        )
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': response.status_code, 'msg': response.json()}

    def login(self, username, password):
        time = int(datetime.now().timestamp())

        data = {
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
            'username': username,
            'queryParams': '{}',
            'optIntoOneTap': 'false',
            'trustedDeviceRecords': '{}',
        }

        response = self.session.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', data=data)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': response.status_code, 'msg': response.json()}




