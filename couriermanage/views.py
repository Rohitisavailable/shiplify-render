from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Courier

def home(request):
	return render(request, 'couriermanage/home.html', {'title': 'home'})

@login_required
def main(request):
	couriers = Courier.objects.all().order_by('-id')
	query = request.GET.get('q')
	if query:
		couriers = Courier.objects.filter(package_no__icontains=query).order_by('-id')
	paginator = Paginator(couriers, 10)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'couriermanage/main.html', {'page_obj': page_obj, 'query': query or ''})

def about(request):
	return render(request, 'couriermanage/about.html', {'title': 'About'})

def upcoming(request):
	return render(request, 'couriermanage/upcoming.html', {'title': 'Coming soon'})