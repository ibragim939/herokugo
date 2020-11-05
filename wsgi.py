from flask import Flask, request, jsonify
import requests


app = Flask(__name__)

INSTANCE_URL = "https://api.maytapi.com/api"
PRODUCT_ID = "de68250b-bd93-4558-afb6-92ba61dbc367"
PHONE_ID = "6962"
API_TOKEN = "5c7d320a-f411-41db-8720-9102d4cbfd65"


@app.route('/', methods=['POST'])
def sms_reply():

    try:

        json_data = request.get_json()
        phone = json_data['user']['phone']
        text = json_data['message']['text']

        baseurl = "https://baza-gai.com.ua/nomer/" + text
        head = {'Accept': 'application/json'}

        url = INSTANCE_URL + "/" + PRODUCT_ID + "/" + PHONE_ID + "/sendMessage"
        headers = {
            "Content-Type": "application/json",
            "x-maytapi-key": API_TOKEN,
        }

        req = requests.get(baseurl, headers=head)

        dic = req.json()
        digits = dic['digits']
        region = dic['region']['name']
        vendor = dic['vendor']
        model = dic['model']
        year = dic['year']
        operations = dic['operations'][0]['notes']
        reg_at = dic['operations'][0]['regAt']

        finaldata = "данные по номеру {}: \nрегион: {}\nмарка: {} {}\nпараметры: {}\nгод выпуска: {}\nдата регистрации: {}".format(
            digits, region, vendor, model, operations, year, reg_at)

        body = {"type": "text", "message": finaldata,
                "to_number": phone}

        requests.post(url, json=body, headers=headers)

        return str(json_data)

    except Exception as e:
        if repr(e) == "KeyError('user',)":
            print('that KeyError but its fine')
        else:
            print(repr(e))
        return str("bad_resp")


if __name__ == "__main__":
    app.run()
