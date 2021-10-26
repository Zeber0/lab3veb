import requests


class RequestsApi:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, url):
        return self.session.get(self.base_url + url)

    def head(self, url):
        return self.session.head(self.base_url + url)

    def post(self, url):
        return self.session.post(self.base_url + url)

    def put(self, url):
        return self.session.put(self.base_url + url)

    def __del__(self):
        self.session.close()


a = RequestsApi("https://api.github.com")
b = a.get("/users/Zebr0")
print(b.json())
