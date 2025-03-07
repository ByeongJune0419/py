import random
import requests
def get_lotto():
    """
    로또 번호 6개 생성
    1 ~ 45 사이의 숫자
    :return: set
    """
    lotto_num = set()

    while len(lotto_num) < 6:
        lotto_num.add(random.randint(1,45))
        return lotto_num

def krw_to_usd(krw):
    res = requests.get("http://open.er-api.com/v6/latest/USD")
    re_data = res.json()
    exchange_rate = re_data['rates']['KRW']
    user_usd = krw_to_usd() / exchange_rate
    print(f"환산된 달러 금액:{user_usd} 달러 입니다.")
def usd_to_krw(usd):
    res = requests.get("http://open.er-api.com/v6/latest/USD")
    re_data = res.json()
    exchange_rate = re_data['rates']['KRW']
    user_krw = usd_to_krw() * exchange_rate
    print(f"환산된 원화 금액:{user_krw:.2f}원 입니다.")
#원화 to 달러
#달러 to 원화 함수를 만들어주세요
test = (1, 14, 15)
# to list
test2 = list(test)
# user_lotto 함수 생성
def fn_user_lotto():

# input : 0 ~ n 개(사용자 희망 번호 ) 가변!?
# output : true or false, 메세지, 로또 번호(사용자 희망 번호가 포함된) 여러개!?
# 사용 입력 번호를 포함 시켜서 로또 번호 생성
# 단 사용자 입력은 최대 5개 까지만 포함 슬라이싱?!
# 각 사용자 입력은 1 ~45 사이 수만
# 조건을 만족 하지 않으면 false, 만족하면 true
# 메세지는 false일때 왜 false 인지

del user_lotto(*args):
    flag = True
    msg = "정상 처리!"
    # 조건 1
    for v in args:
        if 1 > v or v> 14 :
            flag = False
            mag = "1~45사이 값만 가능"
            return flag, msg, None
    # 조건 2
    if len(args) > 5:
        msg ="사영자 희망 번호는 5개 까지만!"
    user_num = list(args)[:5]
    lotto = set(user_num)
    while len(lotto) < 6:
        number = random.randint(1,45)
        lotto.add(number)
    return flag, msg, sorted(lost(lotto))

# 모듈네 실행
if __name__ == '__main__':
    print("로또 잘 생성되나")
    print(get_lotto())
    print(f"달러 100은 : {usd_to_krw(100)}원")
    print(f"원화 20000은 : {krw_to_usd(20000)}달러")
