# TicketGO
TicketGO is a web-based platform that allows users to search for, book, and manage bus reservations. Built using Django, the system offers a streamlined and user-friendly experience for booking intercity bus trips.
![Uploading image.png…]()

## Features
- **Bus Search**: Users can search for available buses based on departure location, destination, and travel date.
- **Booking System**: Securely book tickets for available buses.
- **User Authentication**: Register, log in, and manage user profiles, including uploading profile pictures.
- **Admin Panel**: Manage buses, routes, companies, and reservations through the Django admin interface.
- **Pagination**: Browse through a paginated list of available buses.
## Installation
Clone the repository:
1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/ticketgo.git
```
2. **Navigate into the project directory:**
```bash
cd ticketgo
```
3. **Create a virtual environment:**
```bash
python -m venv .venv
```
4. **Activate the virtual environment:**
- On Windows:
```bash
.venv\Scripts\activate
```
- On macOS/Linux:
```bash
source .venv/bin/activate
```
5. **Install dependencies:**
```bash
pip install -r requirements.txt
```
6. **Apply migrations:**
```bash
python manage.py migrate
```
7. **Create a superuser for the Django admin panel:**
```bash
python manage.py createsuperuser
```
8. **Run the development server:**
```bash
python manage.py runserver
```
## Usage
Once the development server is running, you can access the application at ```http://127.0.0.1:8000/```.

- **Search Buses:** Enter the departure location, destination, and date to find available bus routes.
- **Book a Bus:** After finding a bus, click on the "Book" button to proceed with the reservation process.
- **User Profile:** Once logged in, users can update their profile information and upload a profile photo.
## Admin Panel
To manage bus companies, routes, and reservations, go to the Django admin panel at ```http://127.0.0.1:8000/admin/``` and log in with the superuser credentials.
## Dependencies
- Django
- Pillow (for image handling)
- Bootstrap (for frontend UI)
- django-widget-tweaks (for form customization)
