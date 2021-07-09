from django.shortcuts import reverse
from django.views.generic import View
from django.http import HttpResponseRedirect


class Index(View):
	"""
	Root/homepage view
	"""
	def get(self, request):
		"""
		Get method.
		Redirect ke polls sebagai root/homepage
		"""
		return HttpResponseRedirect(
			reverse('polls:index_polls')
		)

	def post(self, request):
		"""
		Post method.
		Redirect ke polls sebagai root/homepage.
		"""
		return HttpResponseRedirect(
			reverse('polls:index_polls')
	)
