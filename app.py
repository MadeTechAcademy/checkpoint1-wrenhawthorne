import os
import webbrowser
import shutil
import time
import cli_ui
from Apprenticeship import Apprenticeship
from lookups import duties_map, themes, themes_to_duties_map, themes_formatted

def app():
    apprenticeship = Apprenticeship(duties_map, themes_to_duties_map, themes_formatted)

    cli_ui.info(cli_ui.standout, cli_ui.red, "Welcome")
    time.sleep(0.3)
    cli_ui.info(cli_ui.standout, cli_ui.yellow, "to")
    time.sleep(0.3)
    cli_ui.info(cli_ui.standout, cli_ui.green, "Duty")
    time.sleep(0.3)
    cli_ui.info(cli_ui.standout, cli_ui.blue, "Viewer")
    time.sleep(0.3)
    cli_ui.info(cli_ui.standout, cli_ui.fuschia, "(v0.1)\n")
    time.sleep(0.3)

    choices_themes = [
        "1 Apprenticeship",
        "2 Bootcamp",
        "3 Automate!",
        "4 Houston, Prepare to Launch",
        "5 Going Deeper",
        "6 Assemble",
        "7 Call Security"
        ]

    user_input = cli_ui.ask_choice('Please select a theme:\n', choices=choices_themes)
    
    theme = themes[user_input]

    cli_ui.info(cli_ui.standout, cli_ui.green, f"\nYou have selected '{user_input}'\n")
    time.sleep(0.5)

    apprenticeship.set_theme(theme)
    duties = apprenticeship.get_duties_for_theme(theme)
    apprenticeship.set_duties_for_theme(duties)

    choices_display = [
        "1 View duties in terminal",
        "2 View duties in browser",
        "3 Output duties as HTML",
        "4 Download duties as HTML"
    ]

    user_view_or_download = cli_ui.ask_choice("How would you like to view this theme's duties?\n", choices=choices_display)

    html_file = f'0{user_input[0]}_{theme}.html'
    filename = 'file:///'+os.getcwd()+'/' + f'{html_file}'
    
    if user_view_or_download == choices_display[0]:
        apprenticeship.print_duties()
    elif user_view_or_download == choices_display[1]:
        webbrowser.open_new_tab(filename)
    elif user_view_or_download == choices_display[2]:
        apprenticeship.output_html(html_file)
    elif user_view_or_download == choices_display[3]:
        timestamp = time.time()
        destination = os.path.expanduser(f'~/Downloads/{timestamp}_{html_file}')
        shutil.copy(html_file, destination)
        cli_ui.info(cli_ui.standout, cli_ui.green, f"Saved to {destination}")

    cli_ui.info(cli_ui.standout, cli_ui.green,'\nThanks for using Apprentice Themes!\n')

if __name__=="__main__":
    app()