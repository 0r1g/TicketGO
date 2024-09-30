from django.shortcuts import render, redirect, get_object_or_404
from .models import Bus, CompanyName, Booking
from .forms import BookingForm


# Create your views here.


def home(request):
    return render(request, 'api/home.html', {'title': 'Home'})


def show_companies(request):
    return render(request, 'api/companies.html', {'companies': CompanyName.objects.all(), 'title': 'Companies'})


def show_company_details(request, company_id):
    company = CompanyName.objects.get(id=company_id)
    return render(request, 'api/about_company.html', {'company': company, 'title': company.name})


def show_buses(request):
    return render(request, 'api/buses.html', {'buses': Bus.objects.all(), 'title': 'Buses'})


def show_bus(request, bus_id):
    return render(request, 'api/about_bus.html', {'bus': Bus.objects.get(id=bus_id), 'title': 'Bus'})


def booking_form(request, bus_id):
    bus = get_object_or_404(Bus, id=bus_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.bus = bus

            booking.save()
            return redirect('success', booking_id=booking.id)
    else:
        form = BookingForm()

    context = {
        'form': form,
        'bus': bus,
    }
    return render(request, 'api/booking_form.html', context)


def view_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    context = {
        'booking': booking,
    }

    return render(request, 'api/view_booking.html', context)


def success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    return render(request, 'api/success.html', {'booking': booking})
