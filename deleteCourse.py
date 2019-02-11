import requests,random,pprint
import findCourse,login


def delete():
    url = 'http://localhost/api/mgr/sq_mgr/'
    list = []
    print('删除前：')
    pprint.pprint(findCourse.find())
    for i in findCourse.find():
        list.append(i['id'])
    chooseId = random.sample(list, 1)[0]
    print('随机选择修改的id为', chooseId)
    data = {
        'action':'delete_course',
        'id': int(chooseId)
    }
    res = requests.delete(url, data=data, cookies={'sessionid': login.loginStsyme()})
    if res.json()['retcode'] == 0:
        print('删除%s成功' % (chooseId,))
        print('删除后：')
        pprint.pprint(findCourse.find())
    else:
        print('删除%s失败' % (chooseId,))

delete()