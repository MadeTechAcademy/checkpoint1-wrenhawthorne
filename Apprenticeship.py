from HtmlWriter import HtmlWriter

class Apprenticeship:
    def __init__(self, duties_map, themes_to_duties_map, themes_formatted):
        self.duties = duties_map
        self.themes_to_duties_map = themes_to_duties_map
        self.themes_formatted = themes_formatted
        self.theme = 'apprenticeship'

    def print_duties(self):
        for duty in self.duties:
            print("{0}\n".format(self.duties[duty].description))

    def get_theme(self):
        return self.theme
    
    def set_theme(self, theme):
        self.theme = theme

        return self

    def get_duties_for_theme(self, theme):
        duty_ids = self.themes_to_duties_map.get(theme, [])
        duties = {}

        for duty_id in duty_ids:
            if duty_id in self.duties:
                duties[duty_id] = self.duties[duty_id]

        return duties

    def set_duties_for_theme(self, duties):
        self.duties = duties

        return self

    def output_html(self, html_path='01_apprenticeship.html'):
        theme_name_formatted = self.themes_formatted[self.theme]

        html_writer = HtmlWriter(self.duties, theme_name_formatted)

        html_writer.output_html(html_path)