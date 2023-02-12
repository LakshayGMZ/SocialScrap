import requests
import config
from utility.cookieGen import CookieGenerator

class ClientSession(requests.Session):
    def __init__(self):
        super().__init__()
        self.proxies = config.PROXY
        if config.USER_AGENT:
            self.headers['user-agent'] = config.USER_AGENT
        CookieGenerator(self).instagramCookie()
