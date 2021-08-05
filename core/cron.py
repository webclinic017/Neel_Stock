def stock_update_job():
    import requests
    from .models import Stock

    # Stock.objects.all().delete()

    url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'

    r = requests.get(url)

    data = r.json()

    for data in data:
        Stock.objects.create(
            token=data['token'], symbol=data['symbol'], name=data['name'],
            expiry=data['expiry'], strike=data['strike'], lotsize=data['lotsize'],
            instrumenttype=data['instrumenttype'], exch_seg=data['exch_seg'],
            tick_size=data['tick_size']
                             )

    print('done')
