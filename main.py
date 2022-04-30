from Pixe import Pixe
from colorama import Fore
from time import sleep
from art import logo
import os

p=Pixe()
clear = lambda: os.system('clear')
on=True 
while on:
    print(Fore.LIGHTRED_EX+logo)
    print(Fore.LIGHTGREEN_EX + '''
    
        (1) create a new user
        (2) update user 
        (3) delete user 
        (4) create a new graph
        (5) update a graph
        (6) delete a graph
        (7) post a new pixel
        (8) update a pixel
        (9) delete a pixel
    
        (0) quit()
    
    
          ''')
    
    inp=int(input(Fore.LIGHTRED_EX+'choose a number > '))
    if inp == 1:
        cred= input('username , token ').split(' ')
        print(cred)
        p.create_user(usr=cred[0],token=cred[1])
        sleep(1)
        clear()
    
    if inp == 2:
        cred= input('new token ')
        print(cred)
        p.update_user(new_token=cred)
        sleep(1)
        clear()
    
    
    if inp == 3:
        p.delete_user()
        sleep(1)
        clear()
    if inp == 4:
        print(Fore.LIGHTGREEN_EX+'''
              > id: It is an ID for identifying the pixelation graph.
              > name: It is the name of the pixelation graph. 
              > unit: It is a unit of the quantity recorded 
                in the pixelation graph 
              > type: It is the type of quantity to be handled in the graph.(int / float)
              > color: color of graph [shibafu,momiji,sora,ichou,ajisai,kuro]
    
              ''')
        dt= input("> ").split(' ')
        p.create_graph(id=dt[0],name=dt[1],unit=dt[2],type=dt[3],color=dt[4])
        sleep(1)
        clear()
    if inp == 5:
        print(Fore.LIGHTGREEN_EX+'''
              > id: It is an ID for identifying the pixelation graph.
              > name: It is the name of the pixelation graph. 
              > unit: It is a unit of the quantity recorded 
                in the pixelation graph 
              > type: It is the type of quantity to be handled in the graph.(int / float)
              > color: color of graph [shibafu,momiji,sora,ichou,ajisai,kuro]
    
              ''')
        dt= input("> ").split(' ')
        p.update_graph(id=dt[0],name=dt[1],unit=dt[2],type=dt[3],color=dt[4])
        sleep(1)
        clear()
    
    if inp == 6:
        print(Fore.LIGHTGREEN_EX+'''
              > id: It is an ID for identifying the pixelation graph.
              ''')
        dt= input("> ").split(' ')
        p.delete_graph(id=dt[0])
        sleep(1)
        clear()
    
    if inp == 7:
        print(Fore.LIGHTGREEN_EX+'''
              > id: It is an ID for identifying the pixelation graph.
              > quantity:  Specify the quantity to be registered
    
              ''')
        dt= input("> ").split(' ')
        p.post_pixel(id=dt[0],quantity=dt[1])
        sleep(1)
        clear()
    if inp == 8:
        print(Fore.LIGHTGREEN_EX+'''
              > id: It is an ID for identifying the pixelation graph.
              > quantity:  Specify the quantity to be registered
    
              ''')
        dt= input("> ").split(' ')
        p.update_pixel(id=dt[0],quantity=dt[1])
        sleep(1)
        clear()
    if inp == 9:
        print(Fore.LIGHTGREEN_EX+'''
              > id: It is an ID for identifying the pixelation graph.
              ''')
        dt= input("> ").split(' ')
        p.delete_pixel(id=dt[0])
        sleep(1)
        clear()
    if inp == 0:
        #print(chr(27) + "[2J")
        clear()
        on=False
