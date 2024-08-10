# Planetarium API
Second portfolio project.

API service for planetarium manegement written on DRF
## Installing using GitHub
Install PostgresSQL and create db
```
git clone 
cd planetarium_API
python - m venv venv
sourse venv/bin/activate
pip install - r requiments.txt
set ATABASE_URL=postgres://user:password@localhost:5432/mydatabase
set DJANGO_SECRET_KEY=<you secret key>
python manage.py migrate
python manage.py runserver
```

## Run with docker
Docker should be installed
```
docker-compose build
docker-compose up
```

## Getting access
- **creating user via /api/user/register/**
- **get access token via /api/user/token/**

## Features
- **JWT authentificated**
- **Admin panel /admin/**
- **Documentation is located at /api/doc/swagger/**
- **Managing reservation and tickets**
- **Creating AstronomyShow with different ShowThemes**
- **Creating PlanetariumDome**
- **Adding ShowSesions**
- **Filtering AstronomyShow and ShowSessions**



## Database Schema

Here is the database schema for the project:

![Database Schema](assets/shema.png)