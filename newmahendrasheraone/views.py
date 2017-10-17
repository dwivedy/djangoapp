from django.http import HttpResponse

def home(request):
    return HttpResponse("<h2>hello notepad newmahendrasheraone</h2>")
    
def testSimple(request):
    return HttpResponse(request.GET.get("hello",'')+"<h2>hello notepad test</h2>")
    
def testSimpleUrlpath(request,testno):
    return HttpResponse(str(testno)+"<h2>hello notepad test</h2>")
	
		
    
