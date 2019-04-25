from django.shortcuts import render
import json
from django.http import HttpResponse
from dataprocess.webHtml import web_impl

# 展示頁面
def showHtml(request):
    return render(request, 'webHtml/showUpload.html')

# ajax異步傳遞數據
def getAllData(request):
    ret = {"status":False,"message":""}
    try:
        result = web_impl.getData()
        if result:
            ret["status"] = True
            ret["message"] = result
        else:
            ret["message"] = "數據查詢有誤，請確認！"
        return HttpResponse(json.dumps(ret))
    except Exception as e:
        print(e)
        ret["message"] = "數據查詢有誤，請確認！"
        return HttpResponse(json.dumps(ret))

# 添加一筆數據
def addOneData(request):
    ret = {"status":False,"message":""}
    res = request.POST.get("data1")
    result = json.loads(res)
    listA = []
    listA.append(result)
    try:
        if web_impl.addOneData(listA):
            ret["status"] = True
            ret["message"] = "添加成功！"
            return HttpResponse(json.dumps(ret))
        else:
            ret["message"] = "添加失敗！"
            return HttpResponse(json.dumps(ret))
    except Exception as e:
        print(e)
        ret["message"] = "添加失敗！"
        return HttpResponse(json.dumps(ret))

#修改一條數據
def updateOneData(request):
    ret = {"status":False,"message":""}
    id = request.POST.get("citrixID")
    userid = request.POST.get("value")
    try:
        if web_impl.updateOne(userid,id):
            ret["status"] = True
            return HttpResponse(json.dumps(ret))
        else:
            ret["message"] = "修改失敗！"
            return HttpResponse(json.dumps(ret))
    except Exception as e:
        print(e)
        ret["message"] = "運行過程中出現錯誤！"
        return HttpResponse(json.dumps(ret))

#刪除數據
def deleteData(request):
    ret = {"status":False,"message":""}
    res = request.POST.get("idList")
    result = json.loads(res)
    listB = []
    for i in result:
        listA = []
        listA.append(i)
        listB.append(listA)
    try:
        if web_impl.deleteDataList(listB):
            ret["status"] = True
            ret["message"] = "刪除成功！"
            return HttpResponse(json.dumps(ret))
        else:
            ret["message"] = "刪除失敗！"
            return HttpResponse(json.dumps(ret))
    except Exception as e:
        print(e)
        ret["message"] = "運行過程中出現錯誤！"
        return HttpResponse(json.dumps(ret))
