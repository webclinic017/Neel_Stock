from smartapi import SmartConnect
from smartapi import SmartWebSocket

from .models import Stock


def get_ltp_data(Stock=None):
    symbol = Stock.symbol
    token = Stock.token
    exch = Stock.exch_seg

    obj = SmartConnect(api_key='jUhyTbU0')
    data = obj.generateSession('QQQP1001', '@runav@1995')

    ltp = obj.ltpData(exch, symbol, token)
    if ltp['status']:
        return ltp['data']
