# coding: utf-8
 
from tkinter import * 
from tkinter import messagebox
#from tkinter.filedialog import *
from random import randint

def lirefichier(fichier = 'liste_francais.txt', encoding = "UTF-8"):
    """La fonction a 2 entrées, et pas de sorties. Il sert a lire une fichier .txt en python"""
    # lire un fichier .txt en python
    f = open(fichier, encoding = "ISO-8859-15")
    contenu = f.read() # longue chaine de caractere contenant tout les mot du fichier
    #print(contenu[:21]) # affiche 20 premier caractere du fichier
    #print(contenu[1000:1011]) # affiche 10 caractere entre 1000eme et 1010eme inclus
    contenu = contenu.lower()
    return contenu

def dictionnaire_list(text):
    i = 0 # indice caractere suivant du courant
    ind_lettre = 0  #indice du caractere courant

    nb_total_lettre = len(text)
    alpha = "abcdefghijklmnopqrstuvwxyz"
    voyelles = "aeiouy"
    #ignore = ["\n", " ", '\x9c', ] # caractere a ignorer
    dico_lettre_possible = []
    
    for lettre in alpha: # creer un dictionnaire liste de liste vide derriere chaque lettre de alpha 
        dico_lettre_possible.append([])

    for lettre in text: # mettre tout en minuscule
        lettre = lettre.lower()
        
        if(i + 1 == nb_total_lettre): # fin texte ?
            break # finit xxx

        # ignore certains caractere
        if(lettre not in alpha or text[i+1].lower() not in alpha):
            i = i+1
            continue # une fois ignorer, goto prochaine lettre  ------>>>

        ind_lettre = alpha.index(lettre) # index de la lettre dans notre dico principal ; index dans "alphabet"

        """
        if (text[i+1].lower() not in dico_lettre_possible[ind_lettre]): # lettre suivante déjà dans sous dico ?
            dico_lettre_possible[ind_lettre].append(text[i+1].lower()) # si non alors l'ajouter
        """

        #if (text[i+1].lower() not in dico_lettre_possible[ind_lettre]): # lettre suivante déjà dans sous dico ?
        syl_ind = 0
        nb_voyelle = 0
        syllabe = ""
        for syl_ind in range(0, 4):
            if text[i+1+syl_ind].lower() in voyelles:
                nb_voyelle = nb_voyelle + 1
            if nb_voyelle == 2 or text[i+1+syl_ind] not in alpha : # max 1 voyelles dans la syllabe
                break
            else:
                syllabe = syllabe + text[i+1+syl_ind].lower()
        
        if syllabe not in dico_lettre_possible[ind_lettre] :
            dico_lettre_possible[ind_lettre].append(syllabe) # si non alors l'ajouter

        i = i + 1

    return dico_lettre_possible

def generateur(nb_mot, longueur):
    contenu = lirefichier('liste_francais.txt', "ISO-8859-15")
    voyelles = "aeiouy"
    cns = 0
    alpha = "abcdefghijklmnopqrstuvwxyz"

    dico = dictionnaire_list(contenu)
    password = []
    ind_lettre = 0

    for m in range(nb_mot): # commencement du programme ; debut ; generation de la premiere lettre
        cr1 = alpha[randint(0, len(alpha)-1)]
        car_courant = cr1
        mot_courant = cr1

        for l in range(longueur - 1):
            ind_lettre = alpha.index(car_courant)
            car_courant = dico[ind_lettre][randint(0, len(dico[ind_lettre])-1)]
            mot_courant = mot_courant + car_courant

        password.append(mot_courant) # + "-")

    return password

def testeur(mdp):
    # comment for test
    print(mdp)
    score_longueur = test_longueur(mdp)
    score_maj = test_majuscule(mdp)
    score_carcsp = test_carcsp(mdp)
    score_chiffre = test_chiffre(mdp)
    note = score_longueur + score_maj + score_carcsp + score_chiffre

    detail_score = "\n\t score_longueur : " + str(score_longueur) + "\n\t score_maj : " + str(score_maj) + "\n\t score_carcsp : " + str(score_carcsp) + "\n\t score_chiffre : " + str(score_chiffre)

    return [note, detail_score]

def test_longueur(mdp):
    if len(mdp) <=10 and len(mdp) >=8 :
        return 3
    elif len(mdp) >=11 :
        return 5
    return 0
    
# majuscule
def test_majuscule(mdp):
    a_minuscule = False
    a_majuscule = False
    majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for lettre in mdp :
        if lettre in majuscule :
            a_majuscule = True
        if lettre in majuscule.lower() :
            a_minuscule = True
        if a_majuscule == True and a_minuscule == True :
            return 5
    return 0

# caractères spéciaux
def test_carcsp(mdp):
    majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for lettre in mdp :
        if lettre not in majuscule and lettre not in majuscule.lower() :
            return 5
    return 0

# chiffres
def test_chiffre(mdp):
    nombre = "0123456789"
    for lettre in mdp :
        if lettre in nombre :
            return 5
    return 0


def recupere():
    """force = calcul_force(entree.get())"""  
    global entree
    print(entree.get())                                                                                             #avoir la fonction de calcul de force du mdp et l'integrer au code puis renvoyer la note
    """force = testeur(entree.get())"""
    res = testeur(entree.get())                                                       
    if type(res) == list:
        messagebox.showinfo("Alerte", "Votre mot de passe a une force de: "+str(res[0])+"/20")                                              #on vérifie si on recoie une note ou une erreur
    else:
        """messagebox.showinfo(force)"""                                                                                                   #si le message d'erreur est directement retourné
        messagebox.showinfo("Test de la force", "Erreur, veuillez choisir un autre mot de passe")

def genere():
    mdp = generateur(3, 4)                                                                                                               # retour de la fonction qui propose un mot de passe
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

