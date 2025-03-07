import requests
import tkinter as tk
from tkinter import ttk # 향상된 tkinter
# 현재 환율을 api로 가져와서
# 선택한 국가의 외화로 계산하여 출력하시오

res = requests.get("http://open.er-api.com/v6/latest/USD")
if res.status_code == 200:
    re_data = res.json()
    exchanges_rates = re_data['rates']


currency_rate_list = [(currency, rate) for currency, rate in exchanges_rates.items()]

ex_rates = currency_rate_list

def convert_currency():
    print('달러', entry_usd.get())
    print('콤보박스 선택', currency.get())
    result.config(text='변환!')

app = tk.Tk()
app.title("환율 변환가")
app.geometry("300x200")
# USD 입력
tk.Label(app, text='USD 금액:').pack(pady=5)
entry_usd = tk.Entry(app)
entry_usd.pack()
# 통화 선택(콤보)
tk.Label(app, text='변환할 통화 선택:').pack(pady=5)
currency = ttk.Combobox(app, values=list(ex_rates))
currency.pack()
# currency.set("KRW")
currency.current(0)
# 변환 버튼
btn = tk.Button(app, text='변환!', command=convert_currency)
btn.pack(pady=5)
# 결과 출력
result = tk.Label(app, text='결과가 여기에 표시됨.')
result.pack(pady=10)
app.mainloop()