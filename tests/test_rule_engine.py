from rule_engine import RuleEngine


def test_rule_engine_initialization():
    engine = RuleEngine()

    result = engine.evaluate({})

    assert result is None
