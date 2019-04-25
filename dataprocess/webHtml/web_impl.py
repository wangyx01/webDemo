from django.db import connection

#得到數據
def getData():
    cursor = connection.cursor()
    sql = "SELECT ID,USERNAME,USERID,USERMING,USERXING,TEMP,CREATTIME,WORKER FROM TESTEXCLE"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result

# 添加一組數據
def addOneData(list):
    cursor = connection.cursor()
    sql = "INSERT INTO TESTEXCLE(USERNAME,USERID,USERMING,USERXING,TEMP,CREATTIME,WORKER) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    cursor.executemany(sql,list)
    cursor.close()
    if cursor.rowcount:
        return True
    return False

# 修改工號
def updateOne(userid,id):
    cursor = connection.cursor()
    sql = "UPDATE TESTEXCLE SET USERID =%s WHERE ID = %s"
    cursor.execute(sql,[userid,id])
    cursor.close()
    if cursor.rowcount:
        return True
    return False

# 刪除操作
def deleteDataList(isList):
    cursor = connection.cursor()
    sql = "DELETE FROM TESTEXCLE WHERE ID = %s"
    cursor.executemany(sql,isList)
    cursor.close()
    if cursor.rowcount:
        return True
    return False
