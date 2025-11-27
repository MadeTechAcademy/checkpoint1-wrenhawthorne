class HtmlWriter:
    def __init__(self, duties, theme_name_formatted = 'Apprenticeship'):
        self.duties = duties
        self.theme_name_formatted = theme_name_formatted
        self._html_content = '<html>\n<head>\n<title>DevOps Engineer Duties</title>\n</head>\n<body>\n'

    def create_html(self):
        self._html_content += f'<h1>{self.theme_name_formatted}</h1>'
        self._html_content += '\n<ul>'
        
        for duty in self.duties.values():
            self._html_content += f'\n<li>{duty.description}</li>'
        
        self._html_content += '''\n</ul>\n</body>\n</html>'''

        return self._html_content

    def output_html(self, html_path='01_apprenticeship.html'):
        html_content = self.create_html()

        with open(html_path, 'w') as html_file:
            html_file.write(html_content)