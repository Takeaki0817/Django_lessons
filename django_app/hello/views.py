from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     if 'msg' in request.GET:
#         msg = request.GET['msg']
#         result = 'you type: "' + msg +'".'
#     else:
#         result = 'please send msg parameter!'
#     return HttpResponse(result)

# def index(request, id, nickname):
#     result = 'your id: ' + str(id) + ', name: "' + nickname + '".'
#     return HttpResponse(result) 

def index(request):
    params = {
        'title':'hello/Index',
        'msg':'これは、サンプルで作ったページです。',
        'goto':'next',
    }
    return render(request, 'hello/index.html', params)

def next(request):
    params = {
        'title':'Hello/Next',
        'msg':'これは、もう1つのページです。',
        'goto':'index',
    }
    return render(request, 'hello/index.html', params)