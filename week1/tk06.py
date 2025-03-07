from tkinter import *

def new_file():
    """새 파일 생성"""
def open_file():
    """기존의 txt 파일 열기"""
    pass
def exit_app():
    """프로그램 종료"""
    pass

app =Tk()
app.title("메모장")
text_area = Text(app)
text_area.pack(expand=True, fill='both')
# 메뉴바 생성
menubar = Menu(app)
# '파일' 메뉴 생성
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label='새로 만들기', command=new_file)
file_menu.add_command(label='열기', command=open_file)
file_menu.add_separator()
file_menu.add_command(label='종료', command=exit_app)
# 하위 메뉴
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='PDF로 저장')
sub_menu.add_command(label='TXT로 저장')
file_menu.add_cascade(label='내보내기', menu=sub_menu)

menubar.add_cascade(label='파일', menu=file_menu)
# 메뉴바를 연결
app.config(menu=menubar)
app.mainloop()