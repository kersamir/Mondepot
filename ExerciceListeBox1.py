import tkinter as tk
# Fonction à appeler lorsqu'on selectionne 
def afficher_selection():
    # récupère les indices des éléments selectionnés 
    indices = listbox.curselection() 
    #utiliser les indices pour récupérer les valeurs corespondantes 
    concepte = [listbox.get(i) for i in indices]
    # afficher dans la console les concepts en cybersécurité 
    print(f"Les concept(s) en cybersécurité : {concepte}")

# Création de mon interface 

window = tk.Tk()
window.title("Concepts en cybersécurité")
window.geometry("350x200")  # définition de la dimension de la fenêtre
# création de la ListBox
listbox = tk.Listbox(window,selectmode=tk.MULTIPLE)
# insertion ou ajout des concepts en cybersécurité  à la liste
Concepte_cybersecurite =[
    "Phishing", 
    "Malware",
    "Firewall",
    "Chiffrement",
    "VPN"
]
# Ajouter les types de concepte a la liste
for concepte in Concepte_cybersecurite:
    listbox.insert(tk.END,concepte)  # tk.END ajoute à la fin de la liste
# placer la liste sur la fenêtre 
listbox.pack()
# créer un bouton 
button = tk.Button(window,text="Afficher des concepts en cybersécurité",command=afficher_selection)
button.pack()

# lancer mon application
window.mainloop()