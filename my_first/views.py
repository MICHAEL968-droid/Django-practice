from django.http import HttpResponse 
from django.shortcuts import render 

def index(request):
  params = {'name':'harry','place':'Mars'}
  return render(request,'index.html',params)

def about(request):
  #return HttpResponse('this is about page')
  return render(request, 'about.html')

def fb(request):
  return HttpResponse('''<a href = "https://www.amazon.in/">amazon</a>''')

def removepunc(request):
  print(request.GET.get('text','default'))
  return HttpResponse('remove puncutation')


def capfirst(request):
  return HttpResponse('''<a href = "https://www.amazon.in/">amazon</a>''')

def spaceremove(request):
  return HttpResponse('''<a href = "https://www.amazon.in/">amazon</a>''')

def newlineremove(request):
  return HttpResponse('''<a href = "https://www.amazon.in/">amazon</a>''')


def charcount(request):
  return HttpResponse('''<a href = "https://www.amazon.in/">amazon</a>''')
