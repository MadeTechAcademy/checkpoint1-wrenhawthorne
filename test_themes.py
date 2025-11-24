from themes import print_duties_list

def test_empty_list_returns_none():
    duties = []
    result = print_duties_list(duties)
    expected = None

    assert result == expected