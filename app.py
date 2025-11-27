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
    To output 'Automate!' duties to HTML, press (4)\n
    Enter your choice:
    """)
    
    if user_input == '1':
        apprenticeship.print_duties()

    if user_input == '2':
        apprenticeship.output_html('01_apprenticeship.html')

    if user_input == '3':
        bootcamp_duties = apprenticeship.get_duties_for_theme('bootcamp')
        apprenticeship.set_duties_for_theme(bootcamp_duties)
        apprenticeship.output_html('02_bootcamp.html')

    if user_input == '4':
        bootcamp_duties = apprenticeship.get_duties_for_theme('automate')
        apprenticeship.set_duties_for_theme(bootcamp_duties)
        apprenticeship.output_html('03_automate.html')

if __name__=="__main__":
    app()