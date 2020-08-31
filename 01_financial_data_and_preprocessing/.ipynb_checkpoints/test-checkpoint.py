import quandl

from credentials.register_quandl import QUANDL_KEY

print(QUANDL_KEY)

quandl.ApiConfig.api_key = QUANDL_KEY

df_quandl = quandl.get(dataset='WIKI/AAPL',
                       start_date='2000-01-01',
                       end_date='2010-12-31')
