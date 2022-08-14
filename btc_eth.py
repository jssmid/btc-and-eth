from requests import Request, Session
import json
from tkinter import * 
from PIL import ImageTk,Image


#MAIN WINDOW
app = Tk()


#TITLE
app.title("Crypto lab")


#THE WIDTH AND HEIGHT OF THE WINDOW
app.geometry("600x385")


#THE BACKGROUND IMAGE
bg_image = ImageTk.PhotoImage(Image.open("C:\PYTHON PROJCTS VC\crypto\\bg_image3.jpg"))
the_image = Label(app, image=bg_image , width=600, height=389)
the_image.place(x=0,y=0)


#-------------------------------------------------------BITCOIN--------------------------------------------------------
#ENTRY
bitcoin = Entry(app, width=25,background="#99CCFF", font="Rome-B")
bitcoin.place(x=365,y=100)

#TEXT
the_bt_text = Label(app,text="Bitcoin",font="Monospace",bg="#99CCFF")
the_bt_text.place(x=455,y=80)

#----------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------ETHEREUM--------------------------------------------------------
#ENTRY
ethereum = Entry(app, width=25, background="#99CCFF", font="Rome-B")
ethereum.place(x=365,y=200)

#TEXT
the_eth_text = Label(app,text="Ethereum",font="Monospace",bg="#99CCFF")
the_eth_text.place(x=447,y=180)

#----------------------------------------------------------------------------------------------------------------------


#FUNCTIONS
def update():
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
  'start':'1',
  'limit':'2',
  'convert':'USD'
  }
  headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': "API KEY",
  }
  session = Session()
  session.headers.update(headers)

  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  for coin in data['data']:
    if coin['name']== "Bitcoin":
      priceb = str(coin['quote']['USD']['price'])
      bitcoin.delete(0, END)
      bitcoin.insert(0, priceb[:-6] + "                   USD")
    elif coin['name']== "Ethereum":
      pricee = str(coin['quote']['USD']['price'])
      ethereum.delete(0,END)
      ethereum.insert(0, pricee[:-6] + "                  USD")


#THE BUTTON
Update = Button(app, text="UPDATE", padx=15,pady=5,bg="#3367B5",activebackground="#99CCFF", font="arial 15 bold",borderwidth=0, command=update)
Update.place(x=420,y=280)


#LOOP
app.mainloop()