# Book management application
from menus import * 
from fuctoin import *
from addmin import *
import datetime
try_again_addmin = 3
default_path = os.getcwd()
while True:
    s=menu_start
    if s == 1:
        msg,flag=login_user()
        if msg == "addmin":
            while True:
                os.chdir(default_path)
                if timer_tryagain(try_again_addmin):
                    break
                s2=menu_addmin_start()
                if s2==1:
                    pass
                elif s2==2:
                    pass
                else:
                    print("not valid\n{try_again_addmin}")
                    try_again_addmin-=1
                    if flag:
                        report_user()
    elif s == 2:
        sigup_user()    