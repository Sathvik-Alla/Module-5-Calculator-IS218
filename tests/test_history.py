from app.history import History
from app.calculation import Calculation


def test_history_add_and_show():
    h = History()
    c = Calculation("add", 1, 2, 3)

    h.add(c)
    df = h.show()

    assert len(df) == 1
    assert df.iloc[0]["result"] == 3


def test_history_clear():
    h = History()
    c = Calculation("add", 1, 2, 3)

    h.add(c)
    h.clear()

    assert len(h.show()) == 0


def test_history_save_load(tmp_path):
    h = History()
    c = Calculation("add", 2, 3, 5)
    h.add(c)

    file = tmp_path / "history.csv"
    h.save(file)

    h2 = History()
    h2.load(file)

    assert len(h2.show()) == 1

def test_history_load_missing_file():
    h = History()
    h.load("file_that_does_not_exist.csv")

    df = h.show()
    assert df.empty

