import requests

def loginStsyme():
    url = 'http://localhost/api/mgr/loginReq'
    data = {
        'username': 'auto',
        'password': 'sdfsdfsdf'
    }
    res = requests.post(url, data=data)
    if res.json()['retcode'] == 0:
        sessionid = res.headers['Set-Cookie'].split(';')[0].split('=')[1]
        return sessionid
    else:
        return '未获取到sessionid'


if __name__ == '__main__':
    print(loginStsyme())
