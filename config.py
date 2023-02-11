PROXY = ""
PORT = 8080
USER_AGENT = "Instagram 126.0.0.25.121 Android (23/6.0.1; 320dpi; 720x1280; samsung; SM-A310F; a3xelte; samsungexynos7580; en_GB; 110937453)"


# Don't change these
PROXY = {'http': f"http://{PROXY}/", 'https': f"https://{PROXY}/"} if PROXY else None
PORT = PORT or 8081
