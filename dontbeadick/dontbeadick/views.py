from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Drawing

def index(request):
	dr = {
		'title': 'This is the name',
	}

	var_dict = {
		'drawing': dr,
	}

	return render(request, 'index.html', var_dict)


def show_drawing(request, drawing_id):
	# get_object_or_404(Drawing, id=drawing_id)

	dr = {
		'title': 'This is the name',
	}

	var_dict = {
		'drawing': dr,
	}
	
	return render(request, 'index.html', var_dict)



def about(request):
	return render(request, 'about.html', {})