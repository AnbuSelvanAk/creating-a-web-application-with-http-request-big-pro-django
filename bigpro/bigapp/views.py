from django.shortcuts import render
from django.http import HttpResponse
def testing(request):
	a=5
	b=10
	if a>b:
		s="A is big"
	else:
		s="B is big"
	x='<h1><font color="red">A Is...'+str(a)+'B is...'+str(b)+''+str(s)+'</font></h1>'
	return HttpResponse(x)

