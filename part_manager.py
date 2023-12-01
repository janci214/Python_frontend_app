#import mysql.connector
import datetime
from datetime import date
from datetime import timedelta
from tkinter import *
from tkinter import font as tkFont
from tkinter import ttk
from PIL import ImageTk, Image
from tkcalendar import *
from tkintermapview import TkinterMapView
import babel.numbers

root = Tk()

# menu settings
root.title('U kachničky')
root.geometry("657x777")
root.resizable(False, False)
now = datetime.datetime.utcnow()

# icon settings
icon = PhotoImage(file='./img/icon.png')
root.iconphoto(False, icon)

#mydb = mysql.connector.connect(
   # user='root',
   # password='epesu6unmo',
   # host='localhost',
   # database='itu_database',
   # )

#mycursor = mydb.cursor(buffered=True)
#mycursor1 = mydb.cursor(buffered=True)
#mycursor1.execute("DROP TABLE Objednavka")
#mycursor1.execute("DROP TABLE Rezervacia")
#mycursor.execute("CREATE TABLE IF NOT EXISTS Objednavka (datum VARCHAR(30), obsah VARCHAR(20), stol int UNSIGNED, mnozstvo VARCHAR(20), druh VARCHAR(20),orderID int PRIMARY KEY AUTO_INCREMENT)")
#mycursor1.execute("CREATE TABLE IF NOT EXISTS Rezervacia (datum VARCHAR(30), obsah VARCHAR(20), cas VARCHAR(20) , stol VARCHAR(30), druh VARCHAR(20),reservationID int PRIMARY KEY AUTO_INCREMENT)")
#mycursor1.execute("INSERT INTO Rezervacia (datum, obsah, cas, stol, druh ) VALUES (%s,%s,%s,%s,%s)", ( now.strftime('%Y-%m-%d %H:%M:%S'), "svijany", "8", "2", "syrova"  ))
#mydb.commit()
#mycursor.execute("SELECT * FROM Objednavka")
#mycursor1.execute("SELECT * FROM Rezervacia")

#mycursor.execute("DESCRIBE Objednavka")

#for x in mycursor:
   # print(x)

#pozadie
root.title('Kachnicka')
root.geometry("657x777")

# welcomeScreen frame
welcomeScreen = Frame(root)  # new line
welcomeScreen.pack(fill='both', expand=1)

# other frames
menu = Frame(root)
drinksWindow = Frame(root)
newWindow = Frame(root)
reservationWindow = Frame(root)
gamesWindow = Frame(root)
ordersWindow = Frame(root)
homeScreen = Frame(root)
ordersWindow1 = Frame(root)
ordersWindow2 = Frame(root)

# fonts
helv30_bold = tkFont.Font(family='Helvetica', size=35, weight=tkFont.BOLD)
helv30 = tkFont.Font(family='Helvetica', size=30)
helv36 = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)
big_font = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)
font1 = tkFont.Font(family='Helvetica', size=10)
helv28 = tkFont.Font(family='Helvetica', size=16, weight=tkFont.BOLD)

# pozadie
bg = PhotoImage(file="./img/pozadie2.png")

#                                                      WelcomeScreen                                                   #
# canvas
c = Canvas(welcomeScreen, width=567, height=777, bd=0, highlightthickness=0)
c.pack(fill='both', expand=True)

# new background
bg_sign_up = Image.open("./img/bg_sign_up.png").resize((657, 777))
new_bg = ImageTk.PhotoImage(bg_sign_up)
c.create_image(0, 0, image=new_bg, anchor='nw')

# duck
duck = Image.open("./img/duck.png").resize((250, 250))
new_duck = ImageTk.PhotoImage(duck)
c.create_image(325, 180, image=new_duck, anchor='center')


def open_home():
    welcomeScreen.pack_forget()
    menu.pack_forget()
    newWindow.pack_forget()
    drinksWindow.pack_forget()
    gamesWindow.pack_forget()
    ordersWindow.pack_forget()
    reservationWindow.pack_forget()
    homeScreen.pack(fill='both', expand=1)


def remove_actual_order():
    x = 0
    #z = tree.selection()[0]
    #tree.delete(z)

def remove_actual_order1():
    x = 0
   # z = tree3.selection()[0]
   # tree3.delete(z)


def remove_actual_reservation():
    x = 0
   # a = tree1.selection()[0]
   # tree1.delete(a)

def remove_actual_reservation1():
    x = 0
   # a = tree2.selection()[0]
    #tree2.delete(a)


def open_games():
    homeScreen.pack_forget()
    gamesWindow.pack(fill='both', expand=1)
    reservationWindow.pack_forget()
    ordersWindow.pack_forget()


def open_reservations():
    homeScreen.pack_forget()
    reservationWindow.pack(fill='both', expand=1)
    menu.pack_forget()
    newWindow.pack_forget()
    drinksWindow.pack_forget()
    gamesWindow.pack_forget()
    ordersWindow.pack_forget()


def open_drinks():
    homeScreen.pack_forget()
    drinksWindow.pack(fill='both', expand=1)
    menu.pack_forget()
    ordersWindow.pack_forget()


def zobrazit():
    homeScreen.pack_forget()
    menu.pack(fill='both', expand=1)
    newWindow.pack_forget()
    drinksWindow.pack_forget()
    gamesWindow.pack_forget()
    ordersWindow.pack_forget()
    reservationWindow.pack_forget()


# new window
def open_admin_orders():
    ordersWindow2.pack(fill='both', expand=1)
    ordersWindow1.pack_forget()
    menu.pack_forget()
    welcomeScreen.pack_forget()
    homeScreen.pack_forget()

def open_admin():
    ordersWindow1.pack(fill='both', expand=1)
    menu.pack_forget()
    welcomeScreen.pack_forget()
    ordersWindow2.pack_forget()

def open_contact():
    homeScreen.pack_forget()
    newWindow.pack(fill='both', expand=1)
    menu.pack_forget()
    drinksWindow.pack_forget()
    reservationWindow.pack_forget()
    gamesWindow.pack_forget()
    ordersWindow.pack_forget()


def open_menu():
    homeScreen.pack_forget()
    newWindow.pack_forget()
    drinksWindow.pack_forget()
    menu.pack(fill='both', expand=1)
    reservationWindow.pack_forget()
    gamesWindow.pack_forget()
    ordersWindow.pack_forget()
    reservationWindow.pack_forget()


