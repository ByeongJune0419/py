import random
from re import split


def fn_user_lotto():
# input : 0 ~ n 개(사용자 희망 번호 ) 가변!?
    user_input = input("번호를 입력해주세요 최대 6개까지!:")
    user_lotto = list(map(int,user_input.split(',')))

    if 1 <= all(user_lotto) <= 45:
        print(True, " 정상 처리 ")
    else:
        print(False, "다시 입력해주세요")
    lotto_num = random.randint(1,45)
# output : true or false, 메세지, 로또 번호(사용자 희망 번호가 포함된) 여러개!?
# 사용 입력 번호를 포함 시켜서 로또 번호 생성
# 단 사용자 입력은 최대 5개 까지만 포함 슬라이싱?!
# 각 사용자 입력은 1 ~45 사이 수만
# 조건을 만족 하지 않으면 false, 만족하면 true
# 메세지는 false일때 왜 false 인지