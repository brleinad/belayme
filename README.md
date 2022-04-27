# BelayMe

Find your next belayer.

## Running Dev

- Install python 3
- Install [poetry](https://python-poetry.org/docs/#installation)
- Start a virtual env`poetry shell`
- Install dependencies `poetry install`
- Run migrations if needed `python manage.py migrate`
- Run the development server `python manage.py runserver`

## Deployment

TODO

```
docker build . -t belayme
docker run -p 8000:8000 -e "SECRET_KEY=secret" -e "ENV=prod" --name belayme-cont belayme 
```