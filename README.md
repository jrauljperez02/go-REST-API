# GO - SOCIAL NETWORK - REST API

### This is the first part of the backend side of Go - REST API

This project is powered by Docker, to run locally this container, follow the next commands on your CLI


    git clone https://github.com/jrauljperez02/go-REST-API.git

    cd go-REST-API


To build the container, verify you have Docker running on your local machine and build the container using


    docker build .

    docker-compose build


To enable the server on localhost:8000, use: 

    docker-compose up


To acceses to Djanngo CLI Provider, use:

    docker-compose run --rm app sh -c 'python manange.py {command} '