def open_objednavky():
    homeScreen.pack_forget()
    menu.pack_forget()
    newWindow.pack_forget()
    drinksWindow.pack_forget()
    reservationWindow.pack_forget()
    gamesWindow.pack_forget()
    ordersWindow.pack(fill='both', expand=1)

def check_login():
    if(username.get()=="admin"):
        open_admin()
    else:
        open_home()
    


# login
username = Entry(welcomeScreen, font=helv30, width=20, fg='#F3F8A9', bg='darkturquoise', bd=0)
password = Entry(welcomeScreen, font=helv30, width=20, fg='#F3F8A9', bg='darkturquoise', bd=0)
login = Button(welcomeScreen, text='Login', font=helv30_bold, width=8, fg='#F3F8A9', bg='darkturquoise',
               bd=0, activebackground='#F6F48A', activeforeground='#4FCFCF', command=check_login)
unregistered = Button(welcomeScreen, text="Continue as unregistered", font='Helvetica 18 underline',
                      fg='darkturquoise', bg='#F6F48A', bd=0, command=open_home,
                      activebackground='#4FCFCF', activeforeground='#F6F48A')

c.create_text(325, 350, text="Sign up", font=helv30_bold, fill='#34BCCD', anchor='center')
username.place(x=325, y=450, anchor='center')
password.place(x=325, y=520, anchor='center')
login.place(x=325, y=600, anchor='center')
unregistered.place(x=325, y=680, anchor='center')


username.insert(0, 'username')
password.insert(0, 'password')


def clear(e):
    if username.get() == 'username' and password.get() == 'password':
        username.delete(0, END)
        password.delete(0, END)
    password.config(show='*')


username.bind('<Button-1>', clear)
password.bind('<Button-1>', clear)

#                                                        homeScreen                                                    #
home_background = PhotoImage(file="./img/pozadie2.png")
home_bg = Label(homeScreen, image=home_background)
home_bg.place(x=0, y=0, relwidth=1, relheight=1)

# tlacidlo domov
home_button_for_home = ImageTk.PhotoImage(Image.open('./img/25694.png').resize((40, 47), ))
button_label_for_home = Label(image=home_button_for_home)
button = Button(homeScreen, image=home_button_for_home, command=open_home, borderwidth=0, bg='#abf1f4', highlightthickness=0, bd=0,
                activebackground='#9ad8db')
button.place(x=20, y=10)


def buttons_on_top(frame):
    # tlacidlo rezervacie
    rez_button = Button(frame, text="Rezervácie", font=helv36, bg='#abf1f4', highlightthickness=0, bd=0,
                        activebackground='#9ad8db', command=open_reservations, justify=CENTER, )
    rez_button.place(x=80, y=20)
    # tlacidlo menu
    menu_button = Button(frame, text="Menu", font=helv36, bg='#abf1f4', highlightthickness=0, bd=0,
                         activebackground='#9ad8db', command=zobrazit, justify=CENTER, )
    menu_button.place(x=240, y=20)
    # tlacidlo Kontakt
    contact_button = Button(frame, text="Kontakt", font=helv36, bg='#abf1f4', highlightthickness=0, bd=0,
                         activebackground='#9ad8db', command=open_contact, justify=CENTER, )
    contact_button.place(x=340, y=20)
    # pehlad rezervacii
    objednavky_button = Button(frame, text="Objednavky", font=helv36, bg='#abf1f4', highlightthickness=0, bd=0,
                               activebackground='#9ad8db', command=open_objednavky, justify=CENTER, )
    objednavky_button.place(x=470, y=20)


buttons_on_top(homeScreen)

cal = Calendar(homeScreen, selectmode='day', background='#62CCCC', font='Helvetica 16', borderwidth=1,
               bordercolor='#62CCCC', headersbackground='#62CCCC', headersforeground='white',
               weekendbackground='#99E9E9', othermonthbackground='#99E9E9',
               othermonthwebackground='#99E9E9', selectbackground='#62CCCC')
cal.pack(padx=10, pady=240, anchor='n', fill='both', expand=True)


def get_event():
    date = cal.get_date()
    index_before = date.find('/')
    day_and_year = date[(index_before+1):]
    index_after = day_and_year.find('/')
    day = day_and_year[:index_after]
    if int(day) % 2 == 0:
        is_open.config(text='Closed', foreground='red')
    else:
        is_open.config(text='Open', foreground='#60E474')


event = Button(homeScreen, text="Submit", command=get_event, font=helv30_bold, foreground='white',
               background='darkturquoise', bd=0, activebackground='#CBF7F5', activeforeground='darkturquoise')
event.place(x=330, y=130, anchor='center')

is_open = Label(homeScreen, text='', background='white', font=helv30_bold, fg='darkturquoise')
is_open.place(x=330, y=200, anchor='center')


#tlacidlo domov
bg = PhotoImage(file = "./img/pozadie2.png")
my_label = Label(menu, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)


home_button= ImageTk.PhotoImage(Image.open('./img/25694.png').resize((40,47), ))
button_label= Label(image=home_button)
button = Button(menu, image=home_button, command=open_home, borderwidth=0, bg='#abf1f4', highlightthickness = 0, bd = 0,activebackground= '#9ad8db')
button.place(x=20, y=10)

#tlacidlo rezervacie
rez_button= Button(menu, text="Rezervácie", font= helv36, bg='#abf1f4',highlightthickness = 0, bd = 0, activebackground= '#9ad8db' ,  command=open_reservations, justify = CENTER, )
rez_button.place(x=80, y=20)
#tlacidlo menu
menu_button= Button(menu, text="Menu", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0, activebackground= '#9ad8db' ,  command=zobrazit, justify = CENTER, )
menu_button.place(x=240, y=20)
#tlacidlo Kontakt
menu_button= Button(menu, text="Kontakt", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=open_contact, justify = CENTER, )
menu_button.place(x=340, y=20)
#pehlad rezervacii
objednavky_button= Button(menu, text="Objednavky", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=open_objednavky, justify = CENTER, )
objednavky_button.place(x=470, y=20)

#tlacidlo jedlo

