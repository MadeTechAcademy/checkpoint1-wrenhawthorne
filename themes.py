from apprenticeship_duties import apprenticeship_duties

duties_list = apprenticeship_duties

def print_duties_list():
    for duty in duties_list:
        print("{0}\n".format(duty))

if __name__=="__main__":
    user_input = input("""
    Welcome to apprentice themes!\n
    Press (1) to list all the duties\n
    Enter your choice:
    """)
    
    if user_input == '1':
        print_duties_list()