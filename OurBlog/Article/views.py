from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
def test(request):
    return HttpResponse('你好')

def framework_page(request):
    return render_to_response('framework_page.html')