food_button= ImageTk.PhotoImage(Image.open('./img/burger.png').resize((80,80), ))
food_label= Label(image=food_button)
food = Button(menu, image=food_button, command=open_home, borderwidth=0, bg='#FFFFFF', highlightthickness = 0, bd = 0)
food.place(x=75, y=90)
food_lable = Label(menu, text='Fast and yummy,\n good for you tummy!', font= helv36, bg='#FFFFFF')
food_lable.place(x=190, y=110)
#tlacidlo drinky
drink_button= ImageTk.PhotoImage(Image.open('./img/4097652.png').resize((60,60), ))
drink_label= Label(image=drink_button)
drink = Button(menu, image=drink_button, command=open_drinks, borderwidth=0, bg='white', highlightthickness = 0, bd = 0)
drink.place(x=510, y=100)
pointer= ImageTk.PhotoImage(Image.open('./img/pointer.png').resize((60,40), ))
pointer_label =Label(menu, image = pointer, bg="white")
pointer_label.place(x=570, y=110)


#toasty
def objednane_toasty(): 
    stol = variable1.get()
    pocet_toastov = variable55.get()
    #mycursor.execute("INSERT INTO Objednavka (datum, obsah, stol, mnozstvo, druh ) VALUES (%s,%s,%s,%s,%s)", ( now.strftime('%Y-%m-%d %H:%M:%S'), "toastiky", stol, pocet_toastov, ""  ))
    #mydb.commit()

def objednane_hotdogy():
    stol = variable_hotdog.get()
    pocet = variable20.get()
   # mycursor.execute("INSERT INTO Objednavka (datum, obsah, stol, mnozstvo, druh ) VALUES (%s,%s,%s,%s,%s)", ( now.strftime('%Y-%m-%d %H:%M:%S'), "Hot-dog", stol, pocet, ""  ))
    #mydb.commit()

def objednane_pizza():
    stol = variable25.get()
    druh = variable2.get()
   # mycursor.execute("INSERT INTO Objednavka (datum, obsah, stol, mnozstvo, druh ) VALUES (%s,%s,%s,%s,%s)", ( now.strftime('%Y-%m-%d %H:%M:%S'), "Pizza", stol, "1", druh  ))
   # mydb.commit()

obrazocek = ImageTk.PhotoImage(Image.open('./img/toast.png').resize((1,1), ))
toasty_image = ImageTk.PhotoImage(Image.open('./img/toast.png').resize((70,70), ))
container = Label(menu, image=obrazocek, width=600, height=100, bg='#FFCCCC', compound='left')
container.place(x= 30, y= 200)
toastik = Label(menu, image=toasty_image,bg='#FFCCCC')
toastik.place(x= 55, y= 215)
nadpis_toasty = Label(menu, text='Toasty', font = helv28, bg='#FFCCCC')
nadpis_toasty.place(x= 160, y = 210)

text_toasty = Label(menu, text='Výborné toasty s maslom, šunkou, syrom a štipkou oregana. K toastom si \nmôžete pridať rôzne omáčky podľa ponuky, ktoré nájdete na bare', font = font1, bg='#FFCCCC', justify = 'left')
text_toasty.place(x= 163, y = 240)

options55 = ["2", "4", "6", "8"]
variable55 = StringVar(menu)
variable55.set("Mnozstvo")
dropdown = OptionMenu(menu, variable55, *options55)
dropdown.config(bg = '#FFCCCD', bd= 0, highlightthickness = 0,)
dropdown.place(x= 410, y= 271)
menu_button= Button(menu, text="Objednat", bg='#FFCCCC', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=objednane_toasty, justify = CENTER, )
menu_button.place(x=510, y=270)

options1 = ["1", "2", "3", "4","5", "6", "7", "8"]
variable1 = StringVar(menu)
variable1.set("Stol")
dropdown1 = OptionMenu(menu, variable1, *options1)
dropdown1.config(bg = '#FFCCCD', bd= 0, highlightthickness = 0,)
dropdown1.place(x= 340, y= 271)


#hot dog
hot_dog_image = ImageTk.PhotoImage(Image.open('./img/hotdog.png').resize((70,70), ))
container1 = Label(menu, image=obrazocek, width=600, height=100, bg='#FFCCCC', compound='left')
container1.place(x= 30, y= 320)
hot_dog = Label(menu, image=hot_dog_image,bg='#FFCCCC')
hot_dog.place(x= 55, y= 335)
nadpis_hotdog = Label(menu, text='Hot-dogy', font = helv28, bg='#FFCCCC')
nadpis_hotdog.place(x= 160, y = 330)

text_hotdog = Label(menu, text='Výborné Hot-dogy ku ktorým máte na výber celozrnný alebo biely rožok, k \nnemu si môžete pridať rôzne omáčky podľa ponuky, ktoré nájdete na bare', font = font1, bg='#FFCCCC', justify = 'left')
text_hotdog.place(x= 163, y = 360)

options_hotdog = ["1", "2", "3", "4"]
variable_hotdog = StringVar(menu)
variable_hotdog.set("Mnozstvo")
dropdown = OptionMenu(menu, variable_hotdog, *options_hotdog)
dropdown.config(bg = '#FFCCCD', bd= 0, highlightthickness = 0,)
dropdown.place(x= 410, y= 391)
menu_button= Button(menu, text="Objednat", bg='#FFCCCC', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=objednane_hotdogy, justify = CENTER, )
menu_button.place(x=510, y=390)

options1 = ["1", "2", "3", "4","5", "6", "7", "8"]
variable20 = StringVar(menu)
variable20.set("Stol")
dropdown1 = OptionMenu(menu, variable20, *options1)
dropdown1.config(bg = '#FFCCCD', bd= 0, highlightthickness = 0,)
dropdown1.place(x= 340, y= 391)

#pizza

pizza_image = ImageTk.PhotoImage(Image.open('./img/pizza.png').resize((70,70),))
container2 = Label(menu, image=obrazocek, width=600, height=100, bg='#FFCCCC', compound='left')
container2.place(x= 30, y= 440)
pizza = Label(menu, image=pizza_image,bg='#FFCCCC')
pizza.place(x= 55, y= 455)
nadpis_pizza = Label(menu, text='Pizza', font = helv28, bg='#FFCCCC')
nadpis_pizza.place(x= 160, y = 450)

text_pizza = Label(menu, text='Vyberte si jeden zo štyroch druhov výbornej pizze.', font = font1, bg='#FFCCCC', justify = 'left')
text_pizza.place(x= 163, y = 480)

options2 = ["sunkova", "zampionova", "syrova", "pikantni"]
variable2 = StringVar(menu)
variable2.set("Druh")
dropdown2 = OptionMenu(menu, variable2, *options2)
dropdown2.config(bg = '#FFCCCD', bd= 0, highlightthickness = 0,)
dropdown2.place(x= 400, y= 511)
menu_button= Button(menu, text="Objednat", bg='#FFCCCC', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=objednane_pizza, justify = CENTER, )
menu_button.place(x=510, y=510)

