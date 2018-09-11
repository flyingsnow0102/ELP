from django.http import HttpResponse
import pymysql
import json
import sys

def getDao():
    config = {
        'host': '39.105.96.239',
        'port': 3306,
        'user': 'root',
        'password': '662662',
        'db': 'ELP',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
    }
    return pymysql.connect(**config)

def getData(db, sql):
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
    except Exception as e:
        print(e)
        return 'HAHA'
    finally:
        db.close()
        cursor.close()
    return data


def getTestNameList(requset):
    if requset.GET['gradeType'] == 'A':
        sql = 'select * from test_a'
        data = getData(getDao(), sql)
        return HttpResponse(json.dumps(data))
    else:
        sql = 'select * from test_b'
        return HttpResponse(json.dumps(getData(getDao(), sql)))


def getTestQuestions(request):
    jsonFile = open(sys.path[0] + "/ELP/json/test.json", 'r', encoding='utf-8')
    json = jsonFile.read()
    print("\n\n\n" + json)
    return HttpResponse(json)


def getFile(request):
    print('testTheTape')
    test_id = request.GET['test_id']
    print("\n\n\n" + test_id)
    file = open(sys.path[0] + "/ELP/music/" + test_id + ".mp3", 'rb')
    fileUp = file.read()
    return HttpResponse(fileUp, content_type='audio/mpeg')