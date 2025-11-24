from themes import Apprenticeship

def test_print_duties_method_prints_list(capsys):
    Apprenticeship.print_duties()
    captured = capsys.readouterr()
    output = captured.out
    
    firstSlice = output[:50]
    lastSlice = output[-50:]

    assert output != ''
    assert firstSlice == 'Duty 1 Script and code in at least one general pur'
    assert lastSlice == ' with a relentless focus on the user experience.\n\n'