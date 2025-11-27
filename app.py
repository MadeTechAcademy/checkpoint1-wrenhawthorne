from Apprenticeship import Apprenticeship
from duties import duties_map
from themes import themes_map

def app():
    apprenticeship = Apprenticeship(duties_map, themes_map)

    user_input = input("""
    Welcome to apprentice themes!\n
    To list all apprentice duties, press (1)\n
    To output all apprenticeship duties to HTML, press (2)\n
    To output 'Bootcamp' duties to HTML, press (3)\n
    Enter your choice:
    """)
    
    if user_input == '1':
        apprenticeship.print_duties()

    if user_input == '2':
        apprenticeship.output_html()

    if user_input == '3':
        bootcamp_duties = apprenticeship.get_duties_for_theme('bootcamp')
        apprenticeship.set_duties_for_theme(bootcamp_duties)
        apprenticeship.output_html('bootcamp.html')

if __name__=="__main__":
    app()