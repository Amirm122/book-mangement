import hashlib
import socket 
import datetime
from persiantools.jdatetime import JalaliDate
import os
import json
import pandas
from bidi.algorithm import get_display
from arabic_reshaper import reshape
import matplotlib.pyplot as plt 
def timer_tryagain(try_again_admin:int):
    p= os.path.join(os.getcwd(),"addmincore")
    os.chdir(p)
    host_name = socket.gethostname()
    ip = socket.gethostbyname(host_name)
    with open ("addin.json","r") as myfile:
        result=json.load(myfile)
        if try_again_admin == 0:
            now_datetime = JalaliDate(datetime.datetime.now())
            now_dt = datetime.datetime.now()
            now_dt += datetime.timedelta(minutes=2)
            result[str(ip)]=f"limit until : {now_datetime}{now_dt.time()}"
            return True
        else:
            return False
        
    with open ("addin.json","w") as myfile:
        result=json.dump(result,myfile)

def create_special_tocken():
    pass
def add_stock():
    with open("books.json","r",encoding="utf-8") as myfile:
        result = json.load(myfile)
        all_books=result.keys()
        all_items = list(result.items())
        print(all_items)
    index = 1
    for every_book in all_books:
        print(get_display(reshape(every_book)))
        print(f"{index}-{every_book}")
        index+=1
    selection = int(input("enter the your option:"))
    count = int(input("enter the count of book :"))
    all_items[selection- 1][1]["stock"]= count
    update_data ={}
    for every_book in all_items:
        update_data[every_book[0]]= every_book[1]
    with open("books.json","w",encoding="utf-8") as myfile:
        json.dump(update_data,myfile,ensure_ascii=False)
    return"update stock successfully"
def show_plot():
    with open("books.json","r", encoding="utf-8") as myfile:
        r= json.load(myfile)
    name_books = r.keys()
    name_books_utf=[]
    for i in name_books:
        name_books_utf.append(get_display(reshape(i)))
    count_books =[]
    for data_book in r.values():
        if "stock" in data_book:
            count_books.append(data_book["stock"])
        else:
            count_books.append(0)
    plt.bar(name_books,count_books)
    plt.show()        

add_stock()        