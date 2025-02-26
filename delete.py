#!/usr/bin/env python3

import os

DB_PATH = 'password_manager.db'
KEY_PATH = 'encryption.key'

def delete_files():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print("Base de données supprimée.")
    else:
        print("La base de données n'existe pas.")

    if os.path.exists(KEY_PATH):
        os.remove(KEY_PATH)
        print("Clé de chiffrement supprimée.")
    else:
        print("La clé de chiffrement n'existe pas.")

if __name__ == "__main__":
    delete_files()

