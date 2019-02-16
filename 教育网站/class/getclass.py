import json
import requests
import pymysql
import threading
db = pymysql.connect(
    "localhost",
    "root",
    "edu123456",
    "work2",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
}

requestData = [55, 5, 6]#, 8, 9, 10, 19]
nameData = ['一年级','二年级','三年级','四年级','五年级','六年级','初一','初二','初三','高一','高二','高三','']
nameData2 = ['语文','数学','英语','物理','化学','生物','地理','历史','政治']
pageData = [7, 47, 105, 2, 5, 10, 25]


def getJson(tag1, grade,page):
    url = 'http://www.class.cn/ajax/course/list_course'
    data = {
        'type_id': grade,
        'tags[0]': tag1,
        'all_course': '1',
        'sort': 'publishtime-desc',
        'page': page
    }
    html = requests.get(url, params=data).text
    return html

def getJson2(tag1,tag2,grade, page):
    url = 'http://www.class.cn/ajax/course/list_course'
    data = {
        'type_id': grade,
        'tags[0]': tag1,
        'tags[1]': tag2,
        'all_course': '1',
        'sort': 'publishtime-desc',
        'page': page
    }
    html = requests.get(url, params=data).text
    return html
def work2():
    pass

def work():
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "edu123456",
        "work2",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    for grade in [6]:
        for i in range(9,len(nameData)-2):
            tag1=i+2
            for j in range(len(nameData2)):
                tag2=j+15
                for page in range(1,30):
                    gradeName=nameData[i]
                    subjectName=nameData2[j]
                    html = getJson2(tag1,tag2,grade,page)
                    js = json.loads(html)['data']
                    courses=[]
                    try:
                        courses = js['course']
                    except :
                        continue
                    for course in courses:
                        course_id = course['course_id']
                        img = course['img_name']
                        courseName = course['title']
                        print(course_id, img)
                        sql = 'INSERT INTO course_data2(courseId, courseName, courseImg, gradeId, gradeName, subjectId, subjectName, time, aims, instructions) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                        cursor_temp.execute(sql, (course_id, courseName,img,tag1,gradeName,tag2,subjectName," "," "," "))
                        db_temp.commit()
                        print(gradeName,subjectName,courseName)


if __name__ == '__main__':
    work()

