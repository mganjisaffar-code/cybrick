from mitre_ics import MITREICSDatabase


def test_load_default_techniques():
    db = MITREICSDatabase()

    db.load_default()

    assert db.count() == 2
