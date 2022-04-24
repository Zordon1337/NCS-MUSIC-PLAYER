import dearpygui.dearpygui as dpg
import webbrowser
import sys
import pygame

pygame.mixer.init()

def Fearless():

    pygame.mixer.music.load("http://azordon.cf/music/fearless.wav")
    pygame.mixer.music.play()

def cuagain():
    pygame.mixer.music.load("http://azordon.cf/music/cuagain.wav")
    pygame.mixer.music.play()
    
def git():
    webbrowser.open("github.com/zordon1337")
    
def secret():
    webbrowser.open("https://tinyurl.com/bobuxgenerator222")
    
def ONON():
    pygame.mixer.music.load("http://azordon.cf/music/ONON.wav")
    pygame.mixer.music.play() 
    
def infectious():
    pygame.mixer.music.load("http://azordon.cf/music/Infectious.wav")
    pygame.mixer.music.play() 

def whywelose():
    pygame.mixer.music.load("http://azordon.cf/music/whyweloss.wav")
    pygame.mixer.music.play() 
    
def candyland():
    pygame.mixer.music.load("http://azordon.cf/music/candyland.wav")
    pygame.mixer.music.play() 
    
def Flashes():
    pygame.mixer.music.load("http://azordon.cf/music/Flashes.wav")
    pygame.mixer.music.play() 

def Royality():
    pygame.mixer.music.load("http://azordon.cf/music/Royalty.wav")
    pygame.mixer.music.play() 

def myheart():
    pygame.mixer.music.load("http://azordon.cf/music/myheart.wav")
    pygame.mixer.music.play() 
    
def Dreams():
    pygame.mixer.music.load("http://azordon.cf/music/Dreams.wav")
    pygame.mixer.music.play() 
    
def perfect10():
    pygame.mixer.music.load("http://azordon.cf/music/perfect10.wav")
    pygame.mixer.music.play() 

def howling():
    pygame.mixer.music.load("http://azordon.cf/music/howling.wav")
    pygame.mixer.music.play() 
    
def skyhigh():
    pygame.mixer.music.load("http://azordon.cf/music/skyhigh.wav")
    pygame.mixer.music.play() 
    
def hope():
    pygame.mixer.music.load("http://azordon.cf/music/hope.wav")
    pygame.mixer.music.play() 
    
def high():
    pygame.mixer.music.load("http://azordon.cf/music/high.wav")
    pygame.mixer.music.play() 
    
def Eclipse():
    pygame.mixer.music.load("http://azordon.cf/music/Eclipse.wav")
    pygame.mixer.music.play() 
def nova():
    pygame.mixer.music.load("http://azordon.cf/music/nova.wav")
    pygame.mixer.music.play() 
    
def Hellcat():
    pygame.mixer.music.load("http://azordon.cf/music/hellcat.wav")
    pygame.mixer.music.play()
    
def Earth():
    pygame.mixer.music.load("http://azordon.cf/music/earth.wav")
    pygame.mixer.music.play()
    
def undone():
    pygame.mixer.music.load("http://azordon.cf/music/undone.wav")
    pygame.mixer.music.play()
  
def stop():
    pygame.mixer.music.stop() 
    

dpg.create_context()

dpg.create_viewport()

dpg.setup_dearpygui()

with dpg.window(label="NCS MUSIC PLAYER - 1.3", pos=(425, 150), width=480, height=480) as main_window:
    
    dpg.add_text("Select music that you want play")
    dpg.add_button(label="Lost Sky - Fearless pt.II", callback=Fearless)
    dpg.add_button(label="Cartoon - C U Again feat. Mikk Mäe", callback=cuagain)
    dpg.add_button(label="Tobu - Infectious", callback=infectious)
    dpg.add_button(label="Cartoon - On & On (feat. Daniel Levi)", callback=ONON)
    dpg.add_button(label="Cartoon - Why We Lose (feat. Coleman Trapp)", callback=whywelose)
    dpg.add_button(label="Tobu - Candyland [NCS Release]", callback=candyland)
    dpg.add_button(label="NIVIRO - Flashes [NCS Release]", callback=Flashes)
    dpg.add_button(label="Different Heaven & EH!DE - My Heart [NCS Release]", callback=myheart)
    dpg.add_button(label="Unknown Brain - Perfect 10 (feat. Heather Sommer)", callback=perfect10)
    dpg.add_button(label="Egzod & Maestro Chives - Royalty (ft. Neoni) [NCS Release]", callback=Royality)
    dpg.add_button(label="Lost Sky - Dreams", callback=Dreams)
    dpg.add_button(label="Elektronomia - Sky High [NCS Release]", callback=skyhigh)
    dpg.add_button(label="Cartoon - Howling (Ft. Asena) [NCS Release]", callback=howling)   
    dpg.add_button(label="Tobu - Hope [NCS Release]", callback=hope)   
    dpg.add_button(label="JPB - High [NCS RELEASE]", callback=high)
    dpg.add_button(label="Jim Yosef - Eclipse [NCS Release]", callback=Eclipse)
    dpg.add_button(label="Desmeon - Undone (feat. Steklo) [NCS Release]", callback=undone)
    dpg.add_button(label="Ahrix - Nova", callback=nova)
    dpg.add_button(label="Earth - K-391", callback=Earth)
    dpg.add_button(label="DESMEON - HELLCAT [NCS RELEASE]", callback=Hellcat)
    dpg.add_text("Other buttons :)")
    dpg.add_button(label="Stop playing music", callback=stop)   
    dpg.add_button(label="Github", callback=git)
    dpg.add_text("Created by Zordon1337")
    
with dpg.window(label="CLICK THIS <<TRUST ME>>", width=240, height=240) as main_window2:
    
    dpg.add_text("CLICK HERE")
    dpg.add_button(label="<<CLICK ME>>", callback=secret)


dpg.show_viewport()

dpg.start_dearpygui()

dpg.destroy_context()