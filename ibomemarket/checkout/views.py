from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def checkout(request):
	template = 'checkout.html'
	return render(request, template,)



