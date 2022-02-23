import tkinter as tk
import os
import subprocess
import threading

def compile_terminal_command(terminal_command, last_line_index) :
    print(terminal_command)
    if terminal_command == "cls":
        terminal_listbox.delete(0,tk.END)
    elif terminal_command == "exit":
        root.destroy()
    elif "title" in terminal_command :
        terminal_command = terminal_command.replace('title'," ")
        root.title(terminal_command)
    else:
        command_summary = terminal_command.split(' ') # Split the command and args.
        os.environ["PYTHONUNBUFFERED"] = "1" # MAKE SURE THE PREVIOUS OUTPUT IS NOT RECIEVED
        result = subprocess.run(command_summary, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell = True, env = os.environ)
        output = result.stdout
        output_lines = output.splitlines()
        for k in output_lines :
            terminal_listbox.insert(last_line_index, k)
            last_line_index += 1 
        return

def refresh_terminal(backspace = False) :
    # refreshes the terminal when a change is done to terminal by the user.
    global terminal_text
    
    if terminal_text != '>> ' or backspace :
        terminal_listbox.delete(tk.END)
    terminal_listbox.insert(tk.END, terminal_text)
    return

def append_to_terminal_text(text) :
    # can append a single character or more to the terminal
    global terminal_text
    
    terminal_listbox.delete(tk.END)
    terminal_text = terminal_text + text
    terminal_listbox.insert(tk.END, terminal_text)
    terminal_listbox.yview_moveto(1)
    return

def terminal_enter_key_callback() :
    global terminal_text
    
    # The thread that compiles the output is run in background to make sure it does not hang the 
    # program or does not stop the terminal incase the output is taking time to be generated.
    compiler_thread = threading.Thread(target = compile_terminal_command, args = (terminal_text[3 : ], terminal_listbox.size()))
    compiler_thread.daemon = True
    compiler_thread.start()
    
    terminal_text = '>> ' # Resetting the terminal_text variable that stores the text of the current line of the terminal.
    terminal_listbox.insert(tk.END, terminal_text) # Insert the terminal text(basically a new line in this case) to the terminal listbox.
    terminal_listbox.yview_moveto(1) # scrolls down the listbox down to the very last.
    return

def type_to_terminal(string) :
    # types a given string automatically to the terminal.
    for k in string :
        append_to_terminal_text(k)
    
    terminal_listbox.yview_moveto(1)
    return

def terminal_backspace_callback() :
    # callback for backspace key erases the last character.
    global terminal_text
    global terminal_no
    if len(terminal_text) > 3 :
        terminal_text = terminal_text[ : -1]
    refresh_terminal(backspace = True)
    return

root = tk.Tk()
root.title('Command line boter')
root.geometry('677x343')

# Making a frame, this terminal frame can be packed or used as a toplevel window instead.
terminal = tk.Frame(root, bg = 'black')

# Initializing a listbox to act as terminal with bg and fg of your own choice.
# NOTE:  in the listbox to make it so the selection of listbox items is not visible
# I have changed the highlight color and select color to background color and also have set
# the active style i.e. the style used to display a selection to tk.NONE, and have also set
# the highlight thickness to 0.
terminal_listbox = tk.Listbox(terminal, bg = 'black', fg = 'white', highlightcolor = 'black', highlightthickness = 0, selectbackground = 'black', activestyle = tk.NONE)
terminal_scrollbar = tk.Scrollbar(terminal)
terminal_scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

# packing and stuff.
terminal_listbox.pack(expand = True, fill = tk.BOTH)
terminal.pack(expand = True, fill = tk.BOTH)

# Inserting the copyright thingy.
terminal_listbox.insert(tk.END, 'Create by Nimacpp ( github.com/nimacpp )')
terminal_listbox.insert(tk.END, '© Copyright Nima cpp')

# Intializes the terminal text for the first line.
terminal_text = '>> '

# Assigns a scrollbar to the terminal.
terminal_listbox.config(yscrollcommand = terminal_scrollbar.set)
terminal_scrollbar.config(command = terminal_listbox.yview)

# THE FIRST EVER INSERTED ITEM DOES NOT APPEAR SO THIS IS A BUFFER ITEM TO FILL THAT SPOT
terminal_listbox.insert(tk.END, '')
terminal_listbox.insert(tk.END, '')

append_to_terminal_text('') # Buffer.

# SETTING UP BINDINGS FOR ENTER AND BACKSPACE CALLBACKS WITH THEIR RESPECTIVE KEYS
terminal_listbox.bind('<Return>', lambda x : terminal_enter_key_callback())
terminal_listbox.bind('<BackSpace>', lambda x : terminal_backspace_callback())

