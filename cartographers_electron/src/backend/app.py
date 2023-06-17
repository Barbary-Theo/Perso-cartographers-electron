from flask import Flask
from route.map_route import init_map_route


def create_app():
    app = Flask(__name__)

    init_map_route(app)

    app.run()


if __name__ == '__main__':
    create_app()