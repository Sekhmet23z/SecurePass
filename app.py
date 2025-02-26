#!/usr/bin/env python3

import os
import sqlite3
import secrets
import string
from cryptography.fernet import Fernet
import sys
import pyfiglet
 
# Définitions des chemins pour la base de données et la clé de chiffrement
DB_PATH = 'password_manager.db'
KEY_PATH = 'encryption.key'

def check_initial_files():
    # Vérification de la présence de la clé de chiffrement et de la base de données
    if not os.path.exists(KEY_PATH) or not os.path.exists(DB_PATH):
        print("Erreur : Clé de chiffrement ou base de données introuvable.")
        print("Veuillez exécuter './start.py' ou 'python3 start.py' pour les créer.")
        sys.exit(1)  # Quitte le programme avec un code d'erreur

def load_key():
    # Charge la clé de chiffrement depuis le fichier
    with open(KEY_PATH, 'rb') as key_file:
        return Fernet(key_file.read())

# Effectue la vérification des fichiers dès le démarrage
check_initial_files()

# Initialisation de la suite de chiffrement avec la clé chargée
cipher_suite = load_key()


def connect_database():
    # Connexion à la base de données existante
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    return conn, cursor

def close_connection(conn):
    conn.close()

def generer_mdp(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    strong_password = ''.join(secrets.choice(characters) for _ in range(length))
    print("Mot de passe généré:", strong_password)
    return strong_password

# Chiffrement du mot de passe avant l'enregistrement
def enregistrer_mot_de_passe(password_name, password_value):
    try:
        conn, cursor = connect_database()
        encrypted_password = cipher_suite.encrypt(password_value.encode())
        insert_password_query = "INSERT INTO passwords (password_name, password_value) VALUES (?, ?)"
        cursor.execute(insert_password_query, (password_name, encrypted_password))
        conn.commit()
        print("Mot de passe enregistré avec succès.")
    except sqlite3.Error as e:
        print("Erreur lors de l'enregistrement du mot de passe:", e)
    finally:
        close_connection(conn)

# Récupération et déchiffrement des mots de passe
def get_passwords():
    try:
        conn, cursor = connect_database()
        cursor.execute("SELECT password_name, password_value FROM passwords")
        encrypted_passwords = cursor.fetchall()
        passwords = [(name, cipher_suite.decrypt(value).decode()) for name, value in encrypted_passwords]
        return passwords
    except sqlite3.Error as e:
        print("Erreur lors de la récupération des mots de passe:", e)
        return None
    finally:
        close_connection(conn)

def afficher_mots_de_passe():
    passwords = get_passwords()
    if passwords:
        print("Vos mots de passe enregistrés :")
        for password_name, password_value in passwords:
            print(f"{password_name}: {password_value}")
    else:
        print("Aucun mot de passe trouvé.")

def modifier_mot_de_passe(password_name, new_password_value):
    try:
        conn, cursor = connect_database()
        encrypted_password = cipher_suite.encrypt(new_password_value.encode())
        cursor.execute("UPDATE passwords SET password_value = ? WHERE password_name = ?", (encrypted_password, password_name))
        if cursor.rowcount > 0:
            conn.commit()
            print(f"Mot de passe pour '{password_name}' modifié avec succès.")
        else:
            print(f"Mot de passe nommé '{password_name}' non trouvé.")
    except sqlite3.Error as e:
        print("Erreur lors de la modification du mot de passe:", e)
    finally:
        close_connection(conn)

def supprimer_mot_de_passe(password_name):
    try:
        conn, cursor = connect_database()
        cursor.execute("DELETE FROM passwords WHERE password_name = ?", (password_name,))
        if cursor.rowcount > 0:
            conn.commit()
            print(f"Mot de passe pour '{password_name}' supprimé avec succès.")
        else:
            print(f"Mot de passe nommé '{password_name}' non trouvé.")
    except sqlite3.Error as e:
        print("Erreur lors de la suppression du mot de passe:", e)
    finally:
        close_connection(conn)

def main():
    print("Gestionnaire de mots de passe")
    while True:
        print("\n1. Générer un mot de passe")
        print("2. Enregistrer un mot de passe")
        print("3. Voir les mots de passe enregistrés")
        print("4. Modifier un mot de passe")
        print("5. Supprimer un mot de passe")
        print("6. Quitter")
        choice = input("\nEntrez votre choix: ")

        if choice == "1":
            length = int(input("Longueur du mot de passe (par défaut 12): ") or 12)
            generer_mdp(length)
        elif choice == "2":
            password_name = input("Entrez le nom du mot de passe: ")
            password_value = input("Entrez le mot de passe (ou laissez vide pour en générer un): ")
            if not password_value:
                password_value = generer_mdp()
            enregistrer_mot_de_passe(password_name, password_value)
        elif choice == "3":
            afficher_mots_de_passe()
        elif choice == "4":
            password_name = input("Entrez le nom du mot de passe à modifier: ")
            new_password_value = input("Entrez le nouveau mot de passe (ou laissez vide pour en générer un): ")
            if not new_password_value:
                new_password_value = generer_mdp()
            modifier_mot_de_passe(password_name, new_password_value)
        elif choice == "5":
            password_name = input("Entrez le nom du mot de passe à supprimer: ")
            supprimer_mot_de_passe(password_name)
        elif choice == "6":
            print("Fermeture du gestionnaire de mots de passe.")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    ascii_banner = pyfiglet.figlet_format("SecurePass")
    print(ascii_banner)
    print("@Sekhmet.23z")
    main()

