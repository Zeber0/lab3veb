import requests


class RequestsApi:
    query = {}
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.updq()
    def updq(self,q={"user-agent":"test_client"}):
        self.query=q
    def get(self, url, **kwargs):
        return self.session.get(self.base_url + url,headers=self.query, **kwargs)

    def head(self, url, **kwargs):
        return self.session.head(self.base_url + url, **kwargs)

    def post(self, url, **kwargs):
        return self.session.post(self.base_url + url, headers=self.query, **kwargs)

    def put(self, url, **kwargs):
        return self.session.put(self.base_url + url, **kwargs)
    def __del__(self):
        self.session.close()

a = RequestsApi("https://httpbin.org")
response_3=a.get("/get", params={"key_1":"value_1"})
print (response_3.text)
a.updq({"user-agent": "test"})
response_1 = a.get("/get", params={"key_1":"value_1"})
print (response_1.text)
a.updq()
response = a.post("/post", data={"key_2":"value_2"})
print (response.text)