options25 = ["1", "2", "3", "4","5", "6", "7", "8"]
variable25 = StringVar(menu)
variable25.set("Stol")
dropdown2 = OptionMenu(menu, variable25, *options25)
dropdown2.config(bg = '#FFCCCD', bd= 0, highlightthickness = 0,)
dropdown2.place(x= 330, y= 511)


#kontaktna stranka
#newWindow.title('Kontakt')
#newWindow.geometry("657x777")
my_label = Label(newWindow, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

button = Button(newWindow, image=home_button, command=open_home, borderwidth=0, bg='#abf1f4', highlightthickness = 0, bd = 0,activebackground= '#9ad8db')
button.place(x=20, y=10)

#tlacidlo rezervacie
rez_button= Button(newWindow, text="Rezervácie", font= helv36, bg='#abf1f4',highlightthickness = 0, bd = 0, activebackground= '#9ad8db' ,  command=open_reservations, justify = CENTER, )
rez_button.place(x=80, y=20)
#tlacidlo menu
menu_button= Button(newWindow, text="Menu", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0, activebackground= '#9ad8db' ,  command=zobrazit, justify = CENTER, )
menu_button.place(x=240, y=20)
#tlacidlo Kontakt
menu_button= Button(newWindow, text="Kontakt", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=open_contact, justify = CENTER, )
menu_button.place(x=340, y=20)
#pehlad rezervacii
objednavky_button= Button(newWindow, text="Objednavky", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=open_objednavky, justify = CENTER, )
objednavky_button.place(x=470, y=20)

my_label1 = Label(newWindow, text='', bg='#abf1f4')
my_label1.place(x=330, y=350)

kontakt_nadpis = Label(newWindow, text= "Tu nás nájdete:", font=helv36, bg="white")
kontakt_nadpis.place(x= 50, y =100)

#map widget
map_widget = TkinterMapView(newWindow, width=557, height =300, corner_radius=0)
map_widget.place(x= 50, y =140)
map_widget.set_address("49.2269902526738, 16.5949563300233",marker=True)

telefon_image = ImageTk.PhotoImage(Image.open('./img/telephone1.png').resize((50,50),))
telefon_label = Label(newWindow, image = telefon_image, font=helv28, bg = 'white')
telefon_label.place(x= 50, y = 440)
number_label = Label(newWindow, text="541 141 013", font=big_font, bg = 'white')
number_label.place(x= 120, y = 460)

marker_image = ImageTk.PhotoImage(Image.open('./img/marker.png').resize((50,50),))
marker_label = Label(newWindow, image = marker_image, font=helv28, bg = 'white')
marker_label.place(x= 50, y = 500)
adress_label = Label(newWindow, text="Božetěchova 1/2, 612 00 Brno-Královo Pole", font=big_font, bg = 'white')
adress_label.place(x= 120, y = 520)

# stranka drinkov
#drinksWindow.title('Kontakt')
#drinksWindow.geometry("657x777")
def objednane_pivko(): 
    stol = variable17.get()
    druh = variable3.get()
   # mycursor.execute("INSERT INTO Objednavka (datum, obsah, stol, mnozstvo, druh ) VALUES (%s,%s,%s,%s,%s)", ( now.strftime('%Y-%m-%d %H:%M:%S'), "pivečko", stol, "1", druh  ))
   # mydb.commit()
def objednane_vinko(): 
    stol = variable6.get()
    druh = variable4.get()
    #mycursor.execute("INSERT INTO Objednavka (datum, obsah, stol, mnozstvo, druh ) VALUES (%s,%s,%s,%s,%s)", ( now.strftime('%Y-%m-%d %H:%M:%S'), "Vinko", stol, "1", druh  ))
   # mydb.commit()
def objednane_kofola(): 
    stol = variable8.get()
    mnozstvo = variable7.get()
   # mycursor.execute("INSERT INTO Objednavka (datum, obsah, stol, mnozstvo, druh ) VALUES (%s,%s,%s,%s,%s)", ( now.strftime('%Y-%m-%d %H:%M:%S'), "Kofola", stol, mnozstvo, "" ))
   # mydb.commit()
my_label2 = Label(drinksWindow, image=bg)
my_label2.place(x=0, y=0, relwidth=1, relheight=1)

button = Button(drinksWindow, image=home_button, command=open_home, borderwidth=0, bg='#abf1f4', highlightthickness = 0, bd = 0,activebackground= '#9ad8db')
button.place(x=20, y=10)

#tlacidlo rezervacie
rez_button= Button(drinksWindow, text="Rezervácie", font= helv36, bg='#abf1f4',highlightthickness = 0, bd = 0, activebackground= '#9ad8db' ,  command=open_reservations, justify = CENTER, )
rez_button.place(x=80, y=20)
#tlacidlo menu
menu_button= Button(drinksWindow, text="Menu", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0, activebackground= '#9ad8db' ,  command=zobrazit, justify = CENTER, )
menu_button.place(x=240, y=20)
#tlacidlo Kontakt
menu_button= Button(drinksWindow, text="Kontakt", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=open_contact, justify = CENTER, )
menu_button.place(x=340, y=20)
#pehlad rezervacii
objednavky_button= Button(drinksWindow, text="Objednavky", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=open_objednavky, justify = CENTER, )
objednavky_button.place(x=470, y=20)

#tlacidlo drinky
drink1 = Button(drinksWindow, image=drink_button, command=open_drinks, borderwidth=0, bg='white', highlightthickness = 0, bd = 0)
drink1.place(x=370, y=100)
food1 = Button(drinksWindow, image=food_button, command=open_menu, borderwidth=0, bg='#FFFFFF', highlightthickness = 0, bd = 0)
food1.place(x=260, y=90)


pivko = ImageTk.PhotoImage(Image.open('./img/beer.png').resize((1,1), ))
pivko_image = ImageTk.PhotoImage(Image.open('./img/beer.png').resize((70,70), ))
container = Label(drinksWindow, image=pivko, width=600, height=100, bg='#FFCCCC', compound='left')
container.place(x= 30, y= 200)
pivecko = Label(drinksWindow, image=pivko_image,bg='#FFCCCC')
pivecko.place(x= 55, y= 215)
nadpis_pivko = Label(drinksWindow, text='Pivko', font = helv28, bg='#FFCCCC')
nadpis_pivko.place(x= 160, y = 210)

text_pivko = Label(drinksWindow, text='Vyberte si u nás z dboch druhov pivka. Na výber sú Svijany 11° a Opice 14° ', font = font1, bg='#FFCCCC', justify = 'left')
text_pivko.place(x= 163, y = 240)

options3 = ["Svijany", "Opice"]
variable3 = StringVar(drinksWindow)
variable3.set("Druh")
dropdown3 = OptionMenu(drinksWindow, variable3, *options3)
dropdown3.config(bg = '#FFCCCD', bd= 0, highlightthickness = 0,)
dropdown3.place(x= 410, y= 271)
menu_button= Button(drinksWindow, text="Objednat", bg='#FFCCCC', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=objednane_pivko, justify = CENTER, )
menu_button.place(x=510, y=270)

options17 = ["1", "2", "3", "4","5", "6", "7", "8"]
variable17 = StringVar(drinksWindow)
variable17.set("Stol")
dropdown5 = OptionMenu(drinksWindow, variable17, *options17)
dropdown5.config(bg = '#FFCCCD', bd= 0, highlightthickness = 0,)
dropdown5.place(x= 340, y= 271)


#vinko
wine_image = ImageTk.PhotoImage(Image.open('./img/wine.png').resize((70,70), ))
container1 = Label(drinksWindow, image=pivko, width=600, height=100, bg='#FFCCCC', compound='left')
container1.place(x= 30, y= 320)
hot_dog = Label(drinksWindow, image=wine_image,bg='#FFCCCC')
hot_dog.place(x= 55, y= 335)
nadpis_hotdog = Label(drinksWindow, text='Vínko', font = helv28, bg='#FFCCCC')
nadpis_hotdog.place(x= 160, y = 330)

text_wine = Label(drinksWindow, text='U nás sa podáva len výborné vínko. Na výber máme: Rulandské šedé a \nRulandské modré. Víno sa podáva v 0,7l fľašiach. ', font = font1, bg='#FFCCCC', justify = 'left')
text_wine.place(x= 160, y = 360)

options4 = ["Rulandské šedé", "Rulandské modré"]
variable4 = StringVar(drinksWindow)
variable4.set("Druh")
dropdown4 = OptionMenu(drinksWindow, variable4, *options4)
dropdown4.config(bg = '#FFCCCD', bd= 0, highlightthickness = 0,)
dropdown4.place(x= 410, y= 391)
menu_button= Button(drinksWindow, text="Objednat", bg='#FFCCCC', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=objednane_vinko, justify = CENTER, )
menu_button.place(x=510, y=390)

options6 = ["1", "2", "3", "4","5", "6", "7", "8"]
variable6 = StringVar(drinksWindow)
variable6.set("Stol")
dropdown6 = OptionMenu(drinksWindow, variable6, *options6)
dropdown6.config(bg = '#FFCCCD', bd= 0, highlightthickness = 0,)
dropdown6.place(x= 340, y= 391)

#kofola

kofola_image = ImageTk.PhotoImage(Image.open('./img/kofola.png').resize((70,70),))
container3 = Label(drinksWindow, image=obrazocek, width=600, height=100, bg='#FFCCCC', compound='left')
container3.place(x= 30, y= 440)
kofola = Label(drinksWindow, image=kofola_image,bg='#FFCCCC')
kofola.place(x= 55, y= 455)
nadpis_kofola = Label(drinksWindow, text='Kofola', font = helv28, bg='#FFCCCC')
nadpis_kofola.place(x= 160, y = 450)

text_kofola = Label(drinksWindow, text='Ste šofér alebo nemáte chuř na alkohol? U nás máme na čapu taktiež kofolu \noriginál', font = font1, bg='#FFCCCC', justify = 'left')
text_kofola.place(x= 163, y = 480)

options7 = ["malá(0.3l)", "veľká(0.5l)"]
variable7 = StringVar(drinksWindow)
variable7.set("Množstvo")
dropdown7 = OptionMenu(drinksWindow, variable7, *options7)
dropdown7.config(bg = '#FFCCCD', bd= 0, highlightthickness = 0,)
dropdown7.place(x= 420, y= 511)
menu_button= Button(drinksWindow, text="Objednat", bg='#FFCCCC', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=objednane_kofola, justify = CENTER, )
menu_button.place(x=510, y=510)

options8 = ["1", "2", "3", "4","5", "6", "7", "8"]
variable8 = StringVar(drinksWindow)
variable8.set("Stol")
dropdown8 = OptionMenu(drinksWindow, variable8, *options8)
dropdown8.config(bg = '#FFCCCD', bd= 0, highlightthickness = 0,)
dropdown8.place(x= 350, y= 511)

#rezervacie
def reservation_table():
    stol2 = chairs.get()
    cas =time.get()
    meno = name_for_reservation.get()
    #mycursor.execute("INSERT INTO Rezervacia (datum, obsah, cas, stol, druh ) VALUES (%s,%s,%s,%s,%s)", ( now.strftime('%Y-%m-%d %H:%M:%S'), meno, cas, stol2, "rezervacia stola"))
    #mydb.commit()

my_label3 = Label(reservationWindow, image=bg)
my_label3.place(x=0, y=0, relwidth=1, relheight=1)

button = Button(reservationWindow, image=home_button, command=open_home, borderwidth=0, bg='#abf1f4', highlightthickness = 0, bd = 0,activebackground= '#9ad8db')
button.place(x=20, y=10)
#tlacidlo rezervacie
rezervacie_button= ImageTk.PhotoImage(Image.open('./img/reserved.png').resize((70,70),))
rezervacie = Button(reservationWindow, image=rezervacie_button, command=open_reservations, borderwidth=0, bg='#FFFFFF', highlightthickness = 0, bd = 0)
rezervacie.place(x=240, y=90)
#tlacidlo hry
hry_button= ImageTk.PhotoImage(Image.open('./img/hry.png').resize((70,70),))
hry = Button(reservationWindow, image=hry_button, command=open_games, borderwidth=0, bg='white', highlightthickness = 0, bd = 0)
hry.place(x=370, y=100)


#tlacidlo rezervacie
rez_button= Button(reservationWindow, text="Rezervácie", font= helv36, bg='#abf1f4',highlightthickness = 0, bd = 0, activebackground= '#9ad8db' ,  command=open_reservations, justify = CENTER, )
rez_button.place(x=80, y=20)
#tlacidlo menu
menu_button= Button(reservationWindow, text="Menu", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0, activebackground= '#9ad8db' ,  command=zobrazit, justify = CENTER, )
menu_button.place(x=240, y=20)
#tlacidlo Kontakt
menu_button= Button(reservationWindow, text="Kontakt", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=open_contact, justify = CENTER, )
menu_button.place(x=340, y=20)
#pehlad rezervacii
objednavky_button= Button(reservationWindow, text="Objednavky", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=open_objednavky, justify = CENTER, )
objednavky_button.place(x=470, y=20)

# TODO: posunut
def clear_name(e):
    name_for_reservation.delete(0, END)

name_for_reservation = Entry(reservationWindow, font='Helvetica 25', width=20, fg='white', bg='darkturquoise', bd=0)
name_for_reservation.place(x=330, y=200, anchor='center')
name_for_reservation.insert(0, 'name')
name_for_reservation.bind('<Button-1>', clear_name)


# chair
chair_number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
                "20", "21", "22"]
