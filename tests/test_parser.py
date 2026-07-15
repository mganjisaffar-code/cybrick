from src.modbus_parser import ModbusParser


def test_modbus_parser():
    packet = bytes([
        0x00, 0x01,
        0x00, 0x00,
        0x00, 0x06,
        0x01,
        0x03
    ])

    result = ModbusParser.parse(packet)

    assert result.transaction_id == 1
    assert result.protocol_id == 0
    assert result.unit_id == 1
    assert result.function_code == 3
