import connexion
import six

from swagger_server.models.pokemon import Pokemon  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_detail import UserDetail  # noqa: E501
from swagger_server.models.user_pokemon_detail import UserPokemonDetail  # noqa: E501
from swagger_server import util


def create_user():  # noqa: E501
    """create a new user

    create a new user # noqa: E501


    :rtype: User
    """
    return 'do some magic!'


def create_user_and_pokemon_relationship(user_id, pokemon_id):  # noqa: E501
    """create a relationship between a user and a pokemon

    create a relationship between a user and a pokemon # noqa: E501

    :param user_id: user id
    :type user_id: str
    :param pokemon_id: pokemon id
    :type pokemon_id: int

    :rtype: UserPokemonDetail
    """
    return 'do some magic!'


def get_all_pokemon(offset=None, limit=None):  # noqa: E501
    """get a list of all pokemons paginated 20 by 20

    Get all pokemons paginated 20 by 20 only calling this path with or without arguments  # noqa: E501

    :param offset: Number where pagination starts
    :type offset: int
    :param limit: number of records to skip for pagination
    :type limit: int

    :rtype: List[Pokemon]
    """
    return 'do some magic!'


def get_all_users():  # noqa: E501
    """get a list of registered users

    get all users with basic information # noqa: E501


    :rtype: List[User]
    """
    return 'do some magic!'


def get_pokemon(pokemon_id):  # noqa: E501
    """get a specific pokemon by id

    get a pokemon using their unique id # noqa: E501

    :param pokemon_id: it&#x27;s the pokemon id
    :type pokemon_id: int

    :rtype: Pokemon
    """
    return 'do some magic!'


def get_user(user_id):  # noqa: E501
    """get an user with their pokemons

    get an specific user with their catched pokemons # noqa: E501

    :param user_id: it&#x27;s the user id
    :type user_id: str

    :rtype: UserDetail
    """
    return 'do some magic!'


def get_user_and_pokemon_relationship(user_id, pokemon_id):  # noqa: E501
    """get a relationship between an user and a pokemon

    get all information related in the relationship between a pokemon and a user # noqa: E501

    :param user_id: user id
    :type user_id: str
    :param pokemon_id: pokemon id
    :type pokemon_id: int

    :rtype: UserPokemonDetail
    """
    return 'do some magic!'
