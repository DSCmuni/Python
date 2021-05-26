#Working On Cryptology
#i.e Securing Data In Web Or Off Web Apps
#Am Using Package Base64
#documentation at https://github.com/python/cpython/blob/master/Lib/base64.py

import base64
#encoding (securing data to base 64)
username = "Your UserName/ Email/ Phone/Id"
username_bytes = username.encode('ascii')
base64_bytes = base64.b64encode(username_bytes)
base64_username = base64_bytes.decode('ascii')
print(base64_username)

#ascii is American Standard Code for Information Interchange

password = "Your Paswword"
password_bytes = password.encode('ascii')
base64_bytes = base64.b64encode(password_bytes)
base64_password = base64_bytes.decode('ascii')
print(base64_password)

#decoding
  #username to username human readable data
base64_bytes = base64_username.encode ('ascii')
username_bytes = base64.b64decode(base64_bytes)
username = username_bytes.decode('ascii')
print(username)

#password to password human readable data
base64_bytes = base64_password.encode ('ascii')
password_bytes = base64.b64decode(base64_bytes)
password = password_bytes.decode('ascii')
print(password)

#cryptology is a major aspect in coding in that it allows moving of sensitive
#data through plain docucemts, server scripts and other data manipulation,
#schemes without comprising the sensitivity of the data
#follow more @Olisehenesis1 on github
#olisehgenesis on twitter
#+256700643612

