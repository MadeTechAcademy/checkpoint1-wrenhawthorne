from Apprenticeship import Apprenticeship

class TestPrintDuties:
    def test_prints_list_of_duties(self, capsys):
        Apprenticeship.print_duties()
        captured = capsys.readouterr()
        output = captured.out

        firstSlice = output[:50]
        lastSlice = output[-50:]

        assert firstSlice == 'Duty 1 Script and code in at least one general pur'
        assert lastSlice == ' with a relentless focus on the user experience.\n\n'

class TestOutputHtml:
    def test_returns_html_template(self):
        htmlTemplate = '''<html>
            <head>
            <title>DevOps Engineer Duties</title>
            </head>
            <p>Test!</p>
            </body>
            </html>'''

        assert Apprenticeship.output_html() == htmlTemplate