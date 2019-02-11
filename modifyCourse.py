import requests,random,pprint
import login,findCourse

def modify(name, desc):
    url = 'http://localhost/api/mgr/sq_mgr/'
    list = []
    for i in  findCourse.find():
        list.append(i['id'])
    chooseId = random.sample(list, 1)[0]
    print('随机选择修改的id为', chooseId)
    print('修改前')
    for i in  findCourse.find():
        if i['id'] == chooseId:
            pprint.pprint(i)
    datas = {
        'action': 'modify_course',
        'id': int(chooseId),
        'newdata': '''{
  "name":"%s",
  "desc":"%s",
  "display_idx":"4"
}''' % (name, desc)

            }
    res = requests.put(url, data=datas, cookies={'sessionid': login.loginStsyme()})
    if res.json()['retcode'] == 0:
        print('修改成功')
        print('修改后：')
        for i in findCourse.find():
            if i['id'] == chooseId:
                pprint.pprint(i)
    else:
        print('修改失败')


if __name__ == '__main__':
    modify('rinima111','草泥马')
