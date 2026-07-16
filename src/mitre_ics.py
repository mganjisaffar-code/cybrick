from mitre_ics import MITREICSDatabase


def test_load_default_techniques():
    db = MITREICSDatabase()

    db.load_default()

    assert db.count() == 2


def test_find_mitre_technique():
    db = MITREICSDatabase()

    db.load_default()

    result = db.find_by_id("T0804")

    assert result is not None
    assert result.name == "Block Command Message"
    assert result.tactic == "Impair Process Control"
