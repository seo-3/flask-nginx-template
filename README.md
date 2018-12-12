Tag Management Service
=======

## setup

* `docker-compose up -d --build`
  
* `docker exec -it [コンテナID] bash`

## migration

```
migrate
# python manage.py version_control
# python manage.py upgrade[ or downgrade]

Add
# python manage.py script "add hoges table"
```
