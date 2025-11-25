from Apprenticeship import Apprenticeship

def app():
    apprenticeship = Apprenticeship()

    user_input = input("""
    Welcome to apprentice themes!\n
    Press (1) to list all the duties\n
    Enter your choice:
    """)
    
    if user_input == '1':
        apprenticeship.print_duties()

if __name__=="__main__":
    app()