from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.serializers import SnippetSerializer
from api.models import avmoo_api
from api.models import teacher


# Create your views here.




class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



def api_index(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        snippets = avmoo_api.objects.all()

        limit = 20
        p = Paginator(snippets,limit)
        try:
            db =  p.page(page)
            api = SnippetSerializer(db,many=True)
        except PageNotAnInteger:
            db = p.page(1)
            api = SnippetSerializer(db,many=True)
        except EmptyPage:
            db = p.page(p.num_pages);
            api = SnippetSerializer(db,many=True)

        return JSONResponse(api.data,charset='utf-8')
    elif request == 'POST':
        data = JSONParser().parse(request)
        api = SnippetSerializer(data=data)
        if api.is_valid():
            api.save()
            return  JSONResponse(api.data,status=201,charset='utf-8')
        return JSONResponse(api.errors,status=100)
def api_detail(request,pk):
    try:
        snippet = avmoo_api.objects.get(pk = pk)
    except avmoo_api.DoesNotExist:
        return  HttpResponse(status=404)

    if request.method == 'GET':
        api =  SnippetSerializer(snippet)
        return  JSONResponse(api.data,charset='utf-8')
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        api = SnippetSerializer(snippet,data=data)
        if api.is_valid():
            api.save()
            return JSONResponse(api.data,charset='utf-8')
        return  JSONResponse(api.errors,status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return  HttpResponse(status=204)

def  teacher(request):
    if request.method == 'GET':
        snippets = teacher.objects.all()
        page = request.GET.get('page')
        limit = 20
        p = Paginator(snippets,limit)
        try:
            db =  p.page(page)
            api = SnippetSerializer(db,many=True)
        except PageNotAnInteger:
            db = p.page(1)
            api = SnippetSerializer(db,many=True)
        except EmptyPage:
            db = p.page(p.num_pages);
            api = SnippetSerializer(db,many=True)

        return JSONResponse(api.data,charset='utf-8')
    elif request == 'POST':
        data = JSONParser().parse(request)
        api = SnippetSerializer(data=data)
        if api.is_valid():
            api.save()
            return  JSONResponse(api.data,status=201,charset='utf-8')
        return JSONResponse(api.errors,status=100)


def search(request):
	kw = request.GET.get['kw']
	snippets = avmoo_api.objects.filter(Q(fanhao=kw)|Q(artists=kw)|Q(leibie=kw))

	page = request.GET.get('page')

	limit = 20
	p = Paginator(objects,limit)
	try:
		db =  p.page(page)
		api = SnippetSerializer(db,many=True)
	except PageNotAnInteger:
		db = p.page(1)
		api = SnippetSerializer(db,many=True)
	except EmptyPage:
		db = p.page(p.num_pages);
		api = SnippetSerializer(db,many=True)

	return JSONResponse(api.data,charset='utf-8')