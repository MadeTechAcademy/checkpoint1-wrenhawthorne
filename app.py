import os
import webbrowser
from Apprenticeship import Apprenticeship
from lookups import duties_map, themes, themes_to_duties_map, themes_formatted

def app():
    apprenticeship = Apprenticeship(duties_map, themes_to_duties_map, themes_formatted)

    user_input = input("""
    Welcome to Apprentice Themes!\n
    To view all apprentice duties, select (0)\n
    For all apprenticeship duties as HTML, select (1)\n
    For 'Bootcamp' duties as HTML, select (2)\n
    For 'Automate!' duties as HTML, select (3)\n
    For 'Houston, Prepare to Launch' duties as HTML, select (4)\n
    For 'Going Deeper' duties as HTML, select (5)\n
    For 'Assemble!' duties as HTML, select (6)\n
    For 'Call Security' duties as HTML, select (7)\n
    Type your choice (and press Enter):
    """)
    
    if user_input not in themes:
        print('\nPlease select a valid option!\n')
        return
    
    theme = themes[user_input]

    if theme is None:
        apprenticeship.print_duties()
        return

    apprenticeship.set_theme(theme)
    duties = apprenticeship.get_duties_for_theme(theme)
    apprenticeship.set_duties_for_theme(duties)

    html_file = f'0{user_input}_{theme}.html'
    apprenticeship.output_html(html_file)
    filename = 'file:///'+os.getcwd()+'/' + f'{html_file}'

    chooseDisplay = input("""
    To view this theme's duties in your browser, select (1)\n
    Type your choice (and press Enter):
    """)

    if chooseDisplay == '1':
        print('\nLoading...\n')
        webbrowser.open_new_tab(filename)
    else:
        print('\nThanks for using Apprentice Themes!\n')

if __name__=="__main__":
    app()