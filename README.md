# Hacker News' GraphQL Server

This project was built following [The Fullstack Tutorial for GraphQL](https://www.howtographql.com/).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- Python 3.6
- pipenv

### Installing

Clone the repository

```sh
git clone https://github.com/felipemfp/hackernews-django-graphene.git
```

Install the dependencies

```sh
cd hackernews-django-graphene
pipenv install
```

Enter pipenv shell

```sh
pipenv shell
```

Migrate the database

```sh
python manage.py migrate
```

And you should be ready to run the server

```sh
python manage.py runserver
```

Open http://127.0.0.1:8000/graphql and try some queries or mutations.

## Built With

* [Django](https://www.djangoproject.com/)
* [Graphene](http://graphene-python.org/)

## Contributing

Feel free for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/felipemfp/hackernews-django-graphene/tags). 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details