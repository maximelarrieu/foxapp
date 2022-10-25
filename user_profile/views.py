from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def profile_page(request):
    btcusdt_price = request.session.get('btcusdt_price')
    return render(request, 'user_profile/index.html', context={'btcusdt_price': btcusdt_price})
