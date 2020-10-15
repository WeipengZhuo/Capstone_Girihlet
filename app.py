import os
from flask import Flask, jsonify, render_template, request, redirect

from sqlalchemy import func
# import database
# import commands
# from model import Model
from config import DevelopmentConfig, ProductionConfig
# import config
TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')


# init flask app instance
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

# setup with the configuration provided by the user / environment
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config.from_envvar('APP_SETTINGS')
app.config.from_object(DevelopmentConfig)

# setup all our dependencies, for now only database using application factory pattern
# database.init_app(app)
# commands.init_app(app)


@app.route("/")
def main_page():
    # items = Model.query.all()
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
