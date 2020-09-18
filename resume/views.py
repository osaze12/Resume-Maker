from django.shortcuts import render

from resume.form import *
from resume.models import *
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
import requests
import pdfkit

# Create your views here.
def generate_pdf(request, pk):
	try:
		#Path to the windows installed program
		path_wkthmltopdf = b'C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe'
		config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
		output_path = False

		get_url_data= pdfkit.from_url('http://localhost:8000/done/{}/True/'.format(pk), output_path, configuration=config)
		response = HttpResponse(get_url_data, content_type="application/pdf")
		#Download directly without viewing pdf
		# response['Content-Disposition'] = 'attachment'; filename='Resume.pdf'
		return response
	except:
		return HttpResponse("<p style='text-align:center;font-weight:bold;color:#4c4949;padding:20px;'>This software uses wkhtmltopdf installed on windows to generate pdf format,<br/>There may be something wrong with the path to the wkhtmltopdf software. </p>")

def create(request):
	context = {
		'form1': InfoForm,
		'form2': EducationForm,
		'form3': SkillForm,
		'form4': CertificateForm,
		'form5': HobbieForm,
		'form6': ExperienceForm,
	}
	return render(request, 'resume/form1.html', context)

def form1(request):
	if request.method == 'POST':
		form = InfoForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			date_of_birth = form.cleaned_data['date_of_birth']
			phone_number = form.cleaned_data['phone_number']
			address = form.cleaned_data['address']
			location = form.cleaned_data['location']
			projects_link = form.cleaned_data['projects_link']
			resume_summary = form.cleaned_data['resume_summary']
			professional_title = form.cleaned_data['professional_title']


			info = Info.objects.create(first_name =first_name, last_name=last_name,
				email=email, date_of_birth=date_of_birth, phone_number=phone_number,
				address=address, location=location, projects_link=projects_link,
				resume_summary=resume_summary, professional_title=professional_title)
			info.save()
			return JsonResponse({'id': info.id }, status=200)
	
def form2(request):
	if request.method == 'POST':
		form = EducationForm(request.POST)
		if form.is_valid():
			school_name = form.cleaned_data['school_name']
			degree = form.cleaned_data['degree']
			studied = form.cleaned_data['studied']
			pk = request.POST['id']
			user_object_exist = Info.objects.filter(id=pk).exists()
			if user_object_exist == True:
				get_user_instance = Info.objects.get(id=pk)
				edu = Education.objects.create(
										user=get_user_instance,
									    school_name=school_name,
									    studied=studied,
									    degree=degree)

				edu.save()
				return JsonResponse({'success': ' form2 successful'}, status=200)
			else:
				return JsonResponse({'error': 'The username does not exist'} ,status=404)

def form3(request):
	if request.method == 'POST':
		form = SkillForm(request.POST)
		if form.is_valid():
			percentage = form.cleaned_data['percentage']
			name = form.cleaned_data['name']
			pk = request.POST['id']
			get_user_instance = Info.objects.get(id=pk)
			skill = Skill.objects.create(
								user=get_user_instance,
								percentage=percentage,
							    name=name)
			skill.save()
			return JsonResponse({'success': ' form3 successful'}, status=200)
		else:
			return JsonResponse({'error': 'form not valid'}, status=404)

def form4(request):
	if request.method == 'POST':
		form = CertificateForm(request.POST)
		if form.is_valid():
			school = form.cleaned_data['school']
			year = form.cleaned_data['year']
			pk = request.POST['id']

			get_user_instance = Info.objects.get(id=pk)
			cert = Certificate.objects.create(
										user=get_user_instance,
										school=school,
									    year=year)
			cert.save()
			return JsonResponse({'success': ' form4 successful'}, status=200)
		else:
			return JsonResponse({'error': 'form not valid'}, status=404)

def form5(request):
	if request.method == 'POST':
		form = HobbieForm(request.POST)
		if form.is_valid():
			interest = form.cleaned_data['interest']
			pk = request.POST['id']

			get_user_instance = Info.objects.get(id=pk)
				
			hobb = Hobbie.objects.create(
									user=get_user_instance,
									interest=interest)
			hobb.save()
			return JsonResponse({'success': ' form5 successful'}, status=200)
		else:
			return JsonResponse({'error': 'form not valid'}, status=404)

