"""
Cybrick Modbus TCP Parser

Initial implementation for future Modbus TCP packet analysis.
"""

class ModbusParser:
    def __init__(self):
        self.supported_port = 502

    def protocol_name(self):
        return "Modbus TCP"

    def is_modbus_port(self, port):
        return port == self.supported_port


if __name__ == "__main__":
    parser = ModbusParser()
    print(parser.protocol_name())
