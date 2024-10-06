from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Bus, Company, Booking, ProfilePhoto
from .forms import BookingForm, SearchBusesForm, ProfilePhotoForm


def home(request):
    return render(request, 'api/home.html', {'title': 'Home'})


def show_companies(request):
    return render(request, 'api/companies.html', {'companies': Company.objects.all(), 'title': 'Companies'})


def show_company_details(request, company_id):
    company = Company.objects.get(id=company_id)
    return render(request, 'api/about_company.html', {'company': company, 'title': company.name})


def show_buses(request):
    buses = Bus.objects.all().order_by('id')

    form = SearchBusesForm(request.GET or None)

    if form.is_valid():
        buses = Bus.objects.filter(
            from_location=form.cleaned_data['from_location'],
            to_location=form.cleaned_data['to_location'],
            departure_time__date=form.cleaned_data['departure_time'],
        ).order_by('id')

    paginator = Paginator(buses, 5)
    page_number = request.GET.get('page')
    buses = paginator.get_page(page_number)

    context = {
        'buses': buses,
        'form': form,
    }

    return render(request, 'api/buses.html', context)


def show_bus(request, bus_id):
    return render(request, 'api/about_bus.html', {'bus': Bus.objects.get(id=bus_id), 'title': 'Bus'})


@login_required
def profile(request):
    tickets = Booking.objects.filter(user=request.user)
    try:
        photo_profile = get_object_or_404(ProfilePhoto, user=request.user)
    except Http404:
        photo_profile = None

    if request.method == 'POST':
        form = ProfilePhotoForm(request.POST, request.FILES)
        if form.is_valid():
            if photo_profile:
                photo_profile.file = form.cleaned_data['photo']
                photo_profile.save()
            else:
                fp = ProfilePhoto(photo=form.cleaned_data['photo'], user=request.user)
                fp.save()
            return redirect('profile')
    else:
        form = ProfilePhotoForm()

    return render(request, 'api/profile.html', {
        'title': 'Profile',
        'user': request.user,
        'form': form,
        'photo_profile': photo_profile,
        'tickets': tickets
    })


@login_required
def booking_form(request, bus_id):
    bus = get_object_or_404(Bus, id=bus_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.bus = bus
            booking.user = request.user
            booking.save()
            return redirect('success', booking_id=booking.id)
    else:
        form = BookingForm()

    context = {
        'form': form,
        'bus': bus,
    }
    return render(request, 'api/booking_form.html', context)


@login_required
def view_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.user != request.user:
        raise Http404("Сторінка не знайдена.")

    context = {
        'booking': booking,
    }

    return render(request, 'api/view_booking.html', context)


@login_required
def success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.user != request.user:
        raise Http404("Сторінка не знайдена.")

    return render(request, 'api/success.html', {'booking': booking})


def page_not_found(request, exception):
    return render(request, 'api/page_not_found.html', status=404)
