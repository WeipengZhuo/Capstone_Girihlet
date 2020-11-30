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


# def count_composition(seq, bp):
#     counts = 0
#     for b in list(bp):
#         counts += seq.count(b)
#     return counts/len(seq)
#
# def Analysis(df):
#     df['lengths'] = df['sequence'].map(len)
#     letters = ['A', 'T', 'C', 'G', 'AT', 'CG']
#     for l in letters:
#         df[l] = df['sequence'].map(lambda x: count_composition(x, l))
#     return df
#
# def Plotting():
#     import pandas as pd
#
#     df = pd.read_csv('293T_2000ng_small_RNA_S25_R1_001')
#     df = Analysis(df)



if __name__ == "__main__":
    app.run()
