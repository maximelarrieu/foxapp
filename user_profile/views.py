from binance.spot import Spot
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from binance_endpoints import views


# Create your views here.
def binance_connector():
    client = Spot(key='OJmlpfKzP5iE0DamvtIt0J5YI5IrP8KRodtTB9aeQypI36oET1DbGixLz0Mkx65k', secret='spgUQE5EUu5dip6tEZKK80p8SFWhGVk6hSdc7gAkGDjVMJhwvLiUpvGG1PB4bwWH')

    return client


# Create your views here
@login_required
def profile_page(request):
    btcusdt_price = request.session.get('btcusdt_price')

    return render(request, 'user_profile/index.html', context={'btcusdt_price': btcusdt_price})


def get_nft_list(request):
    nft = client.nft
def nft_transaction_history(request):
    client = views.connector()

    nft_transaction_history = client.nft_transaction_history(0)

    return render(request, 'user_profile/nft_list.html', context={'nft_transaction_history': nft_transaction_history})
