#def hlavni_menu():
    # vypsala
    # 1.zobrazit kontakty
    # 2. pridat kontakt
    # 3. ukoncit

    #nacitat vstup od uzivatela (input)

    #vytisknut

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

print("Váš zoznam kontaktov".upper())   

print("1. zobrazit kontakty")
print("2. pridat kontakt")
print("3. ukoncit")

print(contacts)

meno = input("zadajte svoje meno: ")
telefon = input ("zadaj svoje telefonne cislo: ")
email = input ("vypln emailovu adresu: ")

novy_uzivatel = meno, telefon, email

#print(novy_uzivatel)

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

def hlavni_menu():
    # vypsala:
    # 1. zobrazit kontakty
    # 2. přidat kontakt
    # 3. ukončit
    print("1. zobrazit kontakty")
    print("2. přidat kontakt")
    print("3. ukončit")

    # načte vstup od uživatele (input)
    user_entry = input()
    # vytiskne
    print(user_entry)
    
    # celou implementaci commitnout

hlavni_menu()
