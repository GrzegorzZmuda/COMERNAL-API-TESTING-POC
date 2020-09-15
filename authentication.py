from functools import wraps
from flask import request, make_response

def vaildate_user(user, pswd):
    user_accounts = [
        ["jan","123"],
        ["tom","321"],
        ["ian","456"],
        ["al","654"]
    ]
    flag = False
    for i in range(len(user_accounts)):
        if user == user_accounts[i][0] and pswd ==user_accounts[i][1]:
            flag=True
    return flag


def autheniticate(func):
    @wraps(func)
    def decorated(*args,**kwargs):
        auth = request.authorization
        if not auth or not vaildate_user(auth.username, auth.password):
            resp = make_response("Unauthorised",401)
            return resp
        return func(*args,**kwargs)
    return decorated