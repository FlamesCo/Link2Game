
import urllib.request
import sys
import os
def link2game(url):
    """
    This function takes a URL and turns it into a game ROM.
    """
    
    # Get the data from the URL
    data = urllib.request.urlopen(url).read()
    
    # Convert the data into a game ROM
    rom = data.decode("hex")
    
    return rom

    # ask where the user wants to save the rom too
    try :
        save_location = input("Where do you want to save the ROM? ")
        save_location = save_location + ".nes"
        # save the rom
        with open(save_location, "wb") as f:
            f.write(rom)
    except :
        print("Error: Could not save the ROM.")
        ## package it for the nintendo ds
        rom = rom.encode("hex")
        rom = rom.upper()
        rom = rom.replace("\n", "")
        rom = rom.replace(" ", "")
       ## use gptj to generate a rom encoded to .nes format 
        hf.gptj.gptj(rom, "rom.nes")