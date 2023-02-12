PROXY = ""
PORT = 8080
# Choose user agent wisely. changing user agents may break the code
# due to 404 error returned from insta servers with useragent mismatch error
USER_AGENT = "Instagram 126.0.0.25.121 Android (23/6.0.1; 320dpi; 720x1280; samsung; SM-A310F; a3xelte; samsungexynos7580; en_GB; 110937453)"

# Below used to automate your instagram account  like liking the post and messaging from your account
ENABLE_INSTAGRAM_SELFBOT = False
# If setting the above value to False, the value below to be ignored, else to be filled correctly

INSTAGRAM_USERNAME = ""
INSTAGRAM_PASSWORD = ""









# Don't change these
PROXY = {'http': f"http://{PROXY}/", 'https': f"https://{PROXY}/"} if PROXY else None
PORT = PORT or 8082

if not ENABLE_INSTAGRAM_SELFBOT:
    INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD = None, None
