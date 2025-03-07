# w rite, a ppen, r ead
from heapq import nlargest

f = open("delay.txt", 'a', encoding='utf8')
f.write('오늘의 지각자\n')
while True:
    n = input("오늘 지각!(종료:q)")
    if 'q' == n:
        break
    f.write(f'{n}\n')
f.close()