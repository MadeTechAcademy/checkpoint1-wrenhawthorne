from Apprenticeship import Apprenticeship

class TestPrintDuties:
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

        htmlTemplate = '''<html>
            <head>
            <title>DevOps Engineer Duties</title>
            </head>
            <p>Test!</p>
            </body>
            </html>'''

        assert appr.output_html() == htmlTemplate

    def test_inserts_duties_as_paragraphs(self):
        appr = Apprenticeship()
        appr._duties = ['Focus on learning', 'Look after yourself', 'Read the road signs in Geoguessr and just lock in a guess early']

        html = appr.output_html()

        assert "<p>Focus on learning</p>" in html
        assert "<p>Look after yourself</p>" in html