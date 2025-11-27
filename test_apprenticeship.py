from Apprenticeship import Apprenticeship
from Duty import Duty
from duties import duties_map
from themes import themes_map

class TestPrintDuties:
    def test_prints_empty_list(self, capsys):
        appr = Apprenticeship(duties_map, themes_map)
        appr.duties = {}
        appr.print_duties()
        captured = capsys.readouterr()
        output = captured.out

        assert output == ''

    def test_prints_simple_list(self, capsys):
        appr = Apprenticeship(duties_map, themes_map)
        appr.duties = {1: Duty(1, 'Apprentice'), 2: Duty(1, 'Ship')}
        appr.print_duties()
        captured = capsys.readouterr()
        output = captured.out

        assert output == 'Apprentice\n\nShip\n\n'

    def test_prints_list_of_duties(self, capsys):
        appr = Apprenticeship(duties_map, themes_map)
        appr.print_duties()
        captured = capsys.readouterr()
        output = captured.out

        firstSlice = output[:50]
        lastSlice = output[-50:]

        assert firstSlice == 'Duty 1 Script and code in at least one general pur'
        assert lastSlice == ' with a relentless focus on the user experience.\n\n'

class TestOutputHtml:
    def test_returns_html_template(self):
        test_duties = {1: Duty(1, 'Test!')}
        appr = Apprenticeship(test_duties, themes_map)

        htmlTemplate = '''<html>\n<head>\n<title>DevOps Engineer Duties</title>\n</head>\n<body>\n<ul>\n<li>Test!</li>\n</ul>\n</body>\n</html>'''

        output = appr.create_html()

        print('out', output)

        assert output == htmlTemplate

    def test_inserts_duties_as_list_items(self):
        test_duties = {
            1: Duty(1, 'Focus on learning'), 
            2: Duty(2, 'Look after yourself'), 
            3: Duty(3, 'Read the road signs in Geoguessr and just lock in a guess early')
            }
        appr = Apprenticeship(test_duties, themes_map)

        html = appr.create_html()

        assert "<li>Focus on learning</li>" in html
        assert "<li>Look after yourself</li>" in html

    def test_outputs_to_html_document(self, tmp_path):
        test_duties = {1: Duty(1, 'Egg'), 2: Duty(2, 'Salad'), 3: Duty(3, 'Sando')}
        appr = Apprenticeship(test_duties, themes_map)

        test_html_path = tmp_path / 'test.html'
        appr.output_html(test_html_path)
        html_file = open(test_html_path)
        output = html_file.read()

        assert "<li>Egg</li>" in output
        assert "<li>Salad</li>" in output
        assert "<li>Sando</li>" in output

class TestThemes:
    def test_bootcamp_theme_duties(self):
        appr = Apprenticeship(duties_map, themes_map)

        output = appr.get_duties_for_theme('bootcamp')

        assert len(output) == 5
        assert output[1] == duties_map[1]
        assert output[2] == duties_map[2]
        assert output[3] == duties_map[3]
        assert output[4] == duties_map[4]
        assert output[13] == duties_map[13]

    def test_theme_duties_written_to_html(self, tmp_path):
        appr = Apprenticeship(duties_map, themes_map)

        bootcamp_duties = appr.get_duties_for_theme('bootcamp')
        appr.set_duties_for_theme(bootcamp_duties)

        test_html_path = tmp_path / 'bootcamp.html'
        appr.output_html(test_html_path)
        html_file = open(test_html_path)
        output = html_file.read()

        assert duties_map[1].description in output
        assert duties_map[2].description in output
        assert duties_map[3].description in output
        assert duties_map[4].description in output
        assert duties_map[13].description in output

        assert duties_map[5].description not in output
        assert duties_map[6].description not in output
        assert duties_map[7].description not in output
        assert duties_map[8].description not in output
        assert duties_map[9].description not in output
        assert duties_map[10].description not in output
        assert duties_map[11].description not in output
        assert duties_map[12].description not in output

#     def test_automate_theme_duties(self):
#         appr = Apprenticeship(duties_map, themes_map)
        
#         expected = {
#         5: "Duty 5 Build and operate a Continuous Integration (CI) capability, employing version control of source code and related artefacts",
#         7: "Duty 7 Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers).",
#         10: "Duty 10 Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable.",
#         }

#         output = appr.get_duties_for_theme('automate')

#         assert output == expected