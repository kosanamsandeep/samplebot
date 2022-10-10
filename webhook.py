import json
import os
import requests

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():

    req = request.get_json(silent=True, force=True)
    
    print(json.dumps(req, indent=4))
    
    res = makeResponse(req)
    
    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeResponse(req):
    print("result is", req.get("result"))

    print("type of request is",type(req))

    result = req.get("queryResult")

    parameters = result.get("parameters")

    city = parameters.get("geo-city")
    date = parameters.get("date")
    cars = parameters.get("cars")

    print(f"city is {city} and date is {date} and cars type is {cars}")

    action = result.get("action")
    
    if action == "bookcar":
        parameters = result.get("parameters")
        city = parameters.get("geo-city")
        date = parameters.get("date")
        cars = parameters.get("cars")

    # date = parameters.get("date")
    # r=requests.get('http://api.openweathermap.org/data/2.5/forecast?q='+city+'&appid=06f070197b1f60e55231f8c46658d077')
    # json_object = r.json()
    # weather=json_object['list']
    # for i in range(0,30):
    #     if date in weather[i]['dt_txt']:
    #         condition= weather[i]['weather'][0]['description']
    #         break
        speech = "This is a test request"
    else:

        speech = "something wronggg"
    return {
    "speech": speech,
    "displayText": speech,
    "source": "apiai-weather-webhook"
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')

















