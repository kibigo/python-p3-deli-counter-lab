katz_deli = []

def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        statement = "The line is currently:"

        for index, item in enumerate(katz_deli, start=1):
            statement += f" {index}. {item}"
        print (statement)

    
def take_a_number(katz_deli, name):
    katz_deli.append(name)

    line_position = len(katz_deli)
    print (f"Welcome, {name}. You are number {line_position} in line.")

def now_serving (katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        current_serving = katz_deli.pop(0)

        print(f"Currently serving {current_serving}.")