chairs = StringVar(reservationWindow)
chairs.set('Miesto')
reserve_chair = OptionMenu(reservationWindow, chairs, *chair_number)
reserve_chair.config(bg='darkturquoise', bd=0, highlightthickness=0, width=5, height=1, font='Helvetica 25',
                     foreground='white', activebackground='#A9EFEC', activeforeground='white')
reserve_chair.place(x=240, y=250, anchor='e')


# time
hours = ["12:00", '13:00',"14:00", "15:00", "16:00", "17:00","18:00", "19:00", "20:00", "21:00"]
time = StringVar(reservationWindow)
time.set('Čas')
reserve_time = OptionMenu(reservationWindow, time,*hours)
reserve_time.config(bg='darkturquoise', bd=0, highlightthickness=0, width=5, height=1, font='Helvetica 25',
                    foreground='white', activebackground='#A9EFEC', activeforeground='white')
reserve_time.place(x=320, y=250, anchor='center')

reservation_chairs = Image.open("./img/reservation.png").resize((400, 400))
reservation = ImageTk.PhotoImage(reservation_chairs)
reservation_label = Label(reservationWindow, image=reservation)
reservation_label.place(x=330, y = 500, anchor='center')

enter = Button(reservationWindow, text='Enter', font='Helvetica 25 bold', width=6, fg='white', bg='#5CE88E',
               bd=0, activebackground='#39B5B0', activeforeground='#4FCFCF', command=reservation_table)
