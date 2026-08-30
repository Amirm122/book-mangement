import requests
from bs4 import BeautifulSoup
from arabic_reshaper import reshape
from bidi.algorithm import get_display
import json
import datetime
from persiantools.jdatetime import JalaliDate
def is_alive_website():
    r=requests.get("https://www.iranketab.ir/")
    print(r.content)
    if r.status_code==200:
        return r
    else:
        return"can't connect site"



def scrap_website():
    # r=is_alive_website()
    my_html="""<div class="swiper-wrapper items-stretch" id="swiper-wrapper-3cb74d3855d12959" aria-live="polite" style="transition-duration: 0ms; transform: translate3d(0px, 0px, 0px); transition-delay: 0ms;">
                            <div class="swiper-slide !flex min-w-[120px] lg:min-w-[195px] !max-w-[168px] lg:!max-w-[202px] !h-auto swiper-slide-active" role="group" aria-label="1 / 10" style="width: 145.462px; margin-left: 8px;">

<a b-46i66kjl9i="" href="/book/153-malevil#pts=42250" title="قلعه ی مالویل" class="card product-card-simple" data-entity-id="42250">
    <div b-46i66kjl9i="" class="flex flex-col flex-1 relative overflow-hidden p-3">
        <div b-46i66kjl9i="" class="relative">
            <img src="https://img.iranketab.ir/img/225x330?pic=www.iranketab.ir/Images/ProductImages/687c0c0922f84b808d42a99c19b57ffe.jpg" class="object-cover" alt="قلعه ی مالویل" loading="lazy">
        </div>
        <h5 b-46i66kjl9i="" class="text-sm text-default-800 font-bold truncate pt-2">قلعه ی مالویل</h5>
        <h6 b-46i66kjl9i="" class="text-xs text-default truncate pt-1">روبر مرل</h6>
    </div>
    <div b-46i66kjl9i="" class="w-full h-1 bg-gray-100"></div>
    <div b-46i66kjl9i="" class="p-3 my-auto">
        <div b-46i66kjl9i="" class="flex flex-col">
            <div b-46i66kjl9i="" class="flex items-center text-xs">
                    <span b-46i66kjl9i="" class="bg-danger text-white rounded-md px-1">٪5</span>
                    <span b-46i66kjl9i="" class="grow text-end"><s b-46i66kjl9i="" class="price text-default">650،000</s></span>
            </div>
            <div b-46i66kjl9i="" class="primary-price" dir="ltr">
                <span b-46i66kjl9i="" class="toman text-primary font-bold">617،500</span>
            </div>
        </div>
    </div>
</a>


                            </div>
                            <div class="swiper-slide !flex min-w-[120px] lg:min-w-[195px] !max-w-[168px] lg:!max-w-[202px] !h-auto swiper-slide-next" role="group" aria-label="2 / 10" style="width: 145.462px; margin-left: 8px;">

<a b-46i66kjl9i="" href="/book/849-crime-and-punishment#pts=15810" title="جنایت و مکافات" class="card product-card-simple" data-entity-id="15810">
    <div b-46i66kjl9i="" class="flex flex-col flex-1 relative overflow-hidden p-3">
        <div b-46i66kjl9i="" class="relative">
            <img src="https://img.iranketab.ir/img/225x330?pic=www.iranketab.ir/Images/ProductImages/ceed2f1d4b8f4426855b7780d4b064ba.jpg" class="object-cover" alt="جنایت و مکافات" loading="lazy">
        </div>
        <h5 b-46i66kjl9i="" class="text-sm text-default-800 font-bold truncate pt-2">جنایت و مکافات</h5>
        <h6 b-46i66kjl9i="" class="text-xs text-default truncate pt-1">فئودور داستایفسکی</h6>
    </div>
    <div b-46i66kjl9i="" class="w-full h-1 bg-gray-100"></div>
    <div b-46i66kjl9i="" class="p-3 my-auto">
        <div b-46i66kjl9i="" class="flex flex-col">
            <div b-46i66kjl9i="" class="flex items-center text-xs">
                    <span b-46i66kjl9i="" class="bg-danger text-white rounded-md px-1">٪5</span>
                    <span b-46i66kjl9i="" class="grow text-end"><s b-46i66kjl9i="" class="price text-default">895،000</s></span>
            </div>
            <div b-46i66kjl9i="" class="primary-price" dir="ltr">
                <span b-46i66kjl9i="" class="toman text-primary font-bold">850،250</span>
            </div>
        </div>
    </div>
</a>


                            </div>
                            <div class="swiper-slide !fle

x min-w-[120px] lg:min-w-[195px] !max-w-[168px] lg:!max-w-[202px] !h-auto" role="group" aria-label="3 / 10" style="width: 145.462px; margin-left: 8px;">

<a b-46i66kjl9i="" href="/book/1285-aphorisms-on-the-wisdom-of-life#pts=1285" title="در باب حکمت زندگی" class="card product-card-simple" data-entity-id="1285">
    <div b-46i66kjl9i="" class="flex flex-col flex-1 relative overflow-hidden p-3">
        <div b-46i66kjl9i="" class="relative">
            <img src="https://img.iranketab.ir/img/225x330?pic=www.iranketab.ir/Images/ProductImages/26297851853243d8aaddf18a384d0870.jpg" class="object-cover" alt="در باب حکمت زندگی" loading="lazy">
        </div>
        <h5 b-46i66kjl9i="" class="text-sm text-default-800 font-bold truncate pt-2">در باب حکمت زندگی</h5>
        <h6 b-46i66kjl9i="" class="text-xs text-default truncate pt-1">آرتور شوپنهاور</h6>
    </div>
    <div b-46i66kjl9i="" class="w-full h-1 bg-gray-100"></div>
    <div b-46i66kjl9i="" class="p-3 my-auto">
        <div b-46i66kjl9i="" class="flex flex-col">
            <div b-46i66kjl9i="" class="flex items-center text-xs">
                    <span b-46i66kjl9i="" class="bg-danger text-white rounded-md px-1">٪5</span>
                    <span b-46i66kjl9i="" class="grow text-end"><s b-46i66kjl9i="" class="price text-default">350،000</s></span>
            </div>
            <div b-46i66kjl9i="" class="primary-price" dir="ltr">
                <span b-46i66kjl9i="" class="toman text-primary font-bold">332،500</span>
            </div>
        </div>
    </div>
</a>


                            </div>
                            <div class="swiper-slide !flex min-w-[120px] lg:min-w-[195px] !max-w-[168px] lg:!max-w-[202px] !h-auto" role="group" aria-label="4 / 10" style="width: 145.462px; margin-left: 8px;">

<a b-46i66kjl9i="" href="/book/16257-the-necessary-piece-of-a-coherent-whole" title="تکه هایی از یک کل منسجم (شومیز)" class="card product-card-simple" data-entity-id="16257">
    <div b-46i66kjl9i="" class="flex flex-col flex-1 relative overflow-hidden p-3">
        <div b-46i66kjl9i="" class="relative">
            <img src="https://img.iranketab.ir/img/225x330?pic=www.iranketab.ir/Images/ProductImages/e348af31e581461385da1a0bd3ca5aa9.jpg" class="object-cover" alt="تکه هایی از یک کل منسجم (شومیز)" loading="lazy">
        </div>
        <h5 b-46i66kjl9i="" class="text-sm text-default-800 font-bold truncate pt-2">تکه هایی از یک کل منسجم (شومیز)</h5>
        <h6 b-46i66kjl9i="" class="text-xs text-default truncate pt-1">پونه مقیمی</h6>
    </div>
    <div b-46i66kjl9i="" class="w-full h-1 bg-gray-100"></div>
    <div b-46i66kjl9i="" class="p-3 my-auto">
        <div b-46i66kjl9i="" class="flex flex-col">
            <div b-46i66kjl9i="" class="flex items-center text-xs">
                    <span b-46i66kjl9i="" class="bg-danger text-white rounded-md px-1">٪5</span>
                    <span b-46i66kjl9i="" class="grow text-end"><s b-46i66kjl9i="" class="price text-default">598،000</s></span>
            </div>
            <div b-46i66kjl9i="" class="primary-price" dir="ltr">
                <span b-46i66kjl9i="" class="toman text-primary font-bold">568،100</span>
            </div>
        </div>
    </div>
</a>


                            </div>
                            <div class="swiper-slide !flex min-w-[120px] lg:min-w-[195px] !max-w-[168px] lg:!max-w-[202px] !h-auto" role="group" aria-label="5 / 10" style="width: 145.462px; margin-left: 8px;">

<a b-46i66kjl9i="" href="/book/17768-eat-him-if-you-like#pts=17768" title="آدم خواران" class="card product-card-simple" data-entity-id="17768">
    <div b-46i66kjl9i="" class="flex flex-col flex-1 relative overflow-hidden p-3">
        <div b-46i66kjl9i="" class="relative">
            <img src="https://img.iranketab.ir/img/225x330?pic=www.iranketab.ir/Images/ProductImages/940352d9c47d4eefbe7779f2e80fd6b6.jpg" class="object-cover" alt="آدم خواران" loa

ding="lazy">
        </div>
        <h5 b-46i66kjl9i="" class="text-sm text-default-800 font-bold truncate pt-2">آدم خواران</h5>
        <h6 b-46i66kjl9i="" class="text-xs text-default truncate pt-1">ژان تولی</h6>
    </div>
    <div b-46i66kjl9i="" class="w-full h-1 bg-gray-100"></div>
    <div b-46i66kjl9i="" class="p-3 my-auto">
        <div b-46i66kjl9i="" class="flex flex-col">
            <div b-46i66kjl9i="" class="flex items-center text-xs">
                    <span b-46i66kjl9i="" class="bg-danger text-white rounded-md px-1">٪5</span>
                    <span b-46i66kjl9i="" class="grow text-end"><s b-46i66kjl9i="" class="price text-default">250،000</s></span>
            </div>
            <div b-46i66kjl9i="" class="primary-price" dir="ltr">
                <span b-46i66kjl9i="" class="toman text-primary font-bold">237،500</span>
            </div>
        </div>
    </div>
</a>


                            </div>
                            <div class="swiper-slide !flex min-w-[120px] lg:min-w-[195px] !max-w-[168px] lg:!max-w-[202px] !h-auto" role="group" aria-label="6 / 10" style="width: 145.462px; margin-left: 8px;">

<a b-46i66kjl9i="" href="/book/1045-white-nights#pts=2405" title="شب های روشن (جیبی)" class="card product-card-simple" data-entity-id="2405">
    <div b-46i66kjl9i="" class="flex flex-col flex-1 relative overflow-hidden p-3">
        <div b-46i66kjl9i="" class="relative">
            <img src="https://img.iranketab.ir/img/225x330?pic=www.iranketab.ir/Images/ProductImages/6f7443dc709b48f78a10f87f058b28ba.jpg" class="object-cover" alt="شب های روشن (جیبی)" loading="lazy">
        </div>
        <h5 b-46i66kjl9i="" class="text-sm text-default-800 font-bold truncate pt-2">شب های روشن (جیبی)</h5>
        <h6 b-46i66kjl9i="" class="text-xs text-default truncate pt-1">فئودور داستایفسکی</h6>
    </div>
    <div b-46i66kjl9i="" class="w-full h-1 bg-gray-100"></div>
    <div b-46i66kjl9i="" class="p-3 my-auto">
        <div b-46i66kjl9i="" class="flex flex-col">
            <div b-46i66kjl9i="" class="flex items-center text-xs">
                    <span b-46i66kjl9i="" class="bg-danger text-white rounded-md px-1">٪5</span>
                    <span b-46i66kjl9i="" class="grow text-end"><s b-46i66kjl9i="" class="price text-default">125،000</s></span>
            </div>
            <div b-46i66kjl9i="" class="primary-price" dir="ltr">
                <span b-46i66kjl9i="" class="toman text-primary font-bold">118،750</span>
            </div>
        </div>
    </div>
</a>


                            </div>
                            <div class="swiper-slide !flex min-w-[120px] lg:min-w-[195px] !max-w-[168px] lg:!max-w-[202px] !h-auto" role="group" aria-label="7 / 10" style="width: 145.462px; margin-left: 8px;">

<a b-46i66kjl9i="" href="/book/1332-symphony-of-the-dead#pts=12279" title="سمفونی مردگان" class="card product-card-simple" data-entity-id="12279">
    <div b-46i66kjl9i="" class="flex flex-col flex-1 relative overflow-hidden p-3">
        <div b-46i66kjl9i="" class="relative">
            <img src="https://img.iranketab.ir/img/225x330?pic=www.iranketab.ir/Images/ProductImages/40da71d5a84d466a9afb1b0a5a71360f.jpg" class="object-cover" alt="سمفونی مردگان" loading="lazy">
        </div>
        <h5 b-46i66kjl9i="" class="text-sm text-default-800 font-bold truncate pt-2">سمفونی مردگان</h5>
        <h6 b-46i66kjl9i="" class="text-xs text-default truncate pt-1">عباس معروفی</h6>
    </div>
    <div b-46i66kjl9i="" class="w-full h-1 bg-gray-100"></div>
    <div b-46i66kjl9i="" class="p-3 my-auto">
        <div b-46i66kjl9i="" class="flex flex-col">
            <div b-46i66kjl9i="" class="flex items-center text-xs">
                    <span b-46i66kjl9i="" class="bg-danger text-white rounded-md px-1">٪5</span>
                    <span b-46i66kjl9i="" class="grow text-end"><s b-46i66kjl9i="" class="price text-default">480،000</s></span>
            </div>
            <div b

-46i66kjl9i="" class="primary-price" dir="ltr">
                <span b-46i66kjl9i="" class="toman text-primary font-bold">456،000</span>
            </div>
        </div>
    </div>
</a>


                            </div>
                            <div class="swiper-slide !flex min-w-[120px] lg:min-w-[195px] !max-w-[168px] lg:!max-w-[202px] !h-auto" role="group" aria-label="8 / 10" style="width: 145.462px; margin-left: 8px;">

<a b-46i66kjl9i="" href="/book/12832-padre-sergij#pts=12832" title="پدر سرگی" class="card product-card-simple" data-entity-id="12832">
    <div b-46i66kjl9i="" class="flex flex-col flex-1 relative overflow-hidden p-3">
        <div b-46i66kjl9i="" class="relative">
            <img src="https://img.iranketab.ir/img/225x330?pic=www.iranketab.ir/Images/ProductImages/00e063c0974242da9c9dd6730c1bed78.jpg" class="object-cover" alt="پدر سرگی" loading="lazy">
        </div>
        <h5 b-46i66kjl9i="" class="text-sm text-default-800 font-bold truncate pt-2">پدر سرگی</h5>
        <h6 b-46i66kjl9i="" class="text-xs text-default truncate pt-1">لئو تولستوی</h6>
    </div>
    <div b-46i66kjl9i="" class="w-full h-1 bg-gray-100"></div>
    <div b-46i66kjl9i="" class="p-3 my-auto">
        <div b-46i66kjl9i="" class="flex flex-col">
            <div b-46i66kjl9i="" class="flex items-center text-xs">
                    <span b-46i66kjl9i="" class="bg-danger text-white rounded-md px-1">٪5</span>
                    <span b-46i66kjl9i="" class="grow text-end"><s b-46i66kjl9i="" class="price text-default">190،000</s></span>
            </div>
            <div b-46i66kjl9i="" class="primary-price" dir="ltr">
                <span b-46i66kjl9i="" class="toman text-primary font-bold">180،500</span>
            </div>
        </div>
    </div>
</a>


                            </div>
                            <div class="swiper-slide !flex min-w-[120px] lg:min-w-[195px] !max-w-[168px] lg:!max-w-[202px] !h-auto" role="group" aria-label="9 / 10" style="width: 145.462px; margin-left: 8px;">

<a b-46i66kjl9i="" href="/book/9438-navy-blue" title="سرمه ای" class="card product-card-simple" data-entity-id="9438">
    <div b-46i66kjl9i="" class="flex flex-col flex-1 relative overflow-hidden p-3">
        <div b-46i66kjl9i="" class="relative">
            <img src="https://img.iranketab.ir/img/225x330?pic=www.iranketab.ir/Images/ProductImages/7d1ef462f82b484c8357c1c2a52b8106.jpg" class="object-cover" alt="سرمه ای" loading="lazy">
        </div>
        <h5 b-46i66kjl9i="" class="text-sm text-default-800 font-bold truncate pt-2">سرمه ای</h5>
        <h6 b-46i66kjl9i="" class="text-xs text-default truncate pt-1">حامد عسکری</h6>
    </div>
    <div b-46i66kjl9i="" class="w-full h-1 bg-gray-100"></div>
    <div b-46i66kjl9i="" class="p-3 my-auto">
        <div b-46i66kjl9i="" class="flex flex-col">
            <div b-46i66kjl9i="" class="flex items-center text-xs">
                    <span b-46i66kjl9i="" class="bg-danger text-white rounded-md px-1">٪5</span>
                    <span b-46i66kjl9i="" class="grow text-end"><s b-46i66kjl9i="" class="price text-default">120،000</s></span>
            </div>
            <div b-46i66kjl9i="" class="primary-price" dir="ltr">
                <span b-46i66kjl9i="" class="toman text-primary font-bold">114،000</span>
            </div>
        </div>
    </div>
</a>


                            </div>
                            <div class="swiper-slide !flex min-w-[120px] lg:min-w-[195px] !max-w-[168px] lg:!max-w-[202px] !h-auto" role="group" aria-label="10 / 10" style="width: 145.462px; margin-left: 8px;">

<a b-46i66kjl9i="" href="/book/586-the-myth-of-sisyphus#pts=586" title="اسطوره سیزیف" class="card product-card-simple" data-entity-id="586">
    <div b-46i66kjl9i="" class="flex flex-col flex-1 relative overflow-hidden p-3">
        <div b-46i66kjl9i="" class="relative">
            <img s

rc="https://img.iranketab.ir/img/225x330?pic=www.iranketab.ir/Images/ProductImages/905ffb3b75bd4ed8ae2d823fbcb6ba81.jpg" class="object-cover" alt="اسطوره سیزیف" loading="lazy">
        </div>
        <h5 b-46i66kjl9i="" class="text-sm text-default-800 font-bold truncate pt-2">اسطوره سیزیف</h5>
        <h6 b-46i66kjl9i="" class="text-xs text-default truncate pt-1">آلبر کامو</h6>
    </div>
    <div b-46i66kjl9i="" class="w-full h-1 bg-gray-100"></div>
    <div b-46i66kjl9i="" class="p-3 my-auto">
        <div b-46i66kjl9i="" class="flex flex-col">
            <div b-46i66kjl9i="" class="flex items-center text-xs">
                    <span b-46i66kjl9i="" class="bg-danger text-white rounded-md px-1">٪5</span>
                    <span b-46i66kjl9i="" class="grow text-end"><s b-46i66kjl9i="" class="price text-default">275،000</s></span>
            </div>
            <div b-46i66kjl9i="" class="primary-price" dir="ltr">
                <span b-46i66kjl9i="" class="toman text-primary font-bold">261،250</span>
            </div>
        </div>
    </div>
</a>


                            </div>
            </div>"""
    content=BeautifulSoup(my_html,"html.parser")
    div = content.find("div", attrs={"id":"swiper-wrapper-3cb74d3855d12959"}).find_all("div",class_="swiper-slide")
    with open("books.json", "r", encoding="utf-8") as myfile:
        result = json.load(myfile)
    for every_div in div:
        all_divs = every_div.find("a").find_all("div")
        title = all_divs[0].find("h5").get_text()
        author = all_divs[0].find("h6").get_text()
        price = all_divs[-1].find("span",class_="toman").get_text()
        # print(get_display(reshape(title)))
        # print(get_display(reshape(author)))
        # print(price)
        result[title] = {"price" : price, "author" : author}
    with open("books.json", "w", encoding="utf-8") as myfile:
         json.dump(result,myfile,ensure_ascii=False) 
