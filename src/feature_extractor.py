from modbus_parser import ModbusParser


class FeatureExtractor:

    @staticmethod
    def extract(packet: bytes):

        modbus = ModbusParser.parse(packet)

        return {
            "packet_length": len(packet),
            "unit_id": modbus.unit_id,
            "function_code": modbus.function_code,
            "transaction_id": modbus.transaction_id,
        }
