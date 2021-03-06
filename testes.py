from bitcointrade import Bitcointrade
import datetime

versao ='v2'
moeda ='LTC'
par = 'BRL' + moeda
exchange = Bitcointrade(versao,par)

ticker = exchange.ticker()
orders = exchange.orders()
trades = exchange.trades()

if ticker['message'] == None:
    print('# TICKER #------------------------------')
    ticker = ticker['data']
    print('última negociação :',ticker['last'])
    print('volume 24h        :',ticker['volume'])
    print('compra            :',ticker['buy'])
    print('venda             :',ticker['sell'])

if orders['message'] == None:
    print('# ORDERS #------------------------------')
    orders = orders['data']
    bids = orders['bids']
    asks = orders['asks']

    for i in range(5):
        print(bids[i])

print('# TRADES #------------------------------')
if trades['message'] == None:
    trades = trades['data']['trades']
    print('mostrar execuções de compra')
    for trade in trades:
        if trade['type'] == 'buy':
            print(trade['amount'],'@',trade['unit_price'])
            print(trade['date'])
            print('______________________')


