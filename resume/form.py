from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

from resume.models import Info, Education, Experience, Skill, Certificate, Hobbie



	

class InfoForm(forms.ModelForm):
	first_name = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'placeholder': 'Your Personal name'}))
	last_name = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'placeholder': 'Your Father\'s name'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': ' Email Address..'}))

	date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Year-Month-Day'}))
	phone_number = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'placeholder': '+234 *** *** ****'}))
	address = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'Your House Address...'}))
	location = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Example: Lagos, Ikeja'}))
	# projects_link = forms.URLField(max_length=300, widget=forms.TextInput(attrs={'placeholder': 'github.com/osaze12'}))


	class Meta:
		model = Info
		fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'phone_number',
		'address', 'location', 'projects_link', 'resume_summary', 'professional_title'
		]
		widgets = {
			'projects_link': forms.TextInput(attrs={'placeholder': 'github.com/osaze12'})
		}
		
class EducationForm(forms.ModelForm):
	class Meta:
		model = Education
		fields = ['school_name', 'degree', 'studied']
		widgets = {
			'studied': forms.TextInput(attrs={'placeholder': 'Computer Science'})
		}
		

class ExperienceForm(forms.ModelForm):
	class Meta:
		model = Experience
		fields = ['title', 'description']

class SkillForm(forms.ModelForm):
	class Meta:
		model = Skill
		fields = ['percentage', 'name']


class CertificateForm(forms.ModelForm):
	class Meta:
		model = Certificate
		fields = ['school', 'year']
		widgets = {
			'year': forms.TextInput(attrs={'placeholder': '1999'})
		}


class HobbieForm(forms.ModelForm):
	class Meta:
		model = Hobbie
		fields = ['interest']
		widgets = {
			'interest': forms.TextInput(attrs={'placeholder': 'What You Love Doing..'})
		}