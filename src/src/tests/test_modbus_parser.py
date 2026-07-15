from src.modbus_parser import ModbusParser


def test_protocol_name():
    parser = ModbusParser()
    assert parser.protocol_name() == "Modbus TCP"


def test_modbus_port():
    parser = ModbusParser()
    assert parser.is_modbus_port(502)


def test_non_modbus_port():
    parser = ModbusParser()
    assert not parser.is_modbus_port(80)