# SETTING UP KEYBOARD INPUT FOR A LISTBOX HARDCODINGLY.
terminal_listbox.bind('a', lambda x : append_to_terminal_text('a'))
terminal_listbox.bind('b', lambda x : append_to_terminal_text('b'))
terminal_listbox.bind('c', lambda x : append_to_terminal_text('c'))
terminal_listbox.bind('d', lambda x : append_to_terminal_text('d'))
terminal_listbox.bind('e', lambda x : append_to_terminal_text('e'))
terminal_listbox.bind('f', lambda x : append_to_terminal_text('f'))
terminal_listbox.bind('g', lambda x : append_to_terminal_text('g'))
terminal_listbox.bind('h', lambda x : append_to_terminal_text('h'))
terminal_listbox.bind('i', lambda x : append_to_terminal_text('i'))
terminal_listbox.bind('j', lambda x : append_to_terminal_text('j'))
terminal_listbox.bind('k', lambda x : append_to_terminal_text('k'))
terminal_listbox.bind('l', lambda x : append_to_terminal_text('l'))
terminal_listbox.bind('m', lambda x : append_to_terminal_text('m'))
terminal_listbox.bind('n', lambda x : append_to_terminal_text('n'))
terminal_listbox.bind('o', lambda x : append_to_terminal_text('o'))
terminal_listbox.bind('p', lambda x : append_to_terminal_text('p'))
terminal_listbox.bind('q', lambda x : append_to_terminal_text('q'))
terminal_listbox.bind('r', lambda x : append_to_terminal_text('r'))
terminal_listbox.bind('s', lambda x : append_to_terminal_text('s'))
terminal_listbox.bind('t', lambda x : append_to_terminal_text('t'))
terminal_listbox.bind('u', lambda x : append_to_terminal_text('u'))
terminal_listbox.bind('v', lambda x : append_to_terminal_text('v'))
terminal_listbox.bind('w', lambda x : append_to_terminal_text('w'))
terminal_listbox.bind('x', lambda x : append_to_terminal_text('x'))
terminal_listbox.bind('y', lambda x : append_to_terminal_text('y'))
terminal_listbox.bind('z', lambda x : append_to_terminal_text('z'))
terminal_listbox.bind('A', lambda x : append_to_terminal_text('A'))
terminal_listbox.bind('B', lambda x : append_to_terminal_text('B'))
terminal_listbox.bind('C', lambda x : append_to_terminal_text('C'))
terminal_listbox.bind('D', lambda x : append_to_terminal_text('D'))
terminal_listbox.bind('E', lambda x : append_to_terminal_text('E'))
terminal_listbox.bind('F', lambda x : append_to_terminal_text('F'))
terminal_listbox.bind('G', lambda x : append_to_terminal_text('G'))
terminal_listbox.bind('H', lambda x : append_to_terminal_text('H'))
terminal_listbox.bind('I', lambda x : append_to_terminal_text('I'))
terminal_listbox.bind('J', lambda x : append_to_terminal_text('J'))
terminal_listbox.bind('K', lambda x : append_to_terminal_text('K'))
terminal_listbox.bind('L', lambda x : append_to_terminal_text('L'))
terminal_listbox.bind('M', lambda x : append_to_terminal_text('M'))
terminal_listbox.bind('N', lambda x : append_to_terminal_text('N'))
terminal_listbox.bind('O', lambda x : append_to_terminal_text('O'))
terminal_listbox.bind('P', lambda x : append_to_terminal_text('P'))
terminal_listbox.bind('Q', lambda x : append_to_terminal_text('Q'))
terminal_listbox.bind('R', lambda x : append_to_terminal_text('R'))
terminal_listbox.bind('S', lambda x : append_to_terminal_text('S'))
terminal_listbox.bind('T', lambda x : append_to_terminal_text('T'))
terminal_listbox.bind('U', lambda x : append_to_terminal_text('U'))
terminal_listbox.bind('V', lambda x : append_to_terminal_text('V'))
terminal_listbox.bind('W', lambda x : append_to_terminal_text('W'))
terminal_listbox.bind('X', lambda x : append_to_terminal_text('X'))
terminal_listbox.bind('Y', lambda x : append_to_terminal_text('Y'))
terminal_listbox.bind('Z', lambda x : append_to_terminal_text('Z'))
terminal_listbox.bind('1', lambda x : append_to_terminal_text('1'))
terminal_listbox.bind('2', lambda x : append_to_terminal_text('2'))
terminal_listbox.bind('3', lambda x : append_to_terminal_text('3'))
terminal_listbox.bind('4', lambda x : append_to_terminal_text('4'))
terminal_listbox.bind('5', lambda x : append_to_terminal_text('5'))
terminal_listbox.bind('6', lambda x : append_to_terminal_text('6'))
terminal_listbox.bind('7', lambda x : append_to_terminal_text('7'))
terminal_listbox.bind('8', lambda x : append_to_terminal_text('8'))
terminal_listbox.bind('9', lambda x : append_to_terminal_text('9'))
terminal_listbox.bind('0', lambda x : append_to_terminal_text('0'))
terminal_listbox.bind('.', lambda x : append_to_terminal_text('.'))
terminal_listbox.bind(':', lambda x : append_to_terminal_text(':'))
terminal_listbox.bind('!', lambda x : append_to_terminal_text('!'))
terminal_listbox.bind('-', lambda x : append_to_terminal_text('-'))
terminal_listbox.bind('_', lambda x : append_to_terminal_text('_'))
terminal_listbox.bind('?', lambda x : append_to_terminal_text('?'))
terminal_listbox.bind('=', lambda x : append_to_terminal_text('='))
terminal_listbox.bind('(', lambda x : append_to_terminal_text('('))
terminal_listbox.bind(')', lambda x : append_to_terminal_text(')'))
terminal_listbox.bind('<slash>', lambda x : append_to_terminal_text('/'))
terminal_listbox.bind('<backslash>', lambda x : append_to_terminal_text('\\'))
terminal_listbox.bind('<space>', lambda x : append_to_terminal_text(' '))
# Not all keys have been binded here as its a demonstration but as per need all can be binded.

root.mainloop()
