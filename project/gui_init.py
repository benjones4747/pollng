import tkinter as tk
import math

def welcome():
    def close_tkinter_window():
        root.destroy()
    def initialize():
        global mode
        mode = "single player"
        root.destroy()

    def two_player():
        global mode
        mode = "two player"
        Goal = tk.StringVar()
        goal_entry = tk.Entry(frame, textvariable = Goal)
        goal_entry.grid(column = 2, row = 5, sticky = "we")
        goal_entry.focus()
        def submit(*args):
            try:
                global goal
                goal = int(Goal.get())
                root.destroy()
            except ValueError:
                pass
        root.bind('<Return>',submit)
    from random import shuffle, randrange

    def instructions():
        displayed_text = tk.Text(frame, fg = 'black',bg = secondary_background_colour,state = "normal")
        Instructions = open('instructions.txt')
        instructions = Instructions.read()
        Instructions.close()
        displayed_text.insert(1.0,instructions)
        displayed_text.grid(column = 4, row = 1 , rowspan = 5 , sticky='we' )
        displayed_text['state'] = 'disabled'
        
    def show_credits():
        displayed_text = tk.Text(frame, fg = 'black',bg = secondary_background_colour,state = "normal")
        Game_Credits = open('credits.txt')
        game_credits = Game_Credits.read()#'credits' is a built in python function so game_credits had to be used instead
        Game_Credits.close()
        displayed_text.insert(1.0,game_credits)
        displayed_text.grid(column = 4, row = 1 , rowspan = 5 , sticky='we' )
        displayed_text['state'] = 'disabled'
        
    global mode
    mode = '' #this prevents an error if the window is closed manually
    root = tk.Tk()
    
    main_background_colour = '#8e8e8e'
    secondary_background_colour = '#ffffff'
    
    root.title("Polling Aggregator - 0.1.1")
    root.configure(background=main_background_colour)
    frame = tk.Frame(root, bg=main_background_colour)
    frame.grid(column=2, row=0)
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)

    tk.Label(frame, text="Welcome to Polling Aggregator 0.1.1", bg = main_background_colour).grid(column = 1, row = 1,columnspan = 2)
    tk.Label(frame, text="Please select an option from below:", bg = main_background_colour).grid(column = 1, row = 2,columnspan = 2)
    tk.Button(frame, text="Initialize", command=initialize, bg = secondary_background_colour).grid(column=1, row=3,sticky= "we")
    tk.Button(frame, text="See the Instructions", command=instructions, bg = secondary_background_colour).grid(column=1, row=4,sticky= "we")
    tk.Button(frame, text="See the Credits", command=show_credits, bg = secondary_background_colour).grid(column=2, row=4, sticky= "we")
    for child in frame.winfo_children(): child.grid_configure(padx=5, pady=5)#space everything out
    
    root.mainloop()
    del frame
    Mode = mode #store the value of the global variable in a local variable
    del mode #delete the global variable
    return Mode #return the local variable

welcome()