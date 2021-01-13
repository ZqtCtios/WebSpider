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

requestData = [19]
nameData = [100,101,102,103,104,112]
nameData2 = ['国内英语','留学英语','实用英语','小语种','职称英语']
pageData = [7, 47, 105, 2, 5, 10, 25]


def getJson(grade,page):
    url = 'http://www.class.cn/ajax/course/list_course'
    data = {
        'type_id': grade,
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
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "edu123456",
        "work2",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    for grade in requestData:
        gradeName=''
        tag2=0
        for i in range(len(nameData)):
            tag1=nameData[i]
            subjectName=nameData2[i]
            for page in range(1,30):       
                html = getJson(tag1,grade,page)
                print(tag1,subjectName,page)
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

def ww():
    
    for page in range(23,26):
        html =getJson(19,page)
        js = json.loads(html)['data']
        try:
            courses = js['course']
        except :
            continue  
        for course in courses:
            course_id = course['course_id']
            img = course['img_name']
            img='http://v2.data.class.cn/'+img
            path='/home/newdata/courseImg3/{}.jpg'.format(course_id)
            content=requests.get(img).content
            f=open(path,'wb+')
            f.write(content)
            f.close()
            print(path)


def work():
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "edu123456",
        "work2",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    for grade in requestData:
        for i in range(len(nameData)):
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
    ww()

