#!/bin/bash
gunicorn --bind 0.0.0.0:3000 --reload --worker-class=gevent --worker-connections=1000 --workers=1 manage:api
exit 0
exec "$@"
