#hlavni_menu():
    # fce vypsala
        # 1.zobrazit kontakty
        # 2. pridat kontakt
        # 3. ukoncit

    #nacitat vstup od uzivatela (input)

    #vytisknut

def hlavni_menu():
    print("Váš zoznam kontaktov".upper())   
    print("1. Zobraziť kontakty")
    print("2. Pridať kontakt")
    print("3. Ukončiť")


contacts = [
    {
        "name": "Anička",
        "email": "anicka@email.com",
        "phone": "777 777 777"
    },
    {
        "name": "Nikol",
        "email": "nikol@email.com",
        "phone": "777 777 777"
    }
]

#vstup od uzivatela - novy kontakt
meno = input("zadajte svoje meno: ")
email = input ("vypln emailovu adresu: ")
phone = input ("zadaj svoje telefonne cislo: ")

new_contact = {
    "name": meno,
    "email": email,
    "phone": phone
}

print(new_contact)

print("\n\n")
contacts.append(new_contact)

print(contacts)