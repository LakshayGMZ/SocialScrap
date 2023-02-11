import requests
from utility.cookieGen import CookieGenerator
from utility.client import ClientSession


class InstagramScraper:
    def __init__(self):
        self.session = ClientSession()

    def findUserByName(self, name):
        cookies = CookieGenerator(self.session)
        cookies.instagramCookie()

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
            return {'error': 404, 'msg': "Account not found"}

