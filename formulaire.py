# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:42:13 2021

@author: Logan
"""
from tkinter import *

def afficherFormulaire():
    print("Formulaire ouvert")
    fenetre_form = Tk()
    taille_police = 12
    famille_police = "Arial"
    
    #Nom
    label_nom = Label(fenetre_form, text = "Nom :", font=(famille_police, taille_police))
    label_nom.pack()
    entree_nom = Entry(fenetre_form, width=50, font=(famille_police, taille_police))
    entree_nom.pack()
    
    #Prénom
    label_prenom = Label(fenetre_form, text = "Prénom :", font=(famille_police, taille_police))
    label_prenom.pack()
    entree_prenom = Entry(fenetre_form, width=50, font=(famille_police, taille_police))
    entree_prenom.pack()
    
    #Mail
    label_mail = Label(fenetre_form, text = "Mail :", font=(famille_police, taille_police))
    label_mail.pack()
    entree_mail = Entry(fenetre_form, width=50, font=(famille_police, taille_police))
    entree_mail.pack()
    
    #Téléphone
    label_tel = Label(fenetre_form, text = "Téléphone :", font=(famille_police, taille_police))
    label_tel.pack()
    entree_tel = Entry(fenetre_form, width=50, font=(famille_police, taille_police))
    entree_tel.pack()
    
    #Age
    label_age = Label(fenetre_form, text = "Age :", font=(famille_police, taille_police))
    label_age.pack()
    entree_age = Spinbox(fenetre_form, width=50, font=(famille_police, taille_police), from_=0, to=150, increment=1)
    entree_age.pack()   
    
    def verification():
        
        nom = str(entree_nom.get());
        prenom = str(entree_prenom.get());
        mail = str(entree_mail.get());
        tel = str(entree_tel.get());
        age = int(entree_age.get());
        
        #Vérification champs non complétés
        if nom == "" or prenom == "" or mail == "" or tel == "":
            print("Erreur : Il manque une ou plusieurs informations\nL'exportation n'a pas été effectuée")
            messagebox.showinfo("Erreur","Un ou plusieurs champs sont incomplets.")
            return False;
        
        #Validité nom prénom (chiffres interdits)
        chars_interdit_nom_prenom = ["1", "2", "3", "4", "5", "6", "7","8","9","0"]
        for i in range(len(chars_interdit_nom_prenom)):
            if nom.find(str(chars_interdit_nom_prenom[i])) != -1 or prenom.find(str(chars_interdit_nom_prenom[i])) != -1:
                print("Erreur : Nom ou prénom invalide\nL'exportation n'a pas été effectuée")
                messagebox.showinfo("Erreur","Attention, votre nom / prénom ne peut contenir de chiffre.")
                return False;
            
        #Validité mail
        chars_obligatoires = ["@", "."]
        for i in range(len(chars_obligatoires)):
            if mail.find(str(chars_obligatoires[i])) == -1:
                print("Erreur : Format du mail invalide\nL'exportation n'a pas été effectuée")
                messagebox.showinfo("Erreur","Attention, Le format du mail saisi n'est pas valide.\nAssurez vous que votre adresse mail contient les bons caractères ainsi qu'une extension valide.\nExemple : prenom.nom@gmail.com")
                return False;
            
        validite = False
        extensions=[".com", ".net", ".fr"]
        for i in range(len(extensions)):
            if mail.find(str(extensions[i])) != -1: #Si l'extension est valide
                validite = True
                break
        
        if validite == False:
            print("Erreur : Extension mail non valide\nL'exportation n'a pas été effectuée")
            messagebox.showinfo("Erreur","Attention, L'extension du mail saisi n'est pas valide.\nAssurez vous que votre adresse mail contient les bons caractères ainsi qu'une extension valide.\nExemple : prenom.nom@gmail.com")
            return False;
        
        #Validité téléphone
        
        #Formatage tel (on enlève les séparateurs si présents)
        if tel.find(" ") == True or tel.find("."):
            tel = tel.replace(" ", "")
            tel = tel.replace(".", "")
            
        if tel.startswith("+33") == True: #Si le numéro commence par +33
            tel = tel.replace("+33", "0") #On formatte
            
        if tel.isnumeric() == False:
            print("Erreur : Tel non numérique\nL'exportation n'a pas été effectuée")
            messagebox.showinfo("Erreur","Attention, Le numéro de téléphone saisi n'est pas valide.\nAssurez-vous que le numéro comporte le bon nombre de chiffres.\nExemple : 03 80 12 34 56\nOu +33 6 12 34 56 78")
            return False;
        
        if len(tel) != 10:
            print("Erreur : Longueur tel invalide\nL'exportation n'a pas été effectuée")
            messagebox.showinfo("Erreur","Attention, Le numéro de téléphone saisi n'est pas valide.\nAssurez-vous que le numéro comporte le bon nombre de chiffres.\nExemple : 03 80 12 34 56\nOu +33 6 12 34 56 78")
            return False;
            
        #Validité age
        if age <=0:
            print("Erreur : Âge invalide\nL'exportation n'a pas été effectuée")
            messagebox.showinfo("Erreur","L'âge saisi n'est pas valide.")
            return False;
        
        if age < 18:
            print("Erreur : Âge mineur\nL'exportation n'a pas été effectuée")
            messagebox.showinfo("Erreur","Vous devez être majeur pour remplir ce formulaire.")
            return False;
            
        #Pas d'erreur détectée, on exporte le formulaire
        f = open('formulaire.txt','w')
        f.write("Nom : " + str(nom) + "\n")
        f.write("Prénom : " + str(prenom) + "\n")
        f.write("Mail : " + str(mail) + "\n")
        f.write("Tel : " + str(tel) + "\n")
        f.write("Âge : " + str(age) + " ans\n")
        f.close()
        print("Formulaire exporté")
        messagebox.showinfo("Réussi","Le formulaire a bien été exporté")
        fenetre_form.destroy()
        
        
        def fenetreFormulaire(f_nom, f_prenom, f_mail, f_tel, f_age):
            print("Affichage du Formulaire")
            fenetre_affichage_form = Tk()
            
            nom = str(f_nom)
            prenom = str(f_prenom)
            mail = str(f_mail)
            tel = str(f_tel)
            age = str(f_age)
            
            label_nom_prenom = Label(fenetre_affichage_form, text = "Vous êtes : " + str(prenom) + " " + str(nom), font=("Arial", 14))
            label_mail = Label(fenetre_affichage_form, text = "Votre mail est : " + str(mail), font=("Arial", 14))
            label_tel = Label(fenetre_affichage_form, text = "Votre numéro de téléphone est : " + str(tel), font=("Arial", 14))
            label_age = Label(fenetre_affichage_form, text = "Vous avez : " + str(age) + " ans", font=("Arial", 14))
            
            label_nom_prenom.pack()
            label_mail.pack()
            label_tel.pack()
            label_age.pack()
        
        #On affiche les informations saisies
        fenetreFormulaire(nom, prenom, mail, tel, age)
        
            
    
    bouton_confirmer = Button(fenetre_form, text='Confirmer', relief=RAISED, command=verification).pack(side=LEFT, padx=5, pady=5)
    fenetre_form.mainloop()
    
afficherFormulaire()
    

#Blocage de la fermeture de la console
input("pause...")