from django.shortcuts import render
from django.http import HttpResponseRedirect
from app.models import studentreg,SignUp,AdminNotice
def MyLogin(request):
	if request.method=='POST':
		em=request.POST['email']
		pass1=request.POST['pass']
		s1=SignUp.objects.filter(email=em,pass1=pass1).exists()
		if(s1==True):
			if em=='admin@gmail.com':
				return HttpResponseRedirect('/admindash')
			else:
				return HttpResponseRedirect('/userdash')
		else:
			return HttpResponseRedirect('/login')
	return render(request,'login.html')

def MySignUp(request):
	if request.method=='POST':
		nm=request.POST['name']
		mob=request.POST['mob']
		em=request.POST['email']
		pass1=request.POST['pass']
		s1=SignUp(name=nm,mobile=mob,email=em,pass1=pass1)
		s1.save()
		return HttpResponseRedirect('/login')
	return render(request,'signup.html')

def MyAdmin(request):
	return render(request,'admindash.html')

def MyUser(request):
	return render(request,'userdash.html')

def StudReg(request):
	if request.method=='POST':
		fname=request.POST['fname']
		lname=request.POST['lname']
		dob=request.POST['dob']
		gen=request.POST['gen']
		email=request.POST['email']
		mob=request.POST['mob']
		city=request.POST['city']
		print(fname,lname,dob,gen,email,mob,city)
		s1=studentreg(firstname=fname,lastname=lname,birthdate=dob,gender=gen,email=email,mobile=mob,city=city)
		s1.save()
		return HttpResponseRedirect('/userdash')
	return render(request,'studreg.html')

def UserStudView(request):
	s1=studentreg.objects.all()
	dict1={
			'data':s1
	}
	return render(request,'userstudview.html',dict1)

def AdminStudView(request):
	s1=studentreg.objects.all()
	dict1={
			'data':s1
	}
	return render(request,'adminstudview.html',dict1)

def AdminNotice1(request):
	if request.method == 'POST':
		dt1=request.POST['dt']
		sub=request.POST['sub']
		print(dt1,sub)
		s11=AdminNotice(ndate1=dt1,subject=sub)
		s11.save()
		return HttpResponseRedirect('/admindash')
	return render(request,'adminnotice.html')

def AdminNoticeView(request):
	s1=AdminNotice.objects.all()
	dict1={
	'data':s1
	}
	return render(request,'adminnoticeview.html',dict1)

def UserNoticeView(request):
	s1=AdminNotice.objects.all()
	dict1={
	'data':s1
	}
	return render(request,'usernoticeview.html',dict1)

def NoticeRemove(request):
	id=request.GET['id']
	s1=AdminNotice.objects.get(id=id)
	s1.delete()
	return HttpResponseRedirect('/admindash')

def NoticeUpdate(request):
	if request.method == 'GET':
		id1=request.GET['id']
		ndate1=str(request.GET['ndate1'])
		subject=request.GET['subject']
		
		dict1={
				'id1':id1,
				'dt1':ndate1,
				'sub':subject
		}
		return render(request,'noticeupdate.html',dict1)
	elif request.method == 'POST':
		id1=request.POST['id']
		dt1=request.POST['dt']
		sub=request.POST['sub']
		s11=AdminNotice.objects.get(id=id1)
		s11.ndate1=dt1 
		s11.subject=sub
		s11.save()
		return HttpResponseRedirect('/admindash')

def UserStudRemove(request):
	id=request.GET['id']
	s1=studentreg.objects.get(id=id)
	s1.delete()
	return HttpResponseRedirect('/userdash')

def StudUpdate(request):
	if request.method == 'GET':
		id=request.GET['id']
		s1=studentreg.objects.get(id=id)
		dict1={
			'data':s1
		}
		return render(request,'studupdate.html',dict1)

	elif request.method == 'POST':
		fname=request.POST['fname']
		lname=request.POST['lname']
		dob=request.POST['dob']
		gen=request.POST['gen']
		email=request.POST['email']
		mob=request.POST['mob']
		city=request.POST['city']
		s1=studentreg.objects.get(firstname=fname)
		s1.lastname=lname
		s1.birthdate=dob
		s1.gender=gen
		s1.email=email
		s1.mobile=mob
		s1.city=city
		s1.save()
		return HttpResponseRedirect('/userdash')