def login_user():
    global username
    username = input("enter username :")
    password = input("enter password :")         
    with open("users.json","r") as myfile:
        result = json.load(myfile)
    if username in result:
        if password==result[username]:
            return f"welcome {username}",True
        else:
            return "username or password incorrect",False
    else:
        return "username or password incorrect",False

def sigup_user():
    username = input("enter username :")
    if username=="library_addmin":
        return "addmin",True
    password = input("enter password :")         
    with open("users.json","r") as myfile:
        result = json.load(myfile)
    if username not in result:
        result[username] = password

        with open("users.json","w") as myfile:
            json.dump(result,myfile)
        return f"{username} added successfully " 
    else:
        return f"{username} already exist"
def report_user():
    with open("log.txt","a") as myfile:
        now_time=datetime.datetime.now()
        # convert_to_jalali=JalaliDate(now_time)
        now_time=datetime.datetime.strftime(now_time,"%Y-%M-%d %H:%m:%S")
        myfile.write(f"{username} logged at : {now_time}\n")    

def buy_book():
    with open("books.json","r", encoding="utf-8") as myfile:
        result = json.load(myfile)
        all_books = result.keys()
        all_items = list(result.items())
        print(all_items)
    index_temp= 0
    available_books =[]
    for i in all_items:
        if "stock" in i[1]:
            available_books.append(i[0])
            
 
       
    index= 1
    for every_book in available_books:
        print(index, get_display(reshape(every_book)),result[every_book]["stock"],"left")
        index +=1
    selection=  input("enter the number of book to buy:").split()
    for i in selection:
        result[available_books[int(i)-1]]["stock"]-=1
    with open("books.json","w",encoding="utf-8") as myfile:
        json.dump(result,myfile,ensure_ascii=False)  
buy_book()        
scrap_website()      