def form6(request):
	if request.method == 'POST':
		form = ExperienceForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			description = form.cleaned_data['description']
			pk = request.POST['id']

			get_user_instance = Info.objects.get(id=pk)
				
			expe = Experience.objects.create(
										user=get_user_instance,
										title=title,
										description=description)
			expe.save()
			return JsonResponse({'success': ' form6 successful'}, status=200)
		else:
			return JsonResponse({'error': 'form not valid'}, status=404)

# the clear parameter determine whether to remove the pdf button from the screen or not
def done(request, pk, clear):
	if request.method == "POST":
		user_info_exists = Info.objects.filter(id=pk).exists()
		if user_info_exists == True:
			return JsonResponse({'success': 'Everything has gone well.'}, status=200)
		else:
			return JsonResponse({'error':'the id does not exist'}, status=404)
	else:

		try:
			get_user_object = Info.objects.get(id=pk)
		except:
			return HttpResponse("Resume does not exist, please create one.")
	
		get_education_object = Education.objects.filter(user=get_user_object).exists()
		if get_education_object == True:
			education_data = Education.objects.filter(user=get_user_object)
		else:
			education_data = False

		get_skill_object = Skill.objects.filter(user=get_user_object).exists()
		if get_skill_object == True:
			skill_data = Skill.objects.filter(user=get_user_object)
		else:
			skill_data = False

		get_certificate_object = Certificate.objects.filter(user=get_user_object).exists()
		if get_certificate_object == True:
			certificate_data = Certificate.objects.filter(user=get_user_object)
		else:
			certificate_data = False

		get_hobbie_object = Hobbie.objects.filter(user=get_user_object).exists()
		if get_hobbie_object == True:
			hobbie_data = Hobbie.objects.filter(user=get_user_object)
		else:
			hobbie_data = False

		get_experience_object = Experience.objects.filter(user=get_user_object).exists()
		if get_experience_object == True:
			experience_data = Experience.objects.filter(user=get_user_object)
		else:
			experience_data = False

		#GENERATE BAR CHART
		if skill_data != False:
			#import libraries for ploting the chart
			import matplotlib; matplotlib.use('Agg')
			import matplotlib.pyplot as plt 
			from io import BytesIO
			import base64, urllib

			plt.rcdefaults()
			fig, ax = plt.subplots()

			#skill database data
			skill_level_data = [x.percentage for x in skill_data]
			skill_name_data = [x.name for x in skill_data] 

			#creates the bar chart
			ax.barh(skill_name_data, skill_level_data, align='center', color='#18d6b3')
			ax.set_yticks(skill_name_data)
			ax.invert_yaxis()

			#remove all frame lines
			ax.spines['top'].set_visible(False)
			ax.spines['right'].set_visible(False)
			ax.spines['bottom'].set_visible(False)
			ax.spines['left'].set_visible(False)


			imagedata = BytesIO()
			plt.savefig(imagedata, format='png')
			
			imagedata.seek(0)
			string = base64.b64encode(imagedata.read())
			plot_data = 'data:image/png;base64,'+ urllib.parse.quote(string)
			
		else:
			plot_data = False

		context = {
			'info': get_user_object,
			'edus': education_data,
			'certs': certificate_data,
			'hobs': hobbie_data,
			'exps': experience_data,
			'plot': plot_data
		}
		response = render(request, 'resume/resume.html', context)

		if clear == "True":
			response.set_cookie("clear", "True")
		else:
			response.set_cookie("clear", "False")

		return response

# deletes resume by the id
def delete(request, pk):
	user_exists = Info.objects.filter(id=pk).exists()
	if user_exists != True:
		return JsonResponse({'error':'Id does not exist'}, status=404)

	get_user = Info.objects.get(id=pk)
	get_user.delete()
	return JsonResponse({'success':'successfully deleted'}, status=200)


