# from flask import Flask, request, jsonify
# from pyngrok import ngrok
# import requests
# import sys

# app = Flask(__name__)


# INSTANCE_URL = "https://api.maytapi.com/api"
# PRODUCT_ID = "de68250b-bd93-4558-afb6-92ba61dbc367"
# PHONE_ID = "6962"
# API_TOKEN = "5c7d320a-f411-41db-8720-9102d4cbfd65"


# @app.route('/sms', methods=['POST'])
# def sms_reply():

#     try:

#         json_data = request.get_json()
#         phone = json_data['user']['phone']
#         text = json_data['message']['text']

#         print(phone)
#         print(text)

#         url = INSTANCE_URL + "/" + PRODUCT_ID + "/" + PHONE_ID + "/sendMessage"
#         headers = {
#             "Content-Type": "application/json",
#             "x-maytapi-key": API_TOKEN,
#         }

#         body = {"type": "text", "message": text,
#                 "to_number": phone}

#         response = requests.post(url, json=body, headers=headers)

#         return str(json_data)

#     except Exception as e:
#         if repr(e) == "KeyError('user',)":
#             print('that KeyError but its fine')
#         else:
#             print(repr(e))
#         return str("bad_resp")


# if __name__ == '__main__':
#     app.run(debug=True)