enter.place(x=540, y=250, anchor='e')

#hry
def rezervacia_deskovky(): 
    druh = variable_deskovky.get()
    cas = variable10.get()
   # mycursor.execute("INSERT INTO Rezervacia (datum, obsah, cas, stol, druh ) VALUES (%s,%s,%s,%s,%s)", ( now.strftime('%Y-%m-%d %H:%M:%S'), "deskovky", cas, "", druh  ))
    #mydb.commit()
#gamesWindow.title('Kontakt')
#gamesWindow.geometry("657x777")
my_label3 = Label(gamesWindow, image=bg)
my_label3.place(x=0, y=0, relwidth=1, relheight=1)
#tlacidlo rezervacie
rezervacie = Button(gamesWindow, image=rezervacie_button, command=open_reservations, borderwidth=0, bg='#FFFFFF', highlightthickness = 0, bd = 0)
rezervacie.place(x=240, y=90)
#tlacidlo hry
hry = Button(gamesWindow, image=hry_button, command=open_games, borderwidth=0, bg='white', highlightthickness = 0, bd = 0)
hry.place(x=370, y=100)

button = Button(gamesWindow, image=home_button, command=open_home, borderwidth=0, bg='#abf1f4', highlightthickness = 0, bd = 0,activebackground= '#9ad8db')
button.place(x=20, y=10)
#tlacidlo rezervacie
rez_button= Button(gamesWindow, text="Rezervácie", font= helv36, bg='#abf1f4',highlightthickness = 0, bd = 0, activebackground= '#9ad8db' ,  command=open_reservations, justify = CENTER, )
rez_button.place(x=80, y=20)
#tlacidlo menu
menu_button= Button(gamesWindow, text="Menu", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0, activebackground= '#9ad8db' ,  command=zobrazit, justify = CENTER, )
menu_button.place(x=240, y=20)
#tlacidlo Kontakt
menu_button= Button(gamesWindow, text="Kontakt", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=open_contact, justify = CENTER, )
menu_button.place(x=340, y=20)
#pehlad rezervacii
objednavky_button= Button(gamesWindow, text="Objednavky", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=open_objednavky, justify = CENTER, )
objednavky_button.place(x=470, y=20)

#deskovky
deskovky_image = ImageTk.PhotoImage(Image.open('./img/monopoly.png').resize((70,70), ))
container_deskovky = Label(gamesWindow, image=pivko, width=600, height=100, bg='#FFCCCC', compound='left')
container_deskovky.place(x= 30, y= 200)
deskovky = Label(gamesWindow, image=deskovky_image,bg='#FFCCCC')
deskovky.place(x= 55, y= 215)
nadpis_deskovky = Label(gamesWindow, text='Deskovky', font = helv28, bg='#FFCCCC')
nadpis_deskovky.place(x= 160, y = 210)

text_deskovky = Label(gamesWindow, text='U nás máte na výber veľké množstvo hier. Zarezervujte si ich skôr, ako \nvám ich niekto uchmatne.', font = font1, bg='#FFCCCC', justify = 'left')
text_deskovky.place(x= 163, y = 240)

options_deskovky = ["Monopoly", "Šach","Double", "Človeče","Activity", "Dixit","Ligretto", "Carcassone"]
variable_deskovky = StringVar(gamesWindow)
variable_deskovky.set("Hra")
dropdown_deskovky = OptionMenu(gamesWindow, variable_deskovky, *options_deskovky)
dropdown_deskovky.config(bg = '#FFCCCD', bd= 0, highlightthickness = 0,)
dropdown_deskovky.place(x= 430, y= 271)
rezervovat_button= Button(gamesWindow, text="Rezervovať", bg='#FFCCCC', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=rezervacia_deskovky, justify = CENTER, )
rezervovat_button.place(x=510, y=270)
dnes = date.today()
zajtra = dnes + timedelta(days = 1)
pozajtra = dnes + timedelta(days = 2)
popozajtra = dnes + timedelta(days = 3)
popopozajtra = dnes + timedelta(days = 4)
pluspat =dnes + timedelta(days = 5)
datum = [dnes, zajtra, pozajtra, popozajtra,popopozajtra,pluspat]
variable10 = StringVar(gamesWindow)
variable10.set("Datum")
dropdown10 = OptionMenu(gamesWindow, variable10, *datum)
dropdown10.config(bg = '#FFCCCD', bd= 0, highlightthickness = 0,)
dropdown10.place(x= 290, y= 271)


