import logging
from flask import Flask, render_template

logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Hello, world!")
    app.run()
    index()


if __name__ == '__main__':
    main()
