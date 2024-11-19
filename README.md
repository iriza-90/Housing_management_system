
Housing Management System
A Housing Management System built with Django that allows users to manage properties, handle tenant applications, and monitor the status of various rental properties. The system provides an interface for tenants to apply for properties and for landlords to manage their listings.

Table of Contents
Features
Tech Stack
Installation
Usage
Contributing
License
Features
Property Management: Landlords can add, update, and manage rental properties.
Tenant Applications: Tenants can apply for properties with a custom message, and landlords can approve or reject these applications.
Status Tracking: The system tracks the application status (pending, approved, rejected) for each tenant.
User Authentication: Tenants and landlords can log in and manage their respective properties and applications.
Tech Stack
Backend: Django
Database: PostgreSQL (or any database configured with Django)
Frontend: HTML, CSS (Django templates can be used for the frontend)
Version Control: Git
Hosting: GitHub (for code), Heroku/Netlify (for hosting, if applicable)
Installation
To get a local copy of this project running on your machine, follow these steps:

1. Clone the repository:
bash
Copy code
git clone https://github.com/iriza-90/Housing_management_system.git
2. Navigate to the project directory:
bash
Copy code
cd Housing_management_system
3. Set up a virtual environment:
bash
Copy code
python -m venv venv
4. Activate the virtual environment:
On Windows:

bash
Copy code
venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source venv/bin/activate
5. Install dependencies:
bash
Copy code
pip install -r requirements.txt
6. Set up the database:
Make sure you have PostgreSQL installed and set up. You can modify the database settings in settings.py to use the appropriate database configuration.

Then run the migrations:

bash
Copy code
python manage.py migrate
7. Create a superuser (optional for admin access):
bash
Copy code
python manage.py createsuperuser
Follow the prompts to set up the admin account.

Usage
Run the Django development server:

bash
Copy code
python manage.py runserver
Open your browser and go to http://127.0.0.1:8000/.

You can log in as a tenant or landlord:

Tenant: Apply for available properties.
Landlord: Manage your properties and approve/reject tenant applications.
To access the Django Admin panel, go to http://127.0.0.1:8000/admin/ and log in using the superuser credentials.

Contributing
Fork the repository.
Create a new branch (git checkout -b feature-name).
Make your changes.
Commit your changes (git commit -m 'Add feature').
Push to your branch (git push origin feature-name).
Open a pull request.
License
Distributed under the MIT License. See LICENSE for more information.

Acknowledgements
Django Documentation
PostgreSQL Documentation
GitHub
