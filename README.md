# Quotes Service &#182;
This is a starter pack for anyone developing apis using flask-restful and require a boilerplate template. This repository makes use of simple web crawling to fetch quotes of the day. One can build it, run it to understand everything about and easily move it as a microservice for many other use cases using other docker components.

# Structure 🏗
The repository is structured as per the standards as follows:  
```
quote-service
|
|-- app
    |--- api - Here, all api and their functionalities are written.
    |--- models - Here, the Database model can be defined and utilized
    |--- config.py - This is configuration file that most productionized project makes use of.
    |--- __version__.py - This is the version file to indicate the current version of the api spec.
    |--- __init__.py - This is the core file, which initializes the application, generates the swagger spec, and registers the routes
|-- tests - Here, all the tests required for the application can go into.
|-- .env - All the env variables are stored in this file. This is read in the config to generate configs accordingly. Securing this can be done differently.
|-- Dockerfile - The Dockerfile definition defined to build the microservice and serve it at port 5500
|-- env.template - This is just a template to help for developing.
|-- manage.py - The manager file which creates the application and runs it at port 5500
|-- requirements.txt - All the requirements for the service needs to go here.
|-- start_api.sh - By using gunicorn, multiple workers are spawned to start the application in a production way. This is used in Dockerfile.
|-- docker-compose.yml - All the service definitions go here with their build etc...
```

### Setup of Service 💻
The example service already built is the quotes-service. To build and run the existing service you can do the following:  
1. `export HUBUSER=<yourdockerhubusername> && docker-compose build quotes-service`
2. `docker-compose up -d <yourdockerhubusername>/quotes-service or docker run -d -p 5500:5500 <yourdockerhubusername>/quotes-service`
3. `export HUBUSER=<yourdockerhubusername> && docker-compose push quotes-service` (If you wish to push the repo to dockerhub)

Now, when it is running all fine you can open to see the swagger spec at `http://localhost:5500/api/v1/docs` where index and quotes services are available to be executed.  

 
