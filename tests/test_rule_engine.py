from rule_engine import RuleEngine


def test_rule_engine_initialization():
    engine = RuleEngine()

    result = engine.evaluate({})

    assert result is None


def test_modbus_rule_detection():
    engine = RuleEngine()

    result = engine.evaluate({
        "function_code": 8
    })

    assert result is not None
    assert result["severity"] == "high"
    assert result["mitre"] == "T0804"
