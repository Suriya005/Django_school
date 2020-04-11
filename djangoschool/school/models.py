from django.db import models

class Exam_Score(models.Model):

	allsubject = (('math','คณิตศาสตร์'),
					('sci','วิทยาศาสตร์'),
					('art','ศิลปะ'),
					('eng','อังกฤษ'))

	subject = models.CharField(max_length=200, choices=allsubject, default='math')
	stdname = models.CharField(max_length=200)
	score = models.IntegerField(default=0)

