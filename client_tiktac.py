from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from socket import*
from _thread import*
import threading

def send(x):
    socket.send(x.encode('utf-8'))

## define thread function
def recieveThread(socket):
    while True:
        message = socket.recv(2048)
        decodedmessage=message.decode('utf-8')
        if decodedmessage=='a':
           btn1["text"]='O'
           check()  
        if decodedmessage=='b':
           btn2["text"]='O'
           check()
        if decodedmessage=='c':
           btn3["text"]='O'
           check()
        if decodedmessage=='d':
           btn4["text"]='O'
           check()  
        if decodedmessage=='e':
           btn5["text"]='O'
           check()  
        if decodedmessage=='f':
           btn6["text"]='O'
           check()  
        if decodedmessage=='g':
           btn7["text"]='O'
           check()  
        if decodedmessage=='h':
           btn8["text"]='O'
           check()  
        if decodedmessage=='i':
           btn9["text"]='O'  
           check()   
  

  
# create window
window =Tk() 
#set title for the window and and its boundry
window.title("tic tac toe")
window.geometry("400x300")
#create labels for the two players and set text and font type and size  
player1=Label(window,text="player1:X    ",font=('Courier','15'))
player1.grid(row=0,column=0)
player2=Label(window,text="player1:O    ",font=('Courier','15'))
player2.grid(row=1,column=0)
#define actions for each button
def clicked1():
  if btn1["text"]==" ":
         btn1["text"]='X'
         send('a')
         check()
def clicked2():
  if btn2["text"]==" ":
     btn2["text"]='X'
     send('b')
     check()
def clicked3():
  if btn3["text"]==" ":
      btn3["text"]='X'
      send('c')
      check()
def clicked4():
  if btn4["text"]==" ":
      btn4["text"]='X'
      send('d')
      check()
def clicked5():

  if btn5["text"]==" ":
      btn5["text"]='X' 
      send('e')
      check()
def clicked6():

  if btn6["text"]==" ":
      btn6["text"]='X'
      send('f')
      check()
def clicked7():
  if btn7["text"]==" ":
      btn7["text"]='X'
      send('g')
      check()
def clicked8():
  if btn8["text"]==" ":
      btn8["text"]='X'
      send('h')
      check()
def clicked9():
  if btn9["text"]==" ":
      btn9["text"]='X'
      send('i')
      check()
#create 9buttons and its background color  
btn1=Button(window,text=" ",bg="blue",fg="black",width=3,height=1,command=clicked1)
btn2=Button(window,text=" ",bg="blue",fg="black",width=3,height=1,command=clicked2)
btn3=Button(window,text=" ",bg="blue",fg="black",width=3,height=1,command=clicked3)
btn4=Button(window,text=" ",bg="blue",fg="black",width=3,height=1,command=clicked4)
btn5=Button(window,text=" ",bg="blue",fg="black",width=3,height=1,command=clicked5)
btn6=Button(window,text=" ",bg="blue",fg="black",width=3,height=1,command=clicked6)
btn7=Button(window,text=" ",bg="blue",fg="black",width=3,height=1,command=clicked7)
btn8=Button(window,text=" ",bg="blue",fg="black",width=3,height=1,command=clicked8)
btn9=Button(window,text=" ",bg="blue",fg="black",width=3,height=1,command=clicked9)
btn1.grid(row=0,column=1)
btn2.grid(row=0,column=2)
btn3.grid(row=0,column=3)
btn4.grid(row=1,column=1)
btn5.grid(row=1,column=2)
btn6.grid(row=1,column=3)
btn7.grid(row=2,column=1)
btn8.grid(row=2,column=2)
btn9.grid(row=2,column=3)
flag =1
#check each round for a winner 
def check():
     global flag
     flag =flag+1
     b1=btn1["text"]
     b2=btn2["text"]
     b3=btn3["text"]
     b4=btn4["text"]
     b5=btn5["text"]
     b6=btn6["text"]
     b7=btn7["text"]
     b8=btn8["text"]
     b9=btn9["text"]
     if (b1==b2 and b2==b3 and b1=='X')or (b1==b2 and b2==b3 and b1=='O')  : 
        win(b1)
     else:
       if (b4==b5 and b5==b6 and b4=='X')or(b4==b5 and b5==b6 and b4=='O') : 
           win(b4)
       else:
         if (b7==b8 and b8==b9 and b7=='X')or (b7==b8 and b8==b9 and b7=='O'): 
          win(b7)
         else:
           if (b1==b4 and b4==b7 and b1=='X')or(b1==b4 and b4==b7 and b1=='O') : 
             win(b1)
           else:  
             if (b2==b5 and b5==b8 and b2 =='X')or(b2==b5 and b5==b8 and b2 =='O') : 
              win(b2)
             else:  
              if (b3==b6 and b6==b9 and b3=='X')or (b3==b6 and b6==b9 and b3=='O'): 
                win(b3)
              else:
                 if (b1==b5 and b5==b9 and b1=='X')or(b1==b5 and b5==b9 and b1=='O') : 
                    win(b1)  
                 else:  
                  if (b3==b5 and b5==b7 and b3=='X')or(b3==b5 and b5==b7 and b3=='O') : 
                   win(b3) 
                  else:      
                   if flag==10 :
                    #if all buttons was clicked show a draw message   
                     messagebox.showinfo("draw")
                     #close program
                     window.destroy()
#determine the winner                   
def win(player):
    if player=='X':
       messagebox.showinfo("player X win the game")
    if player=='O':
       messagebox.showinfo("player O win the game")


## creating socket and connect 
socket = socket(AF_INET,SOCK_STREAM)
host = '127.0.0.1'
port = 3002
socket.connect((host,port))
## creating thread 
recieve = threading.Thread(target=recieveThread,args=(socket,))
recieve.start()

#show the window      
window.mainloop()
