from django.urls import path
from .views import *	 #HomePage, AboutPage, ContactUs #ดึงฟังชั่น HomePage มาทำงาน

urlpatterns = [
	# localhost:8000/
	path('',HomePage,name='home-page'),
	path('about/',AboutPage,name='about-page'),
	path('contactus/',ContactUs,name='contactus-page')
	path('score/',ShowScore,name='score-page')
]
