import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile
import time
import random


with open("configuracion.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

@bot.command()
async def vitrina(ctx,   keko, *, keko2):
    await ctx.message.delete()
    await ctx.send("Generando expositor de habbo...", delete_after=0)
    time.sleep(3)
    
    response = requests.get(f"https://www.habbo.es/api/public/users?name={keko}")
    response1 = requests.get(f"https://www.habbo.es/api/public/users?name={keko2}")
   
    
    habbo = response.json()['figureString']
    habbo1 = response1.json()['figureString']
   

   
    

    
    
   
    
    url = "https://www.habbo.com/habbo-imaging/avatarimage?size=m&figure="+ habbo +"&action=none&direction=2&head_direction=2&gesture=std&size=m"
    img1 = Image.open(io.BytesIO(requests.get(url).content))
    img1 = img1.resize((64,110), Image.Resampling.LANCZOS)#tamaño del keko 1

    url1 = "https://www.habbo.com/habbo-imaging/avatarimage?size=l&figure="+ habbo1 +"&action=none&direction=2&head_direction=2&gesture=std&size=m"
    habbol = Image.open(io.BytesIO(requests.get(url1).content))
    habbol = habbol.resize((64,110), Image.Resampling.LANCZOS)#tamaño del keko 2
    
    
    


    
    


    

   

    

    
    
    



    img2 = img1.copy()
    
    
    ###

    


    cristal = Image.open(r"imagenes/cristal.png").convert("RGBA") #imagen
    img1 = cristal.resize((138,295), Image.Resampling.LANCZOS)#tamaño de la cristal


    ###
  
    ###
    almo = Image.open(r"imagenes/almohadas.png").convert("RGBA") #imagen
    img1 = almo.resize((138,295), Image.Resampling.LANCZOS)#tamaño de la almo

    ###
    fondoazul = Image.open(r"imagenes/fondoazul.png").convert("RGBA") #imagen
    img1 = fondoazul.resize((138,295), Image.Resampling.LANCZOS)#tamaño de la almo

    
    

 
   
    
    
    
    
    img1.paste(fondoazul,(0,0), mask = fondoazul) #Posicion de la fondoazul
    
    img1.paste(almo,(0,0), mask = almo) #Posicion de la almo
    
    img1.paste(habbol,(40,140), mask = habbol) #Posicion del keko 2

    img1.paste(img2,(14,150), mask = img2) #Posicion del keko 1
    
    img1.paste(cristal,(0,0), mask = cristal) #Posicion de la cristal
  

    
    ### 

    
    
   
    
   ###
   
    
   
    ###
    
   
 
    
    
  ####
   
  ###
    




    

    
    
    
   
    
   
       


      
    
       
      

      
    
       
            
        
        
        
       
        
    with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)

        await ctx.send(file=discord.File(fp=image_binary, filename='keko.png'))
         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])   