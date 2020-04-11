from django.shortcuts import render
from django.http import HttpResponse #HttpResponse เปรียบเสทือนเขียนบนกระดาน
from .models import Exam_Score
def HomePage(request):
	# return HttpResponse('<h1>Hello World!!<h1/>')
	return render(request, 'school/home.html')

def AboutPage(request):
		return render(request,'school/about.html ')

def ContactUs(request):
		return render(request,'school/contactus.html ')
def ShowScore(request):
		score = Exam_Score.objects.all()
		context = {'score':score}
		return render(request,'school/showscore.html ',context)
