# swagger-client
This is a simple API that retrievern information about pokemons

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))

try:
    # create a new user
    api_response = api_instance.create_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->create_user: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | user id
pokemon_id = 56 # int | pokemon id

try:
    # create a relationship between a user and a pokemon
    api_response = api_instance.create_user_and_pokemon_relationship(user_id, pokemon_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->create_user_and_pokemon_relationship: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
offset = 56 # int | Number where pagination starts (optional)
limit = 56 # int | number of records to skip for pagination (optional)

try:
    # get a list of all pokemons paginated 20 by 20
    api_response = api_instance.get_all_pokemon(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_all_pokemon: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))

try:
    # get a list of registered users
    api_response = api_instance.get_all_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_all_users: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
pokemon_id = 56 # int | it's the pokemon id

try:
    # get a specific pokemon by id
    api_response = api_instance.get_pokemon(pokemon_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_pokemon: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | it's the user id

try:
    # get an user with their pokemons
    api_response = api_instance.get_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_user: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | user id
pokemon_id = 56 # int | pokemon id

try:
    # get a relationship between an user and a pokemon
    api_response = api_instance.get_user_and_pokemon_relationship(user_id, pokemon_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_user_and_pokemon_relationship: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://virtserver.swaggerhub.com/ypardo/pokeapi2/1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DevelopersApi* | [**create_user**](docs/DevelopersApi.md#create_user) | **POST** /user | create a new user
*DevelopersApi* | [**create_user_and_pokemon_relationship**](docs/DevelopersApi.md#create_user_and_pokemon_relationship) | **POST** /user/{userId}/pokemon/{pokemonId} | create a relationship between a user and a pokemon
*DevelopersApi* | [**get_all_pokemon**](docs/DevelopersApi.md#get_all_pokemon) | **GET** /pokemon | get a list of all pokemons paginated 20 by 20
*DevelopersApi* | [**get_all_users**](docs/DevelopersApi.md#get_all_users) | **GET** /user | get a list of registered users
*DevelopersApi* | [**get_pokemon**](docs/DevelopersApi.md#get_pokemon) | **GET** /pokemon/{pokemonId} | get a specific pokemon by id
*DevelopersApi* | [**get_user**](docs/DevelopersApi.md#get_user) | **GET** /user/{userId} | get an user with their pokemons
*DevelopersApi* | [**get_user_and_pokemon_relationship**](docs/DevelopersApi.md#get_user_and_pokemon_relationship) | **GET** /user/{userId}/pokemon/{pokemonId} | get a relationship between an user and a pokemon

## Documentation For Models

 - [Pokemon](docs/Pokemon.md)
 - [User](docs/User.md)
 - [UserDetail](docs/UserDetail.md)
 - [UserPokemonDetail](docs/UserPokemonDetail.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

ypardo@modyo.com
