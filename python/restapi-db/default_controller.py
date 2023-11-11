import connexion
import uuid

from openapi_server.db.setting import session
from openapi_server.db import tables


def v1_users_get():  # noqa: E501
    """Get all users.

    Returns an array of User model # noqa: E501

    :rtype: Union[List[User], Tuple[List[User], int], Tuple[List[User], int, Dict[str, str]]
    """

    users = session.query(tables.Users).all()

    return [user.dump() for user in users]


def v1_users_post():  # noqa: E501
    """Create a new User

    Create a new User # noqa: E501

    :param user: user to create
    :type user: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    user_json = connexion.request.get_json()
    user_json["id"] = uuid.uuid4().__str__()

    session.add(tables.Users(**user_json))
    session.commit()

    return user_json


def v1_users_user_id_get(user_id):  # noqa: E501
    """Get user by ID.

    Returns a single User model # noqa: E501

    :param user_id: user id
    :type user_id: str

    :rtype: Union[List[User], Tuple[List[User], int], Tuple[List[User], int, Dict[str, str]]
    """
    user = session.query(tables.Users).filter(tables.Users.id == user_id).one_or_none()

    return user.dump() if user is not None else ("Not found", 404)
