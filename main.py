import os

NUM_LEVELS_ACCESS = 4


def main():
    login_data = open("login_data.csv", "r")
    user_info = {}  # creates empty dict
    for line in login_data:
        line = line.strip()  # gets rid of \n
        pieces = line.split(',')
        user_info[pieces[0]] = {}  # assigns an empty dict to the username
        user_info[pieces[0]]["password"] = pieces[1]
        user_info[pieces[0]]["access"] = pieces[2]

    menus = {}
    for menu_filename in os.listdir('menus'):  # iterates through every menu file in the menu directory
        menu_file = open('menus/'+menu_filename, "r")
        menu_name = menu_file.readline().strip()
        menus[menu_name] = {}
        menus[menu_name]["access"] = {}  # creates dict with all access types
        for level in range(NUM_LEVELS_ACCESS):
            data = menu_file.readline().strip().split(',')
            menus[menu_name]["access"][data[0]] = data[1].split(' ')  # adds list that contains 'r', 'w', or both

    print(user_info)
    print(menus)
    print("Welcome to Dan's Coffee Shop! Please enter your username: ")
    username = input()
    while username not in user_info:
        username = input("Username not found, please try again: ")
    password = input("Hi " + username + ", please enter your password: ")
    while password != user_info[username]["password"]:
        password = input("Incorrect password, please try again: ")
    print("Login successful... see menu options below:")
    for option in menus:
        print(option)
    print()  # line for spacing
    menu_selected = input("Please enter a menu you'd like to access: ")
    valid_input = False
    while not valid_input:
        if menu_selected not in menus:
            menu_selected = input("Input does not match menu options, please try again: ")
        elif 'r' not in menus[menu_selected]['access'][user_info[username]['access']]:
            menu_selected = input("You are not authorized to access this menu.\n"
                                  "Please select a different one or contact your administrator:")
        else:
            valid_input = True
    print("end")



if __name__ == '__main__':
    main()