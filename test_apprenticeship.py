from Apprenticeship import Apprenticeship

class TestPrintDuties:
    def test_prints_empty_list(self, capsys):
        appr = Apprenticeship()
        appr._duties = []
        appr.print_duties()
        captured = capsys.readouterr()
        output = captured.out

        assert output == ''

    def test_prints_simple_list(self, capsys):
        appr = Apprenticeship()
        appr._duties = ['Apprentice', 'Ship']
        appr.print_duties()
        captured = capsys.readouterr()
        output = captured.out

        assert output == 'Apprentice\n\nShip\n\n'

    def test_prints_list_of_duties(self, capsys):
        appr = Apprenticeship()
        appr.print_duties()
        captured = capsys.readouterr()
        output = captured.out

        firstSlice = output[:50]
        lastSlice = output[-50:]

        assert firstSlice == 'Duty 1 Script and code in at least one general pur'
        assert lastSlice == ' with a relentless focus on the user experience.\n\n'

class TestOutputHtml:
    def test_returns_html_template(self):
        appr = Apprenticeship()
        appr._duties = ['Test!']

        htmlTemplate = '''<html>\n<head>\n<title>DevOps Engineer Duties</title>\n</head>\n<body>\n<ul>\n<li>Test!</li>\n</ul>\n</body>\n</html>'''

        assert appr.create_html() == htmlTemplate

    def test_inserts_duties_as_list_items(self):
        appr = Apprenticeship()
        appr._duties = ['Focus on learning', 'Look after yourself', 'Read the road signs in Geoguessr and just lock in a guess early']

        html = appr.create_html()

        assert "<li>Focus on learning</li>" in html
        assert "<li>Look after yourself</li>" in html

    def test_outputs_to_html_document(self, tmp_path):
        appr = Apprenticeship()
        appr._duties = ['Egg', 'Salad', 'Sando']

        test_html_path = tmp_path / 'test.html'
        appr.output_html(test_html_path)
        html_file = open(test_html_path)
        output = html_file.read()

        assert "<li>Egg</li>" in output
        assert "<li>Salad</li>" in output
        assert "<li>Sando</li>" in output
