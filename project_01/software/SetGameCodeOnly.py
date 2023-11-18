"""
--------------------------------------------------------------------------
Set Game
--------------------------------------------------------------------------
License:
Copyright 2023 - Sunny Yu
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors
may be used to endorse or promote products derived from this software without
specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------
Set Game
This drivers codes the card game Set and ellicits a motor to turn after winning
the game and pressing a button (thus dispensing candy).

Note: initial set up is required to sync the graphics from tkinter onto the SPI
screen. If the user doesn't want to play the game on a SPI screen, but rather
on a laptop, the code for the card game Set (excluding code for the button and 
motor) works properly in other programs, such as visual studio code. 

"""

# Import libraries 
import random
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import Label
import time
import os

# Set up SPI screen as environment for game display
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0')
    os.environ.__setitem__('DISPLAY', ':0.0')


# Global variables
global button_array, card_array, active_cards, card_name_array, score, end_sign
global time_duration, game_running, horizontal_size, vertical_size
button_array = []
card_array = []
active_cards = []
card_name_array = []

# Initializing variables 
score = 0
horizontal_size = 320
vertical_size = 240
end_sign = False
game_on = True
game_running = False

def change_display_screens():
    # changes the screen to the welcome screen
    start_frame.pack()
    game_frame.pack_forget()
    rules_frame.pack_forget()
    examples_frame.pack_forget()
    end_frame.pack_forget()
# end def

def change_to_instruction_screens():
    # changes the screen to the instructions
    rules_frame.pack()
    game_frame.pack_forget()
    start_frame.pack_forget()
    examples_frame.pack_forget()
    end_frame.pack_forget()
# end def  

def see_example():
    # changes the screen to the examples
    examples_frame.pack()
    game_frame.pack_forget()
    start_frame.pack_forget()
    rules_frame.pack_forget()
    end_frame.pack_forget()
# end def

def change_title_game():
    # changes the screen to the starting screen (with cards)
    game_frame.pack()
    start_frame.pack_forget()
    rules_frame.pack_forget()
    examples_frame.pack_forget()
    end_frame.pack_forget()
# end def 

def change_win_game():
    # changes the screen to the end/win screen
    end_frame.pack()
    game_frame.pack_forget()
    start_frame.pack_forget()
    rules_frame.pack_forget()
    examples_frame.pack_forget()
# end def
    
def start ():
    # codes the majority of the game

    # variables
    global score, timer_duration, game_running
    game_running = True

    # changes screen to screen with game cards
    change_title_game()
    
    # Variables needed for the game
    global deck, card_array, button_array, card_name_array, score
    deck = []
    card_array = []
    button_array = []
    card_name_array = []

    # Variables needed for the timer and score
    global start_time
    start_time = time.time()
    timer_duration = 120
    score = 0

    # Create a label to display the timer
    global timer_label
    timer_label = Label(button_game_frame, text=f"Time left: \n {timer_duration} secs", font = ("Helvetica",8))
    timer_label.place(x=3,y = 100)


    # Create a label to display score
    global score_label
    score_label = Label(button_game_frame, text=f"Score: {score}", font = ("Helvetica",8))
    score_label.place(x=3, y=140)
  

    # Define our deck
    shapes = ["ovals","squiggles","diamonds"]
    colors = ["red","purple","green"]
    numbers = ["one","two","three"]
    shadings = ["solid","striped","outlined"]

    # makes a deck with all possible shape/color/number/shading combinations
    for shape in shapes:
        for color in colors:
            for number in numbers:
                for shading in shadings: 
                    deck.append(f'{number}_{shading}_{color}_{shape}')

    # Choosing which 12 cards will first be displayed
    for i in range(12):
        card = random.choice(deck)
        deck.remove(card)
        card_name_array.append(card)
        card_image = resize_cards(f'Set_Cards/{card}.png')
        card_array.append(card_image)
        button = Button(card_game_frame, image=card_array[i], bg = "#ADD8E6", state="normal",
                         activebackground="red")
        # Placing the cards in a 4 x 3 grid
        button.grid(row=(int(i / 4)), column=(i % 4), padx=3, pady=3)
        button_array.append(button)

    # Action for when one of the cards is selected/deselected
    button_array[0].config(command=lambda: select_button(0))
    button_array[1].config(command=lambda: select_button(1))
    button_array[2].config(command=lambda: select_button(2))
    button_array[3].config(command=lambda: select_button(3))
    button_array[4].config(command=lambda: select_button(4))
    button_array[5].config(command=lambda: select_button(5))
    button_array[6].config(command=lambda: select_button(6))
    button_array[7].config(command=lambda: select_button(7))
    button_array[8].config(command=lambda: select_button(8))
    button_array[9].config(command=lambda: select_button(9))
    button_array[10].config(command=lambda: select_button(10))
    button_array[11].config(command=lambda: select_button(11))

    # keeps everything updating as long as the game is running
    while game_running:
        loop()
        root.update()
        update_timer() 
        root.title(f'Set Game - {len(deck)} Cards Left') 
        score_label.config(text=f"Score: {score}")

    root.title(f'Set Game - {len(deck)} Cards Left')

