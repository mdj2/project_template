# Project Template

## Introduction

Quick Start Template for ARC projects.
Simply clone this repo, follow the installation instructions, rename the project and app files, and get to work!

## Installation

Make a virtual environment

    virtualenv --no-site-packages .env
    source .env/bin/activate

Start a new Django project using this template

    django-admin.py startproject --template=https://github.com/kfarr2/project_template/archive/master.zip project_name

Install the required packages

    cd project_name
    pip install -r requirements.txt

Change permissions

    chmod 755 manage.py

Edit the local settings file to work with your DB. Get the secret key from the repo manager

    mv project_name/settings/local.py.template project_name/settings/local.py
    vi project_name/settings/local.py

Sync the database

    ./manage.py syncdb
    ./manage.py migrate

Run the server

    make

or

    ./manage.py runserver

NOTE: replace 'project_name' with the name of your project

## Extras

Install RabbitMQ if you need it

    yum install rabbitmq-server
    service rabbitmq-server start
    chkconfig rabbitmq-server on

Run Celery if you are working with task queues

    celery -A project_name.celery worker --loglevel=info

Install ElasticSearch if you need it

    rpm --import http://packages.elasticsearch.org/GPG-KEY-elasticsearch
    echo "[elasticsearch-1.1]
    name=Elasticsearch repository for 1.1.x packages
    baseurl=http://packages.elasticsearch.org/elasticsearch/1.1/centos
    gpgcheck=1
    gpgkey=http://packages.elasticsearch.org/GPG-KEY-elasticsearch
    enabled=1" | sed -e 's/^[ \t]*//'  > /etc/yum.repos.d/elasticsearch.repo
    yum install elasticsearch
    sudo /sbin/chkconfig --add elasticsearch
    sudo service elasticsearch start

If you get an error saying "Can't start up: Not enough memory", update your version of java

    yum install java-1.6.0-openjdk

Rebuild the search index

    ./manage.py rebuild_index