#billiard
def rezervacia_billiard(): 
    druh = variable11.get()
    cas = variable12.get()
    #mycursor.execute("INSERT INTO Rezervacia (datum, obsah, cas, stol, druh ) VALUES (%s,%s,%s,%s,%s)", ( now.strftime('%Y-%m-%d %H:%M:%S'), "billiard", cas, "", druh  ))
   # mydb.commit()
    
billiard_image = ImageTk.PhotoImage(Image.open('./img/billiard.png').resize((70,70), ))
billiard_container = Label(gamesWindow, image=pivko, width=600, height=100, bg='#FFCCCC', compound='left')
billiard_container.place(x= 30, y= 320)
billiard = Label(gamesWindow, image=billiard_image,bg='#FFCCCC')
billiard.place(x= 55, y= 335)
nadpis_billiard = Label(gamesWindow, text='Kulečník', font = helv28, bg='#FFCCCC')
nadpis_billiard.place(x= 160, y = 330)

text_billiard = Label(gamesWindow, text='Rezervujte si kulečník a zahrajte si s kamarátmi. Rezervácia platí na 1 hodinu.', font = font1, bg='#FFCCCC', justify = 'left')
text_billiard.place(x= 160, y = 360)

billiard_date = [dnes, zajtra, pozajtra, popozajtra,popopozajtra,pluspat]
variable11 = StringVar(gamesWindow)
variable11.set("Dátum")
dropdown11 = OptionMenu(gamesWindow, variable11, *billiard_date)
dropdown11.config(bg = '#FFCCCD', bd= 0, highlightthickness = 0,)
dropdown11.place(x= 410, y= 391)
menu_button= Button(gamesWindow, text="rezervovať", bg='#FFCCCC', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=rezervacia_billiard, justify = CENTER, )
menu_button.place(x=510, y=390)

billiard_time = ["14:00", "15:00", "16:00", "17:00","18:00", "19:00", "20:00", "21:00"]
variable12 = StringVar(gamesWindow)
variable12.set("Čas")
dropdown12 = OptionMenu(gamesWindow, variable12, *billiard_time)
dropdown12.config(bg = '#FFCCCD', bd= 0, highlightthickness = 0,)
dropdown12.place(x= 340, y= 391)

#futbalek
def rezervacia_futbalek(): 
    druhh = variable14.get()
    casik = variable15.get()
    stolik = variable13.get()
   # mycursor.execute("INSERT INTO Rezervacia (datum, obsah, cas, stol, druh ) VALUES (%s,%s,%s,%s,%s)", ( now.strftime('%Y-%m-%d %H:%M:%S'), "billiard", casik, stolik, druhh  ))
   # mydb.commit()

football_image = ImageTk.PhotoImage(Image.open('./img/football.png').resize((70,70),))
football_container = Label(gamesWindow, image=obrazocek, width=600, height=100, bg='#FFCCCC', compound='left')
football_container.place(x= 30, y= 440)
football = Label(gamesWindow, image=football_image,bg='#FFCCCC')
football.place(x= 55, y= 455)
nadpis_football = Label(gamesWindow, text='Futbálek', font = helv28, bg='#FFCCCC')
nadpis_football.place(x= 160, y = 450)

text_football = Label(gamesWindow, text='Rezervujte si kulečník a zahrajte si s kamarátmi. Rezervácia platí na 1 hodinu.\nNa výber máte z dvoch stolov.', font = font1, bg='#FFCCCC', justify = 'left')
text_football.place(x= 163, y = 480)

table_options = ["Stôl 1", "Stôl 2"]
variable13 = StringVar(gamesWindow)
variable13.set("Stôl")
dropdown13 = OptionMenu(gamesWindow, variable13, *table_options)
dropdown13.config(bg = '#FFCCCD', bd= 0, highlightthickness = 0,)
dropdown13.place(x= 430, y= 511)
menu_button= Button(gamesWindow, text="Objednat", bg='#FFCCCC', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=rezervacia_futbalek, justify = CENTER, )
menu_button.place(x=510, y=510)

football_date = [dnes, zajtra, pozajtra, popozajtra,popopozajtra,pluspat]
variable14 = StringVar(gamesWindow)
variable14.set("Dátum")
dropdown14 = OptionMenu(gamesWindow, variable14, *football_date)
dropdown14.config(bg = '#FFCCCD', bd= 0, highlightthickness = 0,)
dropdown14.place(x= 315, y= 511)

football_time = ["14:00", "15:00", "16:00", "17:00","18:00", "19:00", "20:00", "21:00"]
variable15 = StringVar(gamesWindow)
variable15.set("Čas")
dropdown15 = OptionMenu(gamesWindow, variable15, *football_time)
dropdown15.config(bg = '#FFCCCD', bd= 0, highlightthickness = 0,)
dropdown15.place(x= 230, y= 511)

