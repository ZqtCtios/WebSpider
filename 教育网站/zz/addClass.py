import pymysql
import json
db = pymysql.connect(
    "localhost",
    "root",
    "zqt1997",
    "data",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()
with open('class.json', 'r') as f:
    data = json.loads(f.read())
for line in data['rtnArray']:
    bookOptionCode = line['bookOptionCode']
    bookOptionName = line['bookOptionName']
    courseVersionId = line['courseVersionId']
    grade = line['grade']
    studyStage = line['studyStage']
    subject = line['subject']
    term = line['term']
    version = line['version']
    versionCode = line['versionCode']
    if len(grade) == 0:
        name = '{}.{}.{}.{}'.format(
            studyStage, subject, version, bookOptionName)
    else:
        name = '{}.{}.{}.{}'.format(grade, term, subject, version)
    print(name)
    sql = 'insert into vc_version(vc_version_id,vc_version_name,vc_code,vc_xiu_code) values(%s,%s,%s,%s)'
    cursor.execute(sql, (courseVersionId, name, versionCode, bookOptionCode))
    db.commit()
