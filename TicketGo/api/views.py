from django.shortcuts import render, redirect
from .models import Category, Transport, Booking
from .forms import BookingForm


# Create your views here.


def home(request):
    return render(request, 'api/home.html')


def show_category(request):
    categories = Category.objects.all()
    return render(request, 'api/categories.html', {'categories': categories})


def show_transport(request, category_id):
    return render(request, 'api/transports.html', {'category_id': category_id, 'transports': Transport.objects.filter(category_id=category_id)})


def show_all_transport(request):
    return render(request, 'api/transports.html', {'transports': Transport.objects.all()})


def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = BookingForm()

    return render(request, 'api/booking_form.html', {'form': form})


def success(request):
    return render(request, 'api/success.html')
