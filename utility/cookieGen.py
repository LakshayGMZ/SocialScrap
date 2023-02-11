class CookieGenerator:
    def __init__(self, session):
        self.session = session

    def instagramCookie(self):
        self.session.get("https://instagram.com/")
        self.session.get("https://www.instagram.com/api/v1/public/landing_info/")

        self.session.headers['x-csrftoken'] = self.session.cookies['csrftoken']
        self.session.headers['x-requested-with'] = 'XMLHttpRequest'


