from pandas_datareader import data
import datetime
from bokeh.plotting import show, output_file, figure
start = datetime.datetime(2020,3,1)
end = datetime.datetime(2020,3,10)
df = data.DataReader(name='AAPL', data_source='yahoo', start=start, end=end)
p = figure(x_axis_type='datetime', width=1000, height=300)
p.title.text='Candlestick Chart'

hours_12 = 12*60*60*1000
p.rect(df.index[df.Close > df.Open], (df.Open + df.Close) / 2, hours_12, abs(df.Open - df.Close))

output_file("CS.html")
show(p)