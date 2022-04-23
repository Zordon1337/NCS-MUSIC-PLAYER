import dearpygui.dearpygui as dpg
import webbrowser
import sys
import pygame

pygame.mixer.init()

def Fearless():

    pygame.mixer.music.load("./music/fearless.wav")
    pygame.mixer.music.play()

def cuagain():
    pygame.mixer.music.load("./music/cuagain.wav")
    pygame.mixer.music.play()
    
def git():
    webbrowser.open("github.com/zordon1337")
    
def secret():
    webbrowser.open("https://tinyurl.com/bobuxgenerator222")
    
def ONON():
    pygame.mixer.music.load("./music/ONON.wav")
    pygame.mixer.music.play() 
    
def infectious():
    pygame.mixer.music.load("./music/Infectious.wav")
    pygame.mixer.music.play() 

def whywelose():
    pygame.mixer.music.load("./music/whyweloss.wav")
    pygame.mixer.music.play() 
    

dpg.create_context()

dpg.create_viewport()

dpg.setup_dearpygui()

with dpg.window(label="NCS MUSIC PLAYER - Beta v0.2", pos=(425, 150), width=480, height=480) as main_window:
    
    dpg.add_text("Select music that you want play")
    dpg.add_button(label="Lost Sky - Fearless pt.II", callback=Fearless)
    dpg.add_button(label="Cartoon - C U Again feat. Mikk Mäe", callback=cuagain)
    dpg.add_button(label="Tobu - Infectious", callback=infectious)
    dpg.add_button(label="Cartoon - On & On (feat. Daniel Levi) [", callback=ONON)
    dpg.add_button(label="Cartoon - Why We Lose (feat. Coleman Trapp)", callback=whywelose)
    dpg.add_button(label="Github", callback=git)
    dpg.add_text("Created by Zordon1337")
    
with dpg.window(label="CLICK THIS <<TRUST ME>>", width=240, height=240) as main_window2:
    
    dpg.add_text("CLICK HERE")
    dpg.add_button(label="<<CLICK ME>>", callback=secret)


dpg.show_viewport()

dpg.start_dearpygui()

dpg.destroy_context()