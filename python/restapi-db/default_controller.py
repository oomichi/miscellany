import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.user import User  # noqa: E501
from openapi_server import util
from openapi_server.db.setting import session
from openapi_server.db import tables


def v1_users_get():  # noqa: E501
    """Get all users.

    Returns an array of User model # noqa: E501


    :rtype: Union[List[User], Tuple[List[User], int], Tuple[List[User], int, Dict[str, str]]
    """

    users = session.query(tables.Users).all()

    return [user.dump() for user in users]


def v1_users_post(user):  # noqa: E501
    """Create a new User

    Create a new User # noqa: E501

    :param user: user to create
    :type user: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v1_users_user_id_get(user_id):  # noqa: E501
    """Get user by ID.

    Returns a single User model # noqa: E501

    :param user_id: user id
    :type user_id: str

    :rtype: Union[List[User], Tuple[List[User], int], Tuple[List[User], int, Dict[str, str]]
    """
    return 'do some magic!'
