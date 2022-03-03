import logging
from flask import Flask
from frontend.user import user

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.register_blueprint(user, url_prefix='/api/v1/users')


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Hello, world!")
    app.run(host='0.0.0.0', port='8000', debug=False)


if __name__ == '__main__':
    main()