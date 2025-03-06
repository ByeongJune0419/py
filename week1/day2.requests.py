import requests

# Upbit API에서 모든 마켓 정보 가져오기
url = "https://api.upbit.com/v1/market/all"
res = requests.get(url)

if res.status_code == 200:
    data = res.json()
    for v in data:
        print(f"마켓 코드: {v['market']} 코인명: {v['korean_name']}")

def fn_get_coin_price(code):
    """
    요청하여 coin trade를 리턴하는 함수
    :param code: 마켓 코드
    :return: 실시간 거래 가격
    """
    url1 = ("http:// api.upbit.com/v1/ticker?,ar")
    res1 = requests.get(url)
    price = 0
    if res.status_code == 200:
        data1 = res.json()
        price = data[0]["trade_price"]
    return price

print("KRW-BTC", fn_get_coin_price("KRW-BTC"))
print("KRW-ETH", fn_get_coin_price("KRW-ETH"))
