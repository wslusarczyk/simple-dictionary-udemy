"""
Napisz program, który pozwoli użytkownikowi:
1)Dodawać nowe definicjie
2?)Szukać isniejących definicjii
3)Usuwać wybrane przez niego definicje
"""

dictionary = {
    'mysz': ("Super myszka")
}

choice = int(input("Wybierz co chcesz zrobić: \n 1)Dodać nową definicję, \n 2)Szukać istniejącej definicji, \n 3)Usunąć isniejącą definicje, \n 4)Zakończ program.\n"))
if choice != 4:
    while(choice != 4):
        while (choice != 1 and choice != 2 and choice != 3 and choice != 4):
            print("Wybór złej opcji, wybierz z pośród 1, 2, 3,4")
            choice = int(input(
                "Wybierz co chcesz zrobić: \n 1)Dodać nową definicję, \n 2)Szukać istniejącej definicji, \n 3)Usunąć isniejącą definicje \n "))

        if choice == 1:
            id = input("Podaj nazwę którą chcesz wprowadzić do słownika ")
            title = input("Podaj definicję tej nazwy")
            dictionary[id] = title
            print("Definicja została dodana pomyślnie")
            while (choice != 1 and choice != 2 and choice != 3):
                print("Wybór złej opcji, wybierz z pośród 1, 2, 3")
                choice = int(input(
                    "Wybierz co chcesz zrobić: \n 1)Dodać nową definicję, \n 2)Szukać istniejącej definicji, \n 3)Usunąć isniejącą definicje \n "))
        elif choice == 2:
            title = input("Jakiej definicji szukasz ")
            if title in dictionary:
                print(title, "-", dictionary[title])
            else:
                print("Nie ma takiej definicji w słowniku")
        elif choice == 3:
            lol = input("Jaką definicję chcesz usunąć ")
            del dictionary[lol]
            print("Definicja",lol, " została usunięta")
        choice = int(input("Wybierz co chcesz zrobić: \n 1)Dodać nową definicję, \n 2)Szukać istniejącej definicji, \n 3)Usunąć isniejącą definicje \n "))
else:
    print("Zakończono")

