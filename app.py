from Apprenticeship import Apprenticeship
from duties_map import duties_map
from themes_to_duties_map import themes_to_duties_map
from themes_formatted import themes_formatted

def app():
    apprenticeship = Apprenticeship(duties_map, themes_to_duties_map, themes_formatted)

    user_input = input("""
    Welcome to apprentice themes!\n
    To view all apprentice duties, select (0)\n
    For all apprenticeship duties as HTML, select (1)\n
    For 'Bootcamp' duties as HTML, select (2)\n
    For 'Automate!' duties as HTML, select (3)\n
    For 'Houston, Prepare to Launch' duties as HTML, select (4)\n
    For 'Going Deeper' duties as HTML, select (5)\n
    For 'Assemble!' duties as HTML, select (6)\n
    For 'Call Security' duties as HTML, select (7)\n
    Enter your choice:
    """)
    
    if user_input == '0':
        apprenticeship.print_duties()

    if user_input == '1':
        apprenticeship.output_html('01_apprenticeship.html')

    if user_input == '2':
        apprenticeship.set_theme('bootcamp')
        duties = apprenticeship.get_duties_for_theme('bootcamp')
        apprenticeship.set_duties_for_theme(duties)
        apprenticeship.output_html('02_bootcamp.html')

    if user_input == '3':
        apprenticeship.set_theme('automate')
        duties = apprenticeship.get_duties_for_theme('automate')
        apprenticeship.set_duties_for_theme(duties)
        apprenticeship.output_html('03_automate.html')

    if user_input == '4':
        apprenticeship.set_theme('houston')
        duties = apprenticeship.get_duties_for_theme('houston')
        apprenticeship.set_duties_for_theme(duties)
        apprenticeship.output_html('04_houston.html')

    if user_input == '5':
        apprenticeship.set_theme('deeper')
        duties = apprenticeship.get_duties_for_theme('deeper')
        apprenticeship.set_duties_for_theme(duties)
        apprenticeship.output_html('05_deeper.html')

    if user_input == '6':
        apprenticeship.set_theme('assemble')
        duties = apprenticeship.get_duties_for_theme('assemble')
        apprenticeship.set_duties_for_theme(duties)
        apprenticeship.output_html('06_assemble.html')

    if user_input == '7':
        apprenticeship.set_theme('security')
        duties = apprenticeship.get_duties_for_theme('security')
        apprenticeship.set_duties_for_theme(duties)
        apprenticeship.output_html('07_security.html')

if __name__=="__main__":
    app()