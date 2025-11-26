from Apprenticeship import Apprenticeship

def app():
    apprenticeship = Apprenticeship()

    user_input = input("""
    Welcome to apprentice themes!\n
    Press (1) to list all the duties\n
    Press (2) to output duties as HTML\n
    Enter your choice:
    """)
    
    if user_input == '1':
        apprenticeship.print_duties()

    if user_input == '2':
        apprenticeship.output_html()

if __name__=="__main__":
    app()