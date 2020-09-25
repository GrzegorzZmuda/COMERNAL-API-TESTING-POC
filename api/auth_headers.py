from base64 import b64encode


username = 'tom'
password = '321'
c=":"
userAndPass = b64encode(username.encode("ascii") + c.encode("ascii") + password.encode("ascii")).decode("ascii")
correct_header_1 = { 'Authorization' : 'Basic %s' %  userAndPass }

username = 'jan'
password = '123'
userAndPass = b64encode(username.encode("ascii") + c.encode("ascii") + password.encode("ascii")).decode("ascii")
correct_header_2 = { 'Authorization' : 'Basic %s' %  userAndPass }

username = 'ian'
password = '456'
userAndPass = b64encode(username.encode("ascii") + c.encode("ascii") + password.encode("ascii")).decode("ascii")
correct_header_3 = { 'Authorization' : 'Basic %s' %  userAndPass }

username = 'al'
password = '654'
userAndPass = b64encode(username.encode("ascii") + c.encode("ascii") + password.encode("ascii")).decode("ascii")
correct_header_4 = { 'Authorization' : 'Basic %s' %  userAndPass }

username = 'to2m'
password = '32ww1'
userAndPass = b64encode(username.encode("ascii") + c.encode("ascii") + password.encode("ascii")).decode("ascii")
incorrect_header_1 = { 'Authorization' : 'Basic %s' %  userAndPass }