from tkinter import*
from PIL import ImageTk, Image
import random

root = Tk()
root.title("Game")
root.geometry("380x700")
root.resizable(0,0)


scr_player = 0
scr_comp = 0

def score(result):
  global scr_player
  global scr_comp
  if result == "You win":
    canvas_scoreboard1.delete('all')
    scr_player += 1
    
    
    canvas_scoreboard1.create_text(16,26,text=scr_player,fill = 'white',font=('Bebas' ,23))

  if result == "You lose":
    canvas_scoreboard2.delete('all')
    scr_comp += 1
    canvas_scoreboard2.create_text(16,26,text=scr_comp,fill = 'black',font=('Bebas' ,23))
    
  
  return 
def rock(a):
  comp=random.choice(["rock","paper","scissor"])
  show_picked(a,comp)
  images_picked(a,comp)
  
  if comp == a:
    show_result("Draw")
  elif comp == "paper":
    show_result("You lose")
  elif comp == "scissor":
    show_result("You win")

def paper(b):
  comp= random.choice(["rock","paper","scissor"])
  show_picked(b,comp)
  images_picked(b,comp)
  
  if comp == b:
    show_result("Draw")
  elif comp == "scissor":
    show_result("You lose")
  elif comp == "rock":
    show_result("You win")

def scissor(c):
  comp= random.choice(["rock","paper","scissor"])
  show_picked(c,comp)
  images_picked(c,comp)
  
  if comp == c:
    show_result("Draw")
  elif comp == "rock":
    show_result("You lose")
  elif comp == "paper":
    show_result("You win")

def show_picked(player,comp):
  canvas_screen1.delete("all")
  canvas_screen2.delete("all")
  player= canvas_screen1.create_text(90,170,text=player.upper(),font=("Bebas",15),fill="#302e2f")
  comp= canvas_screen2.create_text(90,170,text=comp.upper(),font=("Bebas",15),fill="#302e2f")

def show_result(e):
  canvas_screen3.delete("all")
  canvas_screen3.create_text(60,10,text=e, fill = 'white',font=('Bebas',15))
  score(e)


def images_picked(player,comp):
  if player == "rock":
    canvas_screen1.create_image(0,0,anchor=NW,image=player_rock)

  elif player == "paper":
    canvas_screen1.create_image(0,0,anchor=NW,image=player_paper)

  elif player == "scissor":
    canvas_screen1.create_image(0,0,anchor=NW,image=player_scissor)

  if comp == "rock":
    canvas_screen2.create_image(0,0,anchor=NW,image=com_rock)

  elif comp == "paper":
    canvas_screen2.create_image(0,0,anchor=NW,image=com_paper)

  elif comp == "scissor":
    canvas_screen2.create_image(0,0,anchor=NW,image=com_scissor)


def reset_game():

  canvas_scoreboard1.delete('all')
  canvas_scoreboard2.delete('all')
  canvas_screen1.delete("all")
  canvas_screen2.delete("all")
  canvas_screen3.delete("all")

  global scr_player
  global scr_comp
  scr_player = 0
  scr_comp = 0
  canvas_scoreboard1.create_text(16,26,text=scr_player,fill = 'white',font=('Bebas' ,23))

  canvas_scoreboard2.create_text(16,26,text=scr_comp,fill = 'black',font=('Bebas' ,23))
  return
    
  
    
  

player_rock = ImageTk.PhotoImage(Image.open("rock1.png"))

player_paper = ImageTk.PhotoImage(Image.open("paper1.png"))

player_scissor = ImageTk.PhotoImage(Image.open("scissor1.png"))

com_rock = ImageTk.PhotoImage(Image.open("rock.png"))

com_paper = ImageTk.PhotoImage(Image.open("paper.png"))

com_scissor = ImageTk.PhotoImage(Image.open("scissor.png"))

logo = ImageTk.PhotoImage(Image.open("logo.png"))


scoreboard = ImageTk.PhotoImage(Image.open("scoreboard.png"))


scoreboard1= ImageTk.PhotoImage(Image.open("scoreboard1.png"))


bg = ImageTk.PhotoImage(Image.open("bg.png"))

rock_button = ImageTk.PhotoImage(Image.open("rock_button.png"))

paper_button= ImageTk.PhotoImage(Image.open("paper_button.png"))


scissor_button = ImageTk.PhotoImage(Image.open("scissor_button.png"))


new_game= ImageTk.PhotoImage(Image.open("new_game.png"))


quit_game = ImageTk.PhotoImage(Image.open("quit_game.png"))

canvas_main = Canvas(root, width=380, height=700)

canvas_main.place(x=-2, y=0)

canvas_main.create_image(0,0, anchor = NW, image = bg)

canvas_main.create_image(45,0, anchor = NW, image = logo )

canvas_main.create_image(90,115, anchor = NW, image = scoreboard1)


canvas_main.create_image(3,70, anchor = NW, image = scoreboard)

canvas_main.create_image(45,0, anchor = NW, image = logo )

canvas_main.create_text(90,100, text = "Player", font = "Times 10 bold", fill = "black")

canvas_main.create_text(280,100, text = "Computer", font = "Times 10 bold", fill = "black")

canvas_screen1 = Canvas(root, bg = '#709dff',width=180, height=180,highlightbackground='#143d59')

canvas_screen1.place(x=4, y=165)

canvas_screen2 = Canvas(root, bg = '#ff2e2a',width=180, height=180,highlightbackground='#143d59')


canvas_screen2.place(x=192, y=165)

canvas_screen3 = Canvas(root, bg = '#2d292a',width=130, height=25,highlightthickness=0)


canvas_screen3.place(x=148, y=130)

canvas_scoreboard1 = Canvas(root, bg = 'black',width=50, height=40,highlightbackground='#D3D3D3')

canvas_scoreboard1.place(x=125, y=78)

canvas_scoreboard2 = Canvas(root, bg = 'white',width=50, height=40,highlightbackground='#D3D3D3')

canvas_scoreboard2.place(x=175, y=78)

canvas_scoreboard1.create_text(16,26,text=scr_player,fill = 'white',font=('Bebas',23))

canvas_scoreboard2.create_text(16,26,text=scr_player,fill = 'black',font=('Bebas',23))



button1 = Button(canvas_main,border=1,bg= '#e8bf23',image=rock_button,command = lambda: rock("rock")).place(x=3, y=355)

button2 = Button(canvas_main,border=1,bg= '#2ed755',image=paper_button,command = lambda: paper("paper")).place(x=190, y=355)

button3 = Button(canvas_main,border=1,bg= '#03a8fd',image=scissor_button,command = lambda: scissor("scissor")).place(x=100, y=415)

button4 = Button(canvas_main,border=1,bg= '#03a8fd',image=new_game,command = reset_game).place(x=40, y=520)

button5 = Button(canvas_main,border=1,bg= '#ff6546',image=quit_game,command= root.quit).place(x=200, y=520)


root.mainloop()