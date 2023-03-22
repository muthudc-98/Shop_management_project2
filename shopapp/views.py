from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from shopapp.models import Shopview

from shopapp.forms import Shopform
from shopapp.forms import Signupform
import csv
from django.http import HttpResponse
from django.views.decorators.cache import cache_control

def home(request):
	return render(request,'apps/home.html')

def signupfun(request):
	form=Signupform()
	if request.method== 'POST':
		form=Signupform(request.POST)
		user=form.save()
		user.set_password(user.password)
		user.save()
		return HttpResponseRedirect('/accounts/login')

	return render(request,'apps/signup.html',{'form':form})

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def productpage1(request):
	shop=Shopview.objects.all().order_by('name')
	return render(request,'apps/product_page.html',{'sh':shop})

@login_required
def lastpage(request):
	return render(request,'apps/lastpage.html')

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def form(request):
	shop=Shopform()
	if request.method=='POST':
		shop=Shopform(request.POST)
		if shop.is_valid():
			shop.save()
			return redirect('/productpage')

	return render(request,'apps/forms.html',{'fo':shop})

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete(request,id):
	shop=Shopview.objects.get(id=id)
	shop.delete()
	return redirect('/productpage')

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update(request,id):
	form=Shopview.objects.get(id=id)
	if request.method=='POST':
		shop=Shopform(request.POST, instance=form)
		if shop.is_valid():
			shop.save()

		return redirect('/productpage')
	return render(request,'apps/update.html',{'s':form})

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def download(request):
	get=HttpResponse(content_type='text/csv')
	get['content-disposition']='attachment;filename=details.csv'
	col=Shopview.objects.all()
	get2=csv.writer(get)
	get2.writerow(['Name','Quantity','Price'])
	for i in col:
		get2.writerow([i.name,i.quantity,i.price])

	return get 

def logout(request):
	
	return redirect('/home')




