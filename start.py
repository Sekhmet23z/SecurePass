#!/usr/bin/env python3

import os
import sqlite3
from cryptography.fernet import Fernet

DB_PATH = 'password_manager.db'
KEY_PATH = 'encryption.key'

def create_key():
    # Crée une nouvelle clé de chiffrement et la sauvegarde dans un fichier
    key = Fernet.generate_key()
    with open(KEY_PATH, 'wb') as key_file:
        key_file.write(key)
    print("Clé de chiffrement créée et sauvegardée.")

def create_database():
    # Création de la base de données et de la table si elle n'existe pas
    if os.path.exists(DB_PATH):
        print("Erreur : La base de données 'password_manager.db' existe déjà.")
    else:
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                password_name TEXT NOT NULL,
                                password_value TEXT NOT NULL
                            )''')
            conn.commit()
            print("La base de données 'password_manager.db' a été créée avec succès.")
        except sqlite3.Error as e:
            print("Erreur lors de la création de la base de données :", e)
        finally:
            conn.close()

if __name__ == "__main__":
    if not os.path.exists(KEY_PATH):
        create_key()
    else:
        print("Erreur : La clé de chiffrement existe déjà.")
    create_database()

