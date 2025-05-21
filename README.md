## IP Geolocation API

The app allows fetching, storing and deleting geolocation information for IP addresses and URLs.

Allowed operations: 
- GET `localhost:8000/geolocation/` - displays all the stored geolocation information,
- GET `localhost:8000/geolocation/<ip_or_address>` - if IP or URL is already in the database, displays the related information; if it's not, fetches geolocation information from ipstack.com API,
- DELETE `localhost:8000/geolocation/<ip_or_address>` - removes the information for given IP or URL.

Tech stack:
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
You can access the API.

You can also create a Django superuser using

`python manage.py createsuperuser`

and then view and manage the data in the Django admin panel at: http://localhost:8000/admin

### Tests
Tests can be run using built-in Django command:

`python manage.py test`
