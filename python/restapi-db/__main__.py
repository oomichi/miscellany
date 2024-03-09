#!/usr/bin/env python3

import connexion
from datetime import timedelta

from flask_jwt_extended import JWTManager
from openapi_server import encoder
from openapi_server.db.tables import init_tables


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Example API'},
                pythonic_params=True)
    app.app.config['JSON_SORT_KEYS'] = False
    app.app.config['JWT_SECRET_KEY'] = 'need-to-consider-what-is-the-best-here'
    app.app.config['JWT_ALGORITHM'] = 'HS256'
    app.app.config['JWT_LEEWAY'] = 0
    app.app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=300)
    app.app.config['JWT_NOT_BEFORE_DELTA'] = timedelta(seconds=0)

    jwt = JWTManager(app.app)

    app.run(port=8080)


if __name__ == '__main__':
    init_tables()
    main()
