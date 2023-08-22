#!/bin/sh

echo Waiting for database...
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.1
done

echo Database is ready
echo Creating tables...
python3 ./create_db.py

exec "$@"
