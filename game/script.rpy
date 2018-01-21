# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define myname = ""
define me = Character("[myname]")
define tom = Character("Tom")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bedroom
    with fade
    
    "Saturday Morning"
    
    me "I'm late!!!"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    scene classroom:
        zoom 1.75
        
    with fade
    
    pause(2)
    
    show tom:
        zoom 2

    # These display lines of dialogue.

    tom "Hi Good morning!"

    tom "Nice to Meet you"
    
    menu:
        me "I think it remember him..."
        
        "Hi, Tom":
            pass
            
        "Hi Stranger?":
            pass
            
    tom "Hi I'm Tom, Welcome to CoderDojo!"
    tom "What is your name?"
    
    python:
        myname = renpy.input("Input your name")
        myname = myname.strip()
        
    me "My name is [myname]"
    
    show tom:
        ease .1 zoom 5
    
    tom "HI [myname]!!!"
    
    show tom:
        ease .2 zoom 5 xoffset -600
        
    tom "VERY NICE TO MEET YOU!!!!"

    # This ends the game.

    return
