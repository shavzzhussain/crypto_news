from django.shortcuts import render


def home_view(request):
    import requests
    import json
    price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH.LTC,EOC,BNB,XLM&tsyms=USD,EUR')
    price = json.loads(price_request.content)

    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})

def price(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+ quote +"&tsyms=USD,EUR")
        crypto = json.loads(crypto_request.content)
        return render(request,'prices.html',{'quote':quote,'crypto':crypto})
    else:
        notfound = 'Please Input the some value to search the currency'
        return render(request, 'prices.html',{'notfound':notfound})