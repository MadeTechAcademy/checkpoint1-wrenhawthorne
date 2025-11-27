class Apprenticeship:
    def __init__(self, duties_map, themes_to_duties_map, themes_formatted):
        self.duties = duties_map
        self.themes_to_duties_map = themes_to_duties_map
        self.themes_formatted = themes_formatted
        self.theme = 'apprenticeship'

    _html_content = '<html>\n<head>\n<title>DevOps Engineer Duties</title>\n</head>\n<body>\n'

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

    def create_html(self):
        self._html_content += f'<h1>{self.themes_formatted[self.theme]}</h1>'
        self._html_content += '\n<ul>'
        
        for duty_id in self.duties.keys():
            self._html_content += f'\n<li>{self.duties[duty_id].description}</li>'
        
        self._html_content += '''\n</ul>\n</body>\n</html>'''

        return self._html_content
    
    def output_html(self, html_path = '01_apprenticeship.html'):
        self.create_html()

        with open(html_path, 'w') as html_file:
            html_file.write(self._html_content)