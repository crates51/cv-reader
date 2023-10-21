FROM registry.access.redhat.com/ubi9/python-39

# install requirements

USER 0
RUN yum update -y --allowerasing
RUN yum install -y nc
WORKDIR /usr/src/app
RUN chown 1001:0 /usr/src/app

USER 1001
# install dependencies
RUN python -m pip install --upgrade pip
COPY --chown=1001:0 ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Set the Romanian locale environment variables
ENV LANG ro_RO.UTF-8
ENV LC_ALL ro_RO.UTF-8

# copy files
COPY --chown=1001:0 . /usr/src/app/

# for the flask config
ENV FLASK_ENV=production

# run entrypoint
ENTRYPOINT ["./entrypoint.sh"]
