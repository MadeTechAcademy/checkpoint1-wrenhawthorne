from Apprenticeship import Apprenticeship
from duties import duties_map
from themes import themes_map

def app():
    apprenticeship = Apprenticeship(duties_map, themes_map)

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