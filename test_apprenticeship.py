from Apprenticeship import Apprenticeship

class TestPrintDuties:
    def test_prints_empty_list(self, capsys):
        appr = Apprenticeship()
        appr._duties = {}
        appr.print_duties()
        captured = capsys.readouterr()
        output = captured.out

        assert output == ''

    def test_prints_simple_list(self, capsys):
        appr = Apprenticeship()
        appr._duties = {1: 'Apprentice', 2: 'Ship'}
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
        appr._duties = {1: 'Test!'}

        htmlTemplate = '''<html>\n<head>\n<title>DevOps Engineer Duties</title>\n</head>\n<body>\n<ul>\n<li>Test!</li>\n</ul>\n</body>\n</html>'''

        assert appr.create_html() == htmlTemplate

    def test_inserts_duties_as_list_items(self):
        appr = Apprenticeship()
        appr._duties = {
            1: 'Focus on learning', 
            2: 'Look after yourself', 
            3: 'Read the road signs in Geoguessr and just lock in a guess early'
            }

        html = appr.create_html()

        assert "<li>Focus on learning</li>" in html
        assert "<li>Look after yourself</li>" in html

    def test_outputs_to_html_document(self, tmp_path):
        appr = Apprenticeship()
        appr._duties = {1: 'Egg', 2: 'Salad', 3: 'Sando'}

        test_html_path = tmp_path / 'test.html'
        appr.output_html(test_html_path)
        html_file = open(test_html_path)
        output = html_file.read()

        assert "<li>Egg</li>" in output
        assert "<li>Salad</li>" in output
        assert "<li>Sando</li>" in output

class TestThemes:
    def test_bootcamp_theme_duties(self):
        appr = Apprenticeship()
        
        expected = {
        1: "Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage.",
        2: "Duty 2 Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members.",
        3: "Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review.",
        4: "Duty 4 Work as part of an agile team, and explore new ways of working, rapidly responding to changing user needs and with a relentless focus on the user experience. Understand the importance of continual improvement within a blameless culture.",
        13: "Duty 13 Accept ownership of changes; embody the DevOps culture of 'you build it, you run it', with a relentless focus on the user experience."
        }

        output = appr.get_duties_for_theme('bootcamp')

        assert output == expected