#objednavky
#ordersWindow.title('Kontakt')
#ordersWindow.geometry("657x777")
my_label = Label(ordersWindow, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

button = Button(ordersWindow, image=home_button, command=open_home, borderwidth=0, bg='#abf1f4', highlightthickness = 0, bd = 0,activebackground= '#9ad8db')
button.place(x=20, y=10)

#tlacidlo rezervacie
rez_button= Button(ordersWindow, text="Rezervácie", font= helv36, bg='#abf1f4',highlightthickness = 0, bd = 0, activebackground= '#9ad8db' ,  command=open_reservations, justify = CENTER, )
rez_button.place(x=80, y=20)
#tlacidlo menu
menu_button= Button(ordersWindow, text="Menu", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0, activebackground= '#9ad8db' ,  command=zobrazit, justify = CENTER, )
menu_button.place(x=240, y=20)
#tlacidlo Kontakt
menu_button= Button(ordersWindow, text="Kontakt", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=open_contact, justify = CENTER, )
menu_button.place(x=340, y=20)
#pehlad rezervacii
objednavky_button= Button(ordersWindow, text="Objednavky", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0 , activebackground= '#9ad8db' ,  command=open_objednavky, justify = CENTER, )
objednavky_button.place(x=470, y=20)
#tree = ttk.Treeview(ordersWindow)
#tree["show"] = 'headings'
#tree["columns"] = ("datum","obsah","stol","mnozstvo","druh")

#tree.column("datum", width = 180,  anchor=CENTER)
#tree.column("obsah", width = 100,  anchor=CENTER)
#tree.column("stol", width = 60,  anchor=CENTER)
#ree.column("mnozstvo", width = 100,  anchor=CENTER)
#tree.column("druh", width = 140,  anchor=CENTER)

#tree.heading("datum", text = "datum", anchor=CENTER)
#tree.heading("obsah", text = "obsah", anchor=CENTER)
#tree.heading("stol", text = "stol", anchor=CENTER)
#tree.heading("mnozstvo", text = "mnozstvo", anchor=CENTER)
#tree.heading("druh", text = "druh", anchor=CENTER)

#i = 0
#for ro in mycursor:
#    tree.insert('', i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4]))
#    i = i +1

#tree.place(x=40, y=80)

#tree1 = ttk.Treeview(ordersWindow)
#tree1["show"] = 'headings'
#tree1["columns"] = ("datum","obsah","čas","stôl","druh")

#tree1.column("datum", width = 180,  anchor=CENTER)
#tree1.column("obsah", width = 100,  anchor=CENTER)
#tree1.column("čas", width = 60,  anchor=CENTER)
#tree1.column("stôl", width = 100,  anchor=CENTER)
#tree1.column("druh", width = 140,  anchor=CENTER)

#tree1.heading("datum", text = "datum", anchor=CENTER)
#tree1.heading("obsah", text = "obsah", anchor=CENTER)
#tree1.heading("čas", text = "čas", anchor=CENTER)
#tree1.heading("stôl", text = "stôl", anchor=CENTER)
#tree1.heading("druh", text = "druh/datum", anchor=CENTER)

#j = 0
#for rp in mycursor:
 #   tree.insert('', j, text="", values=(rp[0],rp[1],rp[2],rp[3],rp[4]))
 #   j = j +1

#tree1.place(x=40, y=320)

delete_order = Button(ordersWindow, text ="zrušiť objednavku", command= remove_actual_order )
delete_order.place(x = 40, y = 600)
delete_reservation= Button(ordersWindow, text="zrušiť rezerváciu", command = remove_actual_reservation)
delete_reservation.place(x = 500, y = 600)


my_label = Label(ordersWindow1, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)
nadpis = Label(ordersWindow1, text="Prehľad rezervácií", font= helv36, bg = "white")
nadpis.place(x=20, y = 80)

#tlacidlo rezervacie
rez_button5= Button(ordersWindow1, text="Prehľad rezervácií:", font= helv36, bg='#abf1f4',highlightthickness = 0, bd = 0, activebackground= '#9ad8db' ,  justify = CENTER, )
rez_button5.place(x=30, y=20)
#tlacidlo menu
menu_button3= Button(ordersWindow1, text="Prehľad objednávok", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0, activebackground= '#9ad8db' ,  command=open_admin_orders, justify = CENTER, )
menu_button3.place(x=340, y=20)
#tree2 = ttk.Treeview(ordersWindow1)
#tree2["show"] = 'headings'
#tree2["columns"] = ("datum","obsah","stol","mnozstvo","druh")

#tree2.column("datum", width = 180,  anchor=CENTER)
#tree2.column("obsah", width = 100,  anchor=CENTER)
#tree2.column("stol", width = 60,  anchor=CENTER)
#tree2.column("mnozstvo", width = 100,  anchor=CENTER)
#tree2.column("druh", width = 140,  anchor=CENTER)

#tree2.heading("datum", text = "datum", anchor=CENTER)
#tree2.heading("obsah", text = "obsah", anchor=CENTER)
#tree2.heading("stol", text = "stol", anchor=CENTER)
#tree2.heading("mnozstvo", text = "mnozstvo", anchor=CENTER)
#tree2.heading("druh", text = "druh", anchor=CENTER)

#i = 0
#for ro in mycursor:
#    tree2.insert('', i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4]))
#    i = i +1

#tree2.place(x=40, y=130)
delete_reservation= Button(ordersWindow1, text="zrušiť rezerváciu", command = remove_actual_reservation1)
delete_reservation.place(x = 300, y = 400)

my_label = Label(ordersWindow2, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)
nadpis1 = Label(ordersWindow2, text="Prehľad objednávok", font= helv36, bg = "white")
nadpis1.place(x=20, y = 80)

#tlacidlo rezervacie
rez_button6= Button(ordersWindow2, text="Prehľad rezervácií:", font= helv36, bg='#abf1f4',highlightthickness = 0, bd = 0, activebackground= '#9ad8db' , command=open_admin, justify = CENTER, )
rez_button6.place(x=30, y=20)
#tlacidlo menu
menu_button4= Button(ordersWindow2, text="Prehľad objednávok", font= helv36, bg='#abf1f4', highlightthickness = 0, bd = 0, activebackground= '#9ad8db' ,   justify = CENTER, )
menu_button4.place(x=340, y=20)
#tree3 = ttk.Treeview(ordersWindow2)
#tree3["show"] = 'headings'
#tree3["columns"] = ("datum","obsah","stol","mnozstvo","druh")

#tree3.column("datum", width = 180,  anchor=CENTER)
#tree3.column("obsah", width = 100,  anchor=CENTER)
#tree3.column("stol", width = 60,  anchor=CENTER)
#tree3.column("mnozstvo", width = 100,  anchor=CENTER)
#tree3.column("druh", width = 140,  anchor=CENTER)

#tree3.heading("datum", text = "datum", anchor=CENTER)
#tree3.heading("obsah", text = "obsah", anchor=CENTER)
#tree3.heading("stol", text = "stol", anchor=CENTER)
#tree3.heading("mnozstvo", text = "mnozstvo", anchor=CENTER)
#tree3.heading("druh", text = "druh", anchor=CENTER)

#i = 0
#for ro in mycursor:
 #   tree3.insert('', i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4]))
  #  i = i +1

#tree3.place(x=40, y=130)
delete_order = Button(ordersWindow2, text ="zrušiť objednavku", command= remove_actual_order1 )
delete_order.place(x = 300, y = 400)


#start program

menu.mainloop()