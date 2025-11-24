from themes import duties_list

def test_duties_list():
    duty1 = "Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage."
    duty13 = "Duty 13 Accept ownership of changes; embody the DevOps culture of 'you build it, you run it', with a relentless focus on the user experience."
    
    assert len(duties_list) > 10
    assert len(duties_list) == 13
    assert duties_list[0] == duty1
    assert duties_list[-1] == duty13

def test_create_simple_html_output():
    simple_html = """<html>
        <head></head>
        <body><p>Hello World!</p></body>
        </html>"""

    assert create_html_output()