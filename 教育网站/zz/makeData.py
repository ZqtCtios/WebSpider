import xlrd
import pymysql


def update():
    db = pymysql.connect(
        "localhost",
        "root",
        "zqt1997",
        "data",
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    workbook = xlrd.open_workbook('data.xls', formatting_info=True)
    booksheet = workbook.sheet_by_index(0)
    for index in range(23, 36):
        name = booksheet.cell_value(index, 1)
        nameList = name.split('.')
        print(nameList)
        name = '{}.{}.{}.{}'.format(
            nameList[1], nameList[2], nameList[0], nameList[3])
        print(name)
        sql = 'SELECT id,vc_code,vc_xiu_code FROM vc_version WHERE `vc_version_name` LIKE \'{}\''.format(
            name)

        cursor.execute(sql)
        res = cursor.fetchall()[0]
        versionId = res[0]
        version = res[1]
        termId = ""
        term = res[2]
        sql = 'select id,vc_subjectid from subject where `vc_subjectName` like \'{}\''.format(
            nameList[2])
        cursor.execute(sql)
        res = cursor.fetchall()[0]
        subjectId = res[0]
        subject = res[1]
        sql = 'select id,vc_gradeid,vc_section from grade where `vc_gradeName` like \'{}\''.format(
            nameList[1])
        cursor.execute(sql)
        res = cursor.fetchall()[0]
        gradeId = res[0]
        grade = res[1]
        section = res[2]

        sql = 'insert into data values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0)'
        cursor.execute(
            sql,
            (index,
             name,
             section,
             grade,
             gradeId,
             term,
             termId,
             subject,
             subjectId,
             version,
             versionId))
        db.commit()
        print(index)


    # excel.save('data.xls')
if __name__ == "__main__":
    update()
