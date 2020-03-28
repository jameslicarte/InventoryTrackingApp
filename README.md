# InventoryTrackingApp

InventoryTrackingApp is a Docker-Django-Postgres-Vuejs project.
This app main purpose is to track inventory as shipments of items are received and sent. 

## Prerequisities
In order to run this container you'll need docker installed.

## Running the App


```bash
docker-compose up
```

## Running the Test
```bash
docker-compose up app sh -c "python manage.py test && flake8"
```