# end def

def update_timer():
    # updates the time so that the time remaining for the game can be displayed
    global game_running, score

    remaining_time = timer_duration - (time.time() - start_time)
    if remaining_time > 0:
        timer_label.config(text=f"Time left: \n{int(remaining_time)} secs")
        button_game_frame.after(1000, update_timer)
    else:
        timer_label.config(text="Time up!")
        if score > 0:
            change_win_game()

        game_running = False
# end def

def resize_cards(card):
    # Resize the cards to fit the screen fom the original image
    our_card_img = Image.open(card)
    our_card_resize_image = our_card_img.resize((50,68))
    our_card_image = ImageTk.PhotoImage(our_card_resize_image)
    return our_card_image
# end def

#create a list to store the states of the buttons
button_states=["normal"] * 12

def select_button(button_idx):
    # checks if button has already been selected; if yes, then deselect it; if no, then select it
    global active_cards
    if button_idx in active_cards:
        active_cards.remove(button_idx)
    else:
        active_cards.append(button_idx)
# end def


def check_all_or_none(collection):
    # Checks whether the three selected cards are a set of not 
    if collection[0]==collection[1]==collection[2] or collection[0]!=collection[1]!=collection[2]:
        return True
    else:
        return False
# end def 
    
def replace(active_cards):
    # replaces the cards after they've been removed for being a set
    global score
    for i in range(3):
        card = random.choice(deck)
        deck.remove(card)
        card_name_array[active_cards[i]]=(card)
        card_image = resize_cards(f'Set_Cards/{card}.png')
        card_array[active_cards[i]]=(card_image)
        button_array[active_cards[i]].configure(image=card_array[active_cards[i]], state="active")
    

def add(): 
    # chooses 3 random cards to replace when "New Cards" button is pressed and removes a point from score
    global score
    start_range = 0
    end_range = 11
    num_to_choose = 3
    random_numbers = random.sample(range(start_range,end_range+1), num_to_choose)
    
    for i in range(3):
        card = random.choice(deck)
        deck.remove(card)
        card_name_array[random_numbers[i]]=(card)
        card_image = resize_cards(f'Set_Cards/{card}.png')
        card_array[random_numbers[i]]=(card_image)
        button_array[random_numbers[i]].configure(image=card_array[random_numbers[i]], state="active")
    
    score -= 1
# end def

def end_game():
    # ends the game and graphics display if end game button is pressed
    global end_sign, game_running
    end_sign = True
    game_running = False
    root.quit()
# end def    

def loop():
    # code that checks whether three cards have been selected and if they're a set
    global score, game_running
    for i in range(12):
        if i in active_cards:
            button_array[i]["state"] = "active"
        else:
            button_array[i]["state"] = "normal"

    if len(active_cards) == 3:
        numbers = list(map(lambda card_idx: card_name_array[card_idx].split("_")[0]   ,active_cards))
        shadings = list(map(lambda card_idx: card_name_array[card_idx].split("_")[1]   ,active_cards))
        colors = list(map(lambda card_idx: card_name_array[card_idx].split("_")[2]   ,active_cards))
        shapes = list(map(lambda card_idx: card_name_array[card_idx].split("_")[3]   ,active_cards))

        if check_all_or_none(numbers) and check_all_or_none(shadings) and check_all_or_none(colors) and check_all_or_none(shapes):
            print("You found a set")
            replace(active_cards)
            active_cards.clear()
            button_states=["normal"] * 12
            score+=1
    
        else:
            print("That was not a set")
            active_cards.clear()
            button_states=["normal"] * 12

    return
# end def 

# sets up the main GUI root
root = Tk()
root.title('Set Game - Card Deck')
root.geometry("320x240")
root.configure(background="#ADD8E6")

