import logging

from frontend.app import create_app


logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Hello, world!")

    app = create_app()
    app.run()


if __name__ == '__main__':
    main()
