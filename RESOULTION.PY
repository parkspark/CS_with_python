import os

def change_resolution(width, height):
    os.system(f'nircmd setdisplay {width} {height} 32')

change_resolution(1920, 1080)
