# coding: utf-8
 
from tkinter import * 
from tkinter import messagebox
#from tkinter.filedialog import *

def recupere():
    """force = calcul_force(entree.get())"""                                                                                               #avoir la fonction de calcul de force du mdp et l'integrer au code puis renvoyer la note
    force = 10                                                       
    if type(force) == int:
        messagebox.showinfo("Alerte", "Votre mot de passe a une force de: "+str(force)+"/20")                                              #on vérifie si on recoie une note ou une erreur
    else:
        """messagebox.showinfo(force)"""                                                                                                   #si le message d'erreur est directement retourné
        messagebox.showinfo("Test de la force", "Erreur, veuillez choisir un autre mot de passe")

def genere():
    """mdp = generateur()"""                                                                                                               # retour de la fonction qui propose un mot de passe
    mdp = "sordadex-proximet"
    messagebox.showinfo("Mot de passe généré", mdp)

fenetre = Tk()

label = Label(fenetre, text="Saisissez un mot de passe à tester.\nVous avez le droit de rentrer un mot de passe contenant seulement: des majuscules, minuscules, chiffres et tirets.")
label.pack()

value = StringVar() 
value.set("Valeur")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()

bouton = Button(fenetre, text="Tester", command=recupere)
bouton.pack()

label2 = Label(fenetre, text="\n\nOu bien, générez un mot de passe.")
label2.pack()

bouton2 = Button(fenetre, text="Générer un mot de passe", command=genere)
bouton2.pack()


photo = PhotoImage(file="ma_photo.png")
canvas = Canvas(fenetre,width=350, height=200)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()





fenetre.mainloop()

