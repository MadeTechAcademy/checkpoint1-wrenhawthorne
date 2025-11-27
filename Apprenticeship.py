class Apprenticeship:
    def __init__(self, duties, themes):
        self.duties = duties
        self.themes = themes

    _html_content = '''<html>\n<head>\n<title>DevOps Engineer Duties</title>\n</head>\n<body>\n<ul>'''

    def print_duties(self):
        for duty in self.duties:
            print("{0}\n".format(self.duties[duty].description))

    def get_duties_for_theme(self, theme = 'apprenticeship'):
        duty_id_list = self.themes.get(theme)
        duties = []

        for duty_id in duty_id_list:
            duty = self.duties[duty_id]
            duties.append(duty)

        return duties
    
    def set_duties_for_theme(self, duties):
        self._duties = duties

        return self

    def create_html(self):
        for duty in self.duties.values():
            self._html_content += f'\n<li>{duty.description}</li>'
        
        self._html_content += '''\n</ul>\n</body>\n</html>'''

        return self._html_content
    
    def output_html(self, html_path = 'output.html'):
        self.create_html()

        with open(html_path, 'w') as html_file:
            html_file.write(self._html_content)