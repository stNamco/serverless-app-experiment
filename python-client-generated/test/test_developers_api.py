# coding: utf-8

"""
    Simple Pokemon API

    This is a simple API that retrievern information about pokemons  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: ypardo@modyo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.developers_api import DevelopersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDevelopersApi(unittest.TestCase):
    """DevelopersApi unit test stubs"""

    def setUp(self):
        self.api = DevelopersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user(self):
        """Test case for create_user

        create a new user  # noqa: E501
        """
        pass

    def test_create_user_and_pokemon_relationship(self):
        """Test case for create_user_and_pokemon_relationship

        create a relationship between a user and a pokemon  # noqa: E501
        """
        pass

    def test_get_all_pokemon(self):
        """Test case for get_all_pokemon

        get a list of all pokemons paginated 20 by 20  # noqa: E501
        """
        pass

    def test_get_all_users(self):
        """Test case for get_all_users

        get a list of registered users  # noqa: E501
        """
        pass

    def test_get_pokemon(self):
        """Test case for get_pokemon

        get a specific pokemon by id  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        get an user with their pokemons  # noqa: E501
        """
        pass

    def test_get_user_and_pokemon_relationship(self):
        """Test case for get_user_and_pokemon_relationship

        get a relationship between an user and a pokemon  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
