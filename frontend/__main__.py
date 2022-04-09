import logging

from frontend.app import create_app
from frontend.config import config


logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Hello, world!")

    app = create_app()
    app.run(host=config.host, port=config.port, debug=False)


if __name__ == '__main__':
    main()
