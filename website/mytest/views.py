from django.shortcuts import render
import json
from django.http import HttpResponse
from .models import Cities


def showHtml(request):
    return render(request, 'webHtml/showUpload.html')


def getAllCity(request):
    ret = {
        "status": False,
        "message": ""
    }
    try:
        ret["status"] = True
        ret["message"] = [
            (city.id, city.ch_name, city.en_name)
            for city in Cities.objects.all().iterator()
        ]
    except Exception:
        ret["message"] = "數據查詢有誤，請確認！"
    return HttpResponse(json.dumps(ret))


# 添加一筆數據
def addCity(request):
    ret = {
        "status": False,
        "message": ""
    }
    try:
        res = request.POST.get("data1")
        result = json.loads(res)
        Cities.objects.create(ch_name=result[0], en_name=result[1])
        ret["status"] = True
        ret["message"] = "添加成功！"
    except Exception:
        ret["message"] = "添加失敗！"
    return HttpResponse(json.dumps(ret))


#刪除數據
def deleteCity(request):
    ret = {"status": False, "message": ""}
    res = request.POST.get("idList")
    result = json.loads(res)
    try:
        for city in result:
            Cities.objects.filter(id=int(city)).delete()
        ret["status"] = True
        ret["message"] = "刪除成功！"
    except Exception:
        ret["message"] = "刪除失敗！"
    return HttpResponse(json.dumps(ret))
#
# #修改一條數據
# def updateOneData(request):
#     ret = {"status":False,"message":""}
#     id = request.POST.get("citrixID")
#     userid = request.POST.get("value")
#     try:
#         if web_impl.updateOne(userid,id):
#             ret["status"] = True
#             return HttpResponse(json.dumps(ret))
#         else:
#             ret["message"] = "修改失敗！"
#             return HttpResponse(json.dumps(ret))
#     except Exception as e:
#         print(e)
#         ret["message"] = "運行過程中出現錯誤！"
#         return HttpResponse(json.dumps(ret))
#
