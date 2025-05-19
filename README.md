## IP Geolocation API

- Django
- Django Rest Framework
- Postgres DB

### Pull image from github
`git clone https://github.com/PrzemekSkladowski/ip_geolocation_api/`

### Set up API key
In the `/ip_geolocation/.env` file paste your API key for [ipstack.com](ipstack.com):
```text
...
IPSTACK_API_KEY=<PASTE YOUR KEY HERE>
```

### Run the project
Be sure to have Docker Desktop running. Execute:

`docker compose up -d`

This will set up two containers, for postgres database and Django app.

### Load sample data
Enter the container shell environment.

`docker exec -it django_app sh`

Run the following command from the container.

`python manage.py migrate`

`python manage.py loaddata sample_data.json`

### Good to go!
You can access the API via the following endpoints:

You can also create a Django superuser using

`python manage.py createsuperuser`

and then view and manage the data in the Django admin panel at: http://localhost:8000/admin

### Tests
Tests can be run using built-in Django command:

`python manage.py test`
