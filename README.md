#kisanproject
# Django React Boilerplate

## About
A [Django](https://www.djangoproject.com/) project boilerplate/template with lots of state of the art libraries and tools like:
- [React](https://facebook.github.io/react/), for building interactive UIs
- [django-js-reverse](https://github.com/ierror/django-js-reverse), for generating URLs on JS
- [Bootstrap 4](https://v4-alpha.getbootstrap.com/), for responsive styling
- [Webpack](https://webpack.js.org/), for bundling static assets
- [Celery](http://www.celeryproject.org/), for background worker tasks
- [WhiteNoise](http://whitenoise.evans.io/en/stable/) with [brotlipy](https://github.com/python-hyper/brotlipy), for efficient static files serving
- [prospector](https://prospector.landscape.io/en/master/) and [ESLint](https://eslint.org/) with [pre-commit](http://pre-commit.com/) for automated quality assurance (does not replace proper testing!)

For continuous integration, a [CircleCI](https://circleci.com/) configuration `.circleci/config.yml` is included.

Also, includes a Heroku `app.json` and a working Django `production.py` settings, enabling easy deployments with ['Deploy to Heroku' button](https://devcenter.heroku.com/articles/heroku-button). Those Heroku plugins are included in `app.json`:
- PostgreSQL, for DB
- Redis, for Celery
- Sendgrid, for e-mail sending
- Papertrail, for logs and platform errors alerts (must set them manually)

This is a good starting point for modern Python/JavaScript web projects.

## Project bootstrap 
- [ ] Make sure you have Python 3.8 installed
- [ ] Install Django with `pip install django`, to have the `django-admin` command available.

- [ ] Create a new virtualenv with either [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) or only virtualenv: `mkvirtualenv kisanproject` or `python -m venv kisanproject-venv`.
    > If you're using Python's virtualenv (the latter option), make sure to create the environment with the suggested name, otherwise it will be added to version control.
- [ ] Make sure the virtualenv is activated `workon kisanproject` or `source kisanproject-venv/bin/activate`.
- [ ] Compile the requirements before installation and install them:  `make compile_install_requirements`
- [ ] Change the first line of README to the name of the project
- [ ] Add an email address to the `ADMINS` settings variable in `backend/kisanproject/settings/base.py`
- [ ] Change the `SERVER_EMAIL` to the email address used to send e-mails in `backend/kisanproject/settings/production.py`
- [ ] Rename the folder `circleci` to `.circleci` with the command `mv circleci .circleci`
- [ ] Rename file backend/.env.example to backend/.env

## Running
#### If you are using plain python:
- Create the migrations for `users` app: 
  `python manage.py makemigrations`
- Run the migrations:
  `python manage.py migrate`

#### If you are using Docker:
- Create the migrations for `users` app:  
  `docker-compose run --rm backend python manage.py makemigrations`
- Run the migrations:
  `docker-compose run --rm backend python manage.py migrate`

### Tools
- Setup [.editorconfig] file in sublime text editor (ref: http://editorconfig.org/), 
- Setup [.prospector.yaml] file (Ref: https://prospector.landscape.io/en/master/) and 
- Setup [.ESLintignore] file (ref: http://eslint.org/) in the text editor you will use to develop.

### Running the project (without docker)
- Open a command line window and go to the project's directory.
- `pip install -r requirements.txt && pip install -r dev-requirements.txt`
- `npm install`
- `npm run start`
- Open another command line window.
- `workon kisanproject-venv` or `source kisanproject-venv/bin/activate` depending on if you are using virtualenvwrapper or just virtualenv.
- Go to the `backend` directory.
- `python manage.py runserver`


### Running the project (with docker)
- Open a command line window and go to the project's directory.
- `docker-compose up -d `
To access the logs for each service run `docker-compose logs -f service_name` (either backend, frontend, etc)

#### Celery
- Open a command line window and go to the project's directory
- `workon kisanproject-venv` or `source kisanproject-venv/bin/activate` depending on if you are using virtualenvwrapper or just virtualenv.
- `python manage.py celery`

### Testing
`make test`

Will run django tests using `--keepdb` and `--parallel`. You may pass a path to the desired test module in the make command. E.g.:

`make test someapp.tests.test_views`

### Adding new pypi libs
Add the libname to either requirements.in or dev-requirents.in, then either upgrade the libs with `make upgrade` or manually compile it and then,  install.
`pip-compile requirements.in > requirements.txt` or `make upgrade`
`pip install -r requirements.txt`

### Cleaning example code ( please note : currently dont do it. one who will develop will change it )
Before you start creating your own apps remove the example:
- Run the command `make clean_examples` in order to clean up the example apps from the front and backend.
- Deregister the example app by removing `'exampleapp.apps.ExampleappConfig'` from ``backend/kisanproject/settings/base.py``.
- Adjust ``backend/kisanproject/urls.py`` to point to your newly created Django app and remove the path configuration that redirects to the deleted example app.

## Deployment 
### Setup
This project comes with an `app.json` file, which can be used to create an app on Heroku from a GitHub repository.

After setting up the project, you can init a repository and push it on GitHub. If your repository is public, you can use the following button:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy) 

If you are in a private repository, access the following link replacing `$YOUR_REPOSITORY_LINK$` with your repository link.

- `https://heroku.com/deploy?template=$YOUR_REPOSITORY_LINK$`

Remember to fill the `ALLOWED_HOSTS` with the URL of your app, the default on heroku is `appname.herokuapp.com`. Replace `appname` with your heroku app name.

### Sentry

[Sentry](https://sentry.io) is already set up on the project. For production, add `SENTRY_DSN` environment variable on Heroku, with your Sentry DSN as the value.

You can test your Sentry configuration by deploying the boilerplate with the sample page and clicking on the corresponding button.

### Sentry source maps for JS files

The `bin/post_compile` script has a step to push Javascript source maps to Sentry, however some environment variables need to be set on Heroku.

You need to enable Heroku dyno metadata on your Heroku App. Use the following command on Heroku CLI:

- `heroku labs:enable runtime-dyno-metadata -a <app name>`

The environment variables that need to be set are:

- `SENTRY_ORG` - Name of the Sentry Organization that owns your Sentry Project.
- `SENTRY_PROJECT_NAME` - Name of the Sentry Project.
- `SENTRY_API_KEY` - Sentry API key that needs to be generated on Sentry. [You can find or create authentication tokens within Sentry](https://sentry.io/api/).

After enabling dyno metadata and setting the environment variables, your next Heroku Deploys will create a release on Sentry where the release name is the commit SHA, and it will push the source maps to it.

## Linting
- Manually with `prospector` and `npm run lint` on project root.
- During development with an editor compatible with prospector and ESLint.

## Pre-commit hooks
- Run `pre-commit install` to enable the hook into your git repo. The hook will run automatically for each commit.
- Run `git commit -m "Your message" -n` to skip the hook if you need.

## Opinionated Settings
Some settings defaults were decided based on Vinta's experiences. Here's the rationale behind them:

### `CELERY_ACKS_LATE = True`
We believe Celery tasks should be idempotent. So for us it's safe to set `CELERY_ACKS_LATE = True` to ensure tasks will be re-queued after a worker failure. Check Celery docs on ["Should I use retry or acks_late?"](https://docs.celeryproject.org/en/latest/faq.html#should-i-use-retry-or-acks-late) for more info.