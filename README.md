# django-nonstaffadmin

web application made with python and Django

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
python 3.5+
```

### Installing

A step by step series of examples that tell you how to get a development env running

Enter in your project directory and clone droganalisi

```
git clone https://github.com/slackarea/django-nonstaffadmin.git
```

You need a virtual enviroment so

```
pip install virtualenv

virtualenv venv -p python3

source venv/bin/activate

pip install -r requirements.txt
```
Enter in cloned project and create DataBase a Superuser and
a non-Staff user

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Connect you browser to

http://127.0.0.1:8000


## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Python](https://www.python.org) - Official Site
* [Django](https://www.djangoproject.com) - The web framework used


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/slackarea) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

cooming soon

## Authors

* **Vincenzo Ingrosso** - *Initial work* - [slackarea](https://github.com/slackarea)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
