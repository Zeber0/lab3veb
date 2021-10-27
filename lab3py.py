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
        res=self.session.get(self.base_url + url,headers=self.query, **kwargs)
        if res.status_code!=200:
            return None
        else:
            return res

    def post(self, url, **kwargs):
        res=self.session.post(self.base_url + url, headers=self.query, **kwargs)
        if res.status_code!=200:
            return None
        else:
            return res

    def __del__(self):
        self.session.close()

a = RequestsApi("https://httpbin.org")
a.updq({"user-agent": "test"})
response_1 = a.get("/get", params={"key_1":"value_1"})
if response_1 is not None:
	print("ok")
response = a.post("/status/400", data={"key_2":"value_2"})
if response is None:
	print("ok")

