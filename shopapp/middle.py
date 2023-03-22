from django.http import HttpResponse

class Middlefun(object):
	def __init__(self,get_response):
		self.get_response=get_response
	def __call__(self,request):
		response=self.get_response(request)
		return response
	def process_exception(self,request,exception):
		s='<h1>Currently unavailable. Please try again later...</h1>'
		return HttpResponse(s)