# defining the different frames for the game

global start_frame
# start_frame is the welcome frame (buttons: start game, instructions)
start_frame = Frame(root, width = horizontal_size, height = vertical_size, bg ="#ADD8E6")
start_frame.pack()

label_intro = Label(start_frame, text = "Hello, Welcome to Set.\n \n Find 10 sets in 2 minutes to win a prize! \n \n Press 'Instructions' to learn the rules.", font = ("Helvetica", 12), bg = "#ADD8E6")
label_intro.place(x = 60, y = 30)

start_game_button = Button(start_frame, text = "Start Playing", font = ("Helvetica", 10), command = start)
start_game_button.place(x=120,y=150)
instructions_button = Button(start_frame, text = "Instructions", font = ("Helvetica", 10), command = change_to_instruction_screens)
instructions_button.place(x=125,y=200)

global rules_frame
# rules_frame has the rules of the game (buttons: see examples, go back)
rules_frame = Frame(root, width = horizontal_size, height = vertical_size, bg ="#ADD8E6" )
rules_frame.pack()

rules_label = Label(rules_frame, text = "Rules for Set", font = ("Helvetica", 10), bg = "#ADD8E6")
rules_label.place(x = 120, y = 30)
rules1_label = Label(rules_frame, text = "- a SET consists of 3 cards", font = ("Helvetica", 8), bg = "#ADD8E6")
rules1_label.place(x = 100, y = 60)
rules2_label = Label(rules_frame, text = "- each of the cards' features (looked at one-by-by) \n must be the same OR different on each card", font = ("Helvetica", 8), bg = "#ADD8E6")
rules2_label.place(x = 40, y = 90)
rule3_label = Label(rules_frame, text = "- i.e. shape must either be the same on \n all 3 cards OR different on all 3 cards", font = ("Helvetica", 8), bg = "#ADD8E6")
rule3_label.place(x = 60, y = 130)

see_ex_button = Button(rules_frame, text="See Examples", font=("Helvetica", 10), command = see_example)
see_ex_button.place(x=120,y=180)
go_back_button = Button(rules_frame, text="Back", font=("Helvetica", 10), command = change_display_screens)
go_back_button.place(x=150,y=210)

global examples_frame
# examples_frame shows examples of a set (buttons: go back)
examples_frame = Frame(root, width = horizontal_size, height = vertical_size, bg = "#ADD8E6")
examples_frame.pack()

example_set_open = Image.open("Set_Cards/example_sets.jpg")
example_set_resize = example_set_open.resize((150,180))
example_set_photo = ImageTk.PhotoImage(example_set_resize)
example_label = tk.Label(examples_frame,image=example_set_photo)
example_label.place(x=90,y=10)

go_back_button2 = Button(examples_frame, text="Back", font=("Helvetica", 10), command = change_display_screens)
go_back_button2.place(x=130,y=200)


global game_frame
# game_frame is the screen once the game starts with cards (buttons: add cards, end game, new game)
game_frame = Frame(root, width = horizontal_size, height = vertical_size, bg = "#ADD8E6")
game_frame.pack()

# creating 2 separate frames in the game frame; 1 for the cards and 1 for the action buttons
card_game_frame = Frame(game_frame, width = 250, height = 240, bg = "#ADD8E6")
card_game_frame.place(x=0,y=0)
button_game_frame = Frame(game_frame, width = 70, height = 240, bg = "#ADD8E6")
button_game_frame.place(x = 250, y = 0)

# Creating buttons for the game frame
new_game_button = Button(button_game_frame, text="New Game", font=("Helvetica", 8), command = start)
new_game_button.place(x=3,y=10)
add_button = Button(button_game_frame, text="New Cards", font=("Helvetica", 8), command = add)
add_button.place(x=3,y=40)
end_button = Button(button_game_frame,text="End Game", font=("Helvetica", 8), command = end_game)
end_button.place(x=3,y=70)


global end_frame
# end_frame is the frame that displays at the end after user wins game
end_frame = Frame(root, width = horizontal_size, height = vertical_size, bg = "#ADD8E6")
end_frame.pack()

congrats_label = Label(end_frame, text="Congrats! You won! \n Press the button to dispense candy!", font=("Helvetica", 8), bg = "#ADD8E6")
congrats_label.place(x=60,y=70)

def main():
    # code's main loop
    global game_running, end_sign
    change_display_screens()
    root.update()
    print('after turn on')
    print(game_running)
    root.mainloop()
 
main()