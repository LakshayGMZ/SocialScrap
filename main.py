from instagram.index import InstagramScraper

if __name__ == '__main__':
    uname = str(input("Enter username to search: "))
    instaScraper = InstagramScraper()
    data = instaScraper.findUserByName(uname)
    print(data)

