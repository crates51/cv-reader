#!/bin/bash
#set -e
#{
    #mkdir -p migrations/versions  # create empty folder if not exists
    #python manage.py db upgrade &
    #wait $!
    #echo "################################## MIGRATION DONE ##################################"
#} || {
    #echo "################################## MIGRATION FAILED ##################################"
#}
#
#gunicorn --bind 0.0.0.0:5000 --timeout 60 --worker-class=gevent --worker-connections=1000 --workers=3 manage:app

gunicorn --bind 0.0.0.0:3000 --reload --worker-class=gevent --worker-connections=1000 --workers=1 manage:api
exit 0
exec "$@"
