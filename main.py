import json
import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask import request

app = Flask(__name__)

class Crawler():
    baseURL = "http://www.tlkg.com/activityweb/activityMvList.kg"

    def request(self, race_id):
        # print(requests.get(self.baseURL+race_id).url)
        payload = {'key': 0, 'page': 1, 'actid': race_id}
        return requests.post(self.baseURL, data=payload).content
    def parse(self, response):
        print(json.loads(response)['content'])
        return json.dumps(json.loads(response)['content'],sort_keys = True ,indent = 4, ensure_ascii=False).encode('utf8')
        # return json.loads(response)['content']
        # json.dumps(response,sort_keys = True ,indent = 4 )
        # soup = BeautifulSoup(response, 'html.parser')
        # yield soup.find_all('div', { "class" : "musicname" })
        # yield (soup.find_all('div', { "class" : "mvname" }))

crawler = Crawler()

@app.route("/index")
def index():
    actid = request.args.get('actid')
    if actid>0:
        print actid
        content = crawler.request(actid)
        result = crawler.parse(content)
        return (result)
    else:
        return 'Yooooo'

if __name__ == '__main__':
    app.run()
    
    