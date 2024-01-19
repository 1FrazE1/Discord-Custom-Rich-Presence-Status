#FRAZE#FRAZE#FRAZE#FRAZE#FRAZE#FRAZE#FRAZE#FRAZE#FRAZE#FRAZE#FRAZE#FRAZE

#You need those libs:
    #pip install pypresence
    #pip install time

from pypresence import Presence
from time import time
 
RPC = Presence("id") #Your ID
btns = [ #buttons
    { S
        "label": "your name",  #name of button 1
        "url": "your url" #your URL
    }, 
    {
        "label": "your name",  #name of button 2
        "url": "your url" #your URL
    } 
] 

RPC.connect()
RPC.update( 
    state="your lower text",  #lower
    details="your upper text",  #upper
    start=time(), #start time
    buttons=btns,
    large_image="name1", #name of large image
    small_image="name2", #name of small image
    large_text="your text", #large image text
    small_text="your text" #small image text
)
input()
#FRAZE#FRAZE#FRAZE#FRAZE#FRAZE#FRAZE#FRAZE#FRAZE#FRAZE#FRAZE#FRAZE#FRAZE
