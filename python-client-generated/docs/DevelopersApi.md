# swagger_client.DevelopersApi

All URIs are relative to *https://virtserver.swaggerhub.com/ypardo/pokeapi2/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](DevelopersApi.md#create_user) | **POST** /user | create a new user
[**create_user_and_pokemon_relationship**](DevelopersApi.md#create_user_and_pokemon_relationship) | **POST** /user/{userId}/pokemon/{pokemonId} | create a relationship between a user and a pokemon
[**get_all_pokemon**](DevelopersApi.md#get_all_pokemon) | **GET** /pokemon | get a list of all pokemons paginated 20 by 20
[**get_all_users**](DevelopersApi.md#get_all_users) | **GET** /user | get a list of registered users
[**get_pokemon**](DevelopersApi.md#get_pokemon) | **GET** /pokemon/{pokemonId} | get a specific pokemon by id
[**get_user**](DevelopersApi.md#get_user) | **GET** /user/{userId} | get an user with their pokemons
[**get_user_and_pokemon_relationship**](DevelopersApi.md#get_user_and_pokemon_relationship) | **GET** /user/{userId}/pokemon/{pokemonId} | get a relationship between an user and a pokemon

# **create_user**
> User create_user()

create a new user

create a new user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()

try:
    # create a new user
    api_response = api_instance.create_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->create_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_and_pokemon_relationship**
> UserPokemonDetail create_user_and_pokemon_relationship(user_id, pokemon_id)

create a relationship between a user and a pokemon

create a relationship between a user and a pokemon

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
user_id = 'user_id_example' # str | user id
pokemon_id = 56 # int | pokemon id

try:
    # create a relationship between a user and a pokemon
    api_response = api_instance.create_user_and_pokemon_relationship(user_id, pokemon_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->create_user_and_pokemon_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| user id | 
 **pokemon_id** | **int**| pokemon id | 

### Return type

[**UserPokemonDetail**](UserPokemonDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_pokemon**
> list[Pokemon] get_all_pokemon(offset=offset, limit=limit)

get a list of all pokemons paginated 20 by 20

Get all pokemons paginated 20 by 20 only calling this path with or without arguments 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
offset = 56 # int | Number where pagination starts (optional)
limit = 56 # int | number of records to skip for pagination (optional)

try:
    # get a list of all pokemons paginated 20 by 20
    api_response = api_instance.get_all_pokemon(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_all_pokemon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Number where pagination starts | [optional] 
 **limit** | **int**| number of records to skip for pagination | [optional] 

### Return type

[**list[Pokemon]**](Pokemon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users**
> list[User] get_all_users()

get a list of registered users

get all users with basic information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()

try:
    # get a list of registered users
    api_response = api_instance.get_all_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_all_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pokemon**
> Pokemon get_pokemon(pokemon_id)

get a specific pokemon by id

get a pokemon using their unique id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
pokemon_id = 56 # int | it's the pokemon id

try:
    # get a specific pokemon by id
    api_response = api_instance.get_pokemon(pokemon_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_pokemon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pokemon_id** | **int**| it&#x27;s the pokemon id | 

### Return type

[**Pokemon**](Pokemon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserDetail get_user(user_id)

get an user with their pokemons

get an specific user with their catched pokemons

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
user_id = 'user_id_example' # str | it's the user id

try:
    # get an user with their pokemons
    api_response = api_instance.get_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| it&#x27;s the user id | 

### Return type

[**UserDetail**](UserDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_and_pokemon_relationship**
> UserPokemonDetail get_user_and_pokemon_relationship(user_id, pokemon_id)

get a relationship between an user and a pokemon

get all information related in the relationship between a pokemon and a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
user_id = 'user_id_example' # str | user id
pokemon_id = 56 # int | pokemon id

try:
    # get a relationship between an user and a pokemon
    api_response = api_instance.get_user_and_pokemon_relationship(user_id, pokemon_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_user_and_pokemon_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| user id | 
 **pokemon_id** | **int**| pokemon id | 

### Return type

[**UserPokemonDetail**](UserPokemonDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

