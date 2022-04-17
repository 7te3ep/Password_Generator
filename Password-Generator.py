

                # Random Username Generator Advanced 

# Preset
import random
import os

os.system('clear')

# Liste of potentially generated characters
alphabet = ["a","b","c", "d", "e", "f", "g" , "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]
# longueurlist = len(alphabet)
longueurlist= 25
# User settings variables
print("                                  PASSWORD GENERATOR\n\n")
nombredefois = int(input("Combien de tentatives ? (only int) "))
longueur  = int(input("La longueur de ton mot de passe est ? (only int) "))
number = input("Tu veux des nombres dedans ? y/n ")
if number == "y" : 
    alphabet.extend(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    longueurlist += 10
    
special = input("Tu veux des characteres speciaux dedans ? y/n ")
if special == "y" : 
    alphabet.extend(["*", "<", ">", ":", ".", ",", '"', "'", ")", "("])
    longueurlist += 10

maj = input("Tu veux des majuscules dedans ? y/n ")
if maj == "y" : 
    alphabet.extend(["A","B","C","D","E","F",'G',"H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]) 
    longueurlist += 25

longueurlist = len(alphabet) - 1

#generation lauching 
generer =  input("commencer a generer ? y/n ")

def mdp() :
    for generation in range (longueur):
          aleatoir = random.randint(0,longueurlist)
          print(alphabet[aleatoir],end= '',)
    print("\n")
    
os.system('clear')
print("                                  PASSWORD GENERATOR\n\n")
if generer == "y" :
    for jegen in range(nombredefois) :
        mdp() 



 
