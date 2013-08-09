# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Drawing


def index(request):
	try:
		drawing = Drawing.objects.latest('created_on')
	except Drawing.DoesNotExist:
		raise Exception
	try:
		next_drawing = Drawing.objects.filter(created_on__gt=drawing.created_on).order_by('created_on')[0]
	except IndexError:
		next_drawing = None
	try:
		previous_drawing = Drawing.objects.filter(created_on__lt=drawing.created_on).latest('created_on')
	except Drawing.DoesNotExist:
		previous_drawing = None
	var_dict = {
		'drawing': drawing,
		'next_drawing': next_drawing,
		'previous_drawing': previous_drawing,
	}
	return render(request, 'index.html', var_dict)


def show_drawing(request, drawing_id):
	drawing = get_object_or_404(Drawing, id=drawing_id)
	try:
		next_drawing = Drawing.objects.filter(created_on__gt=drawing.created_on).order_by('created_on')[0]
	except IndexError:
		next_drawing = None
	try:
		previous_drawing = Drawing.objects.filter(created_on__lt=drawing.created_on).latest('created_on')
	except Drawing.DoesNotExist:
		previous_drawing = None
	var_dict = {
		'drawing': drawing,
		'next_drawing': next_drawing,
		'previous_drawing': previous_drawing,
	}
	return render(request, 'index.html', var_dict)


def about(request):
	return render(request, 'about.html', {})