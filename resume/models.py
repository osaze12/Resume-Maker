from django.db import models

# Create your models here.
class Info(models.Model):

	first_name = models.CharField(max_length=14)
	last_name = models.CharField(max_length=14)
	email = models.EmailField()
	date_of_birth = models.DateField()
	phone_number = models.CharField(max_length=14)
	address = models.CharField(max_length=250)
	location = models.CharField(max_length=20)
	projects_link = models.URLField(max_length=300, null=True, blank=True)
	resume_summary = models.TextField(max_length=400)
	professional_title = models.CharField(max_length=50)


class Education(models.Model):

	DEGREES = [
		('bsc', 'BSC'),
		('hnd', 'HND'),
		('nd', 'ND'),
		('msc', 'MSC')
	]
	user = models.ForeignKey(Info, on_delete=models.CASCADE)
	school_name = models.CharField(max_length=100)
	degree = models.CharField(
				max_length=3,
				choices=DEGREES,
				default='bsc',
			 )
	studied = models.CharField(max_length=150)

class Experience(models.Model):

	title = models.CharField(max_length=80)
	description = models.TextField(max_length=400)
	user = models.ForeignKey(Info, on_delete=models.CASCADE)

class Skill(models.Model):

	SKILL_LEVEL = [
	(1, 'LEVEL 1'),
	(2, 'LEVEL 2'),
	(3, 'LEVEL 3'),
	(4, 'LEVEL 4'),
	(5, 'LEVEL 5')
	]
	percentage = models.IntegerField(
		choices= SKILL_LEVEL,
		default= '1',
	)
	name = models.CharField(max_length=10)
	user = models.ForeignKey(Info, on_delete=models.CASCADE)

class Certificate(models.Model):

	user = models.ForeignKey(Info, on_delete=models.CASCADE)
	school = models.CharField(max_length=100)
	year = models.IntegerField()


class Hobbie(models.Model):

	user = models.ForeignKey(Info, on_delete=models.CASCADE)
	interest = models.CharField(max_length=150, blank=True)