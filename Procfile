web: gunicorn kisanproject.wsgi --chdir backend --limit-request-line 8188 --log-file -
worker: celery worker --workdir backend --app=kisanproject -B --loglevel=info
