import requests
import json
import base64

url= "https://smartkts.com/dntthda/"
username=input("username: ")
#encoding (securing data to base 64)
username_bytes = username.encode('ascii')
#ascii is American Standard Code for Information Interchange
base64_bytes = base64.b64encode(username_bytes)
base64_username = base64_bytes.decode('ascii')
username=base64_username

password=input("password: ")
#encoding (securing data to base 64)
password_bytes = password.encode('ascii')
base64_bytes = base64.b64encode(password_bytes)
base64_password = base64_bytes.decode('ascii')
password = base64_password


body={
    "username" :str(username),
    "password" :str(password),
    "type" :"login"
    }
body = json.dumps(body)
r=requests.request("POST", url, data=body)
print(r.text)
