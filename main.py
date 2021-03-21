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
            print("Wybór złej opcji, wybierz spośród 1, 2, 3, 4")
            choice = int(input(
                "Wybierz co chcesz zrobić: \n 1)Dodać nową definicję, \n 2)Szukać istniejącej definicji, \n 3)Usunąć isniejącą definicje, \n 4)Zakończ program. \n "))

        if choice == 1:
            id = input("Podaj nazwę którą chcesz wprowadzić do słownika ")
            value = input("Podaj definicję tej nazwy")
            dictionary[id] = value
            print("Definicja została dodana pomyślnie")
            while (choice != 1 and choice != 2 and choice != 3):
                print("Wybór złej opcji, wybierz z pośród 1, 2, 3")
                choice = int(input(
                    "Wybierz co chcesz zrobić: \n 1)Dodać nową definicję, \n 2)Szukać istniejącej definicji, \n 3)Usunąć isniejącą definicje, \n 4)Zakończ program. \n "))
        elif choice == 2:
            value = input("Jakiej definicji szukasz ")
            if value in dictionary:
                print(value, "-", dictionary[value])
            else:
                print("Nie ma takiej definicji w słowniku")
        elif choice == 3:
            idToRemove = input("Jaką definicję chcesz usunąć ")
            del dictionary[idToRemove]
            print("Definicja", idToRemove, " została usunięta")
        choice = int(input("Wybierz co chcesz zrobić: \n 1)Dodać nową definicję, \n 2)Szukać istniejącej definicji, \n 3)Usunąć isniejącą definicje, \n 4)Zakończ program. \n "))
else:
    print("Zakończono")
