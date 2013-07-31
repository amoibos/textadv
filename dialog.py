import textwrap
import os
import platform

wrapper = textwrap.TextWrapper(width=40, replace_whitespace=False)

def cls():
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    else:
        print("Unknown OS")


def msg(box, message_block):
        if box == "battle":
            box_width = 50
            box_symbol_horizontal = "*"
            box_symbol_side = "!   "
        elif box == "text":
            box_width = 50
            box_symbol_horizontal = "-"
            box_symbol_side = "|   "
        elif box == "error":
            box_width = 50
            box_symbol_horizontal = "!"
            box_symbol_side = "!   "
        else:
            box_width = 50
            box_symbol_horizontal = "-"
            box_symbol_side = "|   "            



        #cls()
        print(box_symbol_horizontal * box_width)  # outer horizontal border
        print(box_symbol_side)

        if type(message_block) == str: 
            wraped_text = wrapper.wrap(message_block)  
            # wrap long string into a list of short ones
            for string in wraped_text:
                print("{0} {1}".format(box_symbol_side, string))

        elif type(message_block) == tuple:
            for obj in message_block:  
            # loop through objects of message_block and check type
                if type(obj) == str:
                    wraped_text = wrapper.wrap(obj)
                    # wrap long string into a list of short ones
                    for string in wraped_text:
                        print("{0} {1}".format(box_symbol_side, string))
                elif type(obj) in (tuple, list):  #if obj is tuple go through every tuple       
                    for phrase in obj:
                        wraped_text = wrapper.wrap(phrase)
                        for string in wraped_text:
                            print("{0} {1}".format(box_symbol_side, string))

        print(box_symbol_side)  # outer symbols
        print(box_symbol_horizontal * box_width)


def line(argument):
    if argument == "small":
        print("-" * 20)
    if argument == "normal":
        print("-" * 30)
    if argument == "big":
        print("-" * 40)
    if argument == "double":
        print("=" * 30)






