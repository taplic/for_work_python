import view
import model

def main() :
    while True :
        request = view.choice()
        if request == 1:
            user = view.get_person()
            model.write_data(user)
        if request == 2:
            users = model.read_data()
            name = view.ask_person()
            model.find_person(users, name )
        if request == 3:
            model.print_all()
        else:
            break
           
if __name__ == "__main__" :
    main()  