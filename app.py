from flask import Flask, render_template, request, redirect
from alpha_vantage.timeseries import TimeSeries
from bokeh.plotting import figure
from bokeh.embed import components

#use python app.py to run NOT
app = Flask(__name__)
app.vars = {}

@app.route('/', methods= ['GET'])
def index():
    return render_template('/index.html')

@app.route('/index',methods = ['POST'])
def graph():
    app.vars['ticker'] = request.form['stock_ticker']
    script, div = make_plot()
    return render_template('/graph.html', script=script, div=div)


def make_plot():
    ts = TimeSeries(key='USYG6VWRKD3TEBF3', output_format='pandas')
    data, meta_data = ts.get_daily(app.vars['ticker'])
    plots = figure()
    plots.line(data.index, data['4. close'])
    script, div = components(plots)
    return script, div


if __name__ == '__main__':
    app.run(port=8000, debug = 1)
