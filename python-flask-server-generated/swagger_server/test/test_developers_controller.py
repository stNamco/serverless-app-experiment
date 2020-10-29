# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.pokemon import Pokemon  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_detail import UserDetail  # noqa: E501
from swagger_server.models.user_pokemon_detail import UserPokemonDetail  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDevelopersController(BaseTestCase):
    """DevelopersController integration test stubs"""

    def test_create_user(self):
        """Test case for create_user

        create a new user
        """
        response = self.client.open(
            '/ypardo/pokeapi2/1.0.0/user',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_user_and_pokemon_relationship(self):
        """Test case for create_user_and_pokemon_relationship

        create a relationship between a user and a pokemon
        """
        response = self.client.open(
            '/ypardo/pokeapi2/1.0.0/user/{userId}/pokemon/{pokemonId}'.format(user_id='user_id_example', pokemon_id=56),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_pokemon(self):
        """Test case for get_all_pokemon

        get a list of all pokemons paginated 20 by 20
        """
        query_string = [('offset', 1),
                        ('limit', 1)]
        response = self.client.open(
            '/ypardo/pokeapi2/1.0.0/pokemon',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_users(self):
        """Test case for get_all_users

        get a list of registered users
        """
        response = self.client.open(
            '/ypardo/pokeapi2/1.0.0/user',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_pokemon(self):
        """Test case for get_pokemon

        get a specific pokemon by id
        """
        response = self.client.open(
            '/ypardo/pokeapi2/1.0.0/pokemon/{pokemonId}'.format(pokemon_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user(self):
        """Test case for get_user

        get an user with their pokemons
        """
        response = self.client.open(
            '/ypardo/pokeapi2/1.0.0/user/{userId}'.format(user_id='user_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_and_pokemon_relationship(self):
        """Test case for get_user_and_pokemon_relationship

        get a relationship between an user and a pokemon
        """
        response = self.client.open(
            '/ypardo/pokeapi2/1.0.0/user/{userId}/pokemon/{pokemonId}'.format(user_id='user_id_example', pokemon_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
