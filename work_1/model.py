import view

def write_data(user):
    """Записывает данные в базу данных"""
    with open("tele.txt", "a", encoding="utf8" ) as file:
        file.write(user + "\n")
def read_data():
    with open("tele.txt", "r", encoding="utf8") as file:
        content = file.readlines()
        return content
def find_person(persons, name):
    """По имени или фамилии ищет человека в базе данных"""
    similar_person = list()
    for person in persons:
        if name.lower() in person.lower():
            similar_person.append(person)
    for i in range(len(similar_person)):
        print(f"{i + 1} {similar_person[i]}")
    print("--------------------------")
    while True:
        request = view.change_menu()
        if request == 1:
            if len(similar_person) > 1:
                choice = int(input("Введите данные, которые необходимо изменить - "))
            else:
                choice = 1
            print("Введите новые данные")
            new_person = view.get_person()
            change_person(new_person, similar_person[choice - 1])
            print("--------------------------")
            print("Данные обновлены")
            print(f"Добавлен: {new_person}")
            print("--------------------------")
        elif request == 2:
            if len(similar_person) > 1:
                choice = int(input("Введите данные, которые необходимо удалить - "))
            else:
                choice = 1
            delete_person(similar_person[choice - 1])
            print("--------------------------")
            print("Данные удалены")
            print("--------------------------")
        else:
            break
def delete_person(name):
     """Удаляет данные"""
persons = read_data()
with open("tele.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if name != person:
                file.write(person)
def change_person(new_name, old_name):
    """Изменяет данные"""
    persons = read_data()
    with open("tele.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if  old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")
def print_all():
    with open("tele.txt", "r", encoding="utf8" ) as file:
        lst = file.readlines()
        for line in lst:
            print(line)