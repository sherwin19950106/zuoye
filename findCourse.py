import requests,pprint
import login

def find():
    url = 'http://localhost/api/mgr/sq_mgr/'
    datas = {
        'action': 'list_course',
        'pagenum':1,
        'pagesize':20
    }
    cookie = {
        'sessionid': login.loginStsyme()
    }
    res = requests.get(url, params=datas, cookies=cookie)
    if res.json()['retcode'] == 0:
        return res.json()['retlist']
    else:
        print('为获取到课程')


if __name__ == '__main__':
    for i in find():
        print(i['id'])