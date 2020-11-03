from flask import Flask, request, jsonify
import requests


app = Flask(__name__)

# INSTANCE_URL = "https://api.maytapi.com/api"
# PRODUCT_ID = "de68250b-bd93-4558-afb6-92ba61dbc367"
# PHONE_ID = "6962"
# API_TOKEN = "5c7d320a-f411-41db-8720-9102d4cbfd65"


# @app.route("/")
# def sms_reply():

#     try:

#         json_data = request.get_json()
#         phone = json_data['user']['phone']
#         text = json_data['message']['text']

#         url = INSTANCE_URL + "/" + PRODUCT_ID + "/" + PHONE_ID + "/sendMessage"
#         headers = {
#             "Content-Type": "application/json",
#             "x-maytapi-key": API_TOKEN,
#         }

#         body = {"type": "text", "message": text,
#                 "to_number": phone}

#         requests.post(url, json=body, headers=headers)

#         return str(json_data)

#     except Exception as e:
#         if repr(e) == "KeyError('user',)":
#             print('that KeyError but its fine')
#         else:
#             print(repr(e))
#         return str("bad_resp")


@app.route("/testy")
def testy():

    json_data = request.get_json()

    url = "https://api.maytapi.com/api" + "/" + \
        "de68250b-bd93-4558-afb6-92ba61dbc367" + "/" + "6962" + "/sendMessage"

    headers = {
        "Content-Type": "application/json",
        "x-maytapi-key": "5c7d320a-f411-41db-8720-9102d4cbfd65",
    }

    body = {"type": "text", "message": "text",
            "to_number": "79785921959"}
    requests.post(url, json=body, headers=headers)
    
    return str(json_data)


if __name__ == "__main__":
    app.run()
