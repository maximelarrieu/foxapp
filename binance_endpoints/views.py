from django.shortcuts import render
from binance.spot import Spot
import threading


# Create your views here.
def connector():
    client = Spot(key='OJmlpfKzP5iE0DamvtIt0J5YI5IrP8KRodtTB9aeQypI36oET1DbGixLz0Mkx65k', secret='spgUQE5EUu5dip6tEZKK80p8SFWhGVk6hSdc7gAkGDjVMJhwvLiUpvGG1PB4bwWH')

    return client


def get_btc_usdt_price(request):
    client = connector()
    btcusdt = client.avg_price("BTCUSDT")
    btcusdt_price = btcusdt['price']
    request.session['btcusdt_price'] = btcusdt_price

    return btcusdt_price


def btc_price(request):
    client = connector()
    btcusdt_price = get_btc_usdt_price(request)
    user_assets = client.asset_detail()

    mining_account_list = client.mining_account_list("sha256", "450267197")
    print("mining account", mining_account_list)

    nft = client.nft_transaction_history(0)

    stacking = client.staking_product_list("STAKING")

    exchange = client.exchange_info()

    return render(request, 'binance_endpoints/index.html', context={
        'btcusdt_price': btcusdt_price,
        'user_assets': user_assets,
        'mining_account_list': mining_account_list,
        'nft': nft,
        'stacking': stacking,
        'exchange': exchange
    })


def user_asset(request):
    client = connector()

    # user_assets = client.mining_account_list()
