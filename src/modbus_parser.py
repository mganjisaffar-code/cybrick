"""
Cybrick - Modbus TCP Parser
"""

from dataclasses import dataclass


@dataclass
class ModbusPacket:
    transaction_id: int
    protocol_id: int
    length: int
    unit_id: int
    function_code: int


class ModbusParser:

    @staticmethod
    def parse(data: bytes):

        if len(data) < 8:
            raise ValueError("Invalid Modbus TCP packet")

        transaction_id = int.from_bytes(data[0:2], "big")
        protocol_id = int.from_bytes(data[2:4], "big")
        length = int.from_bytes(data[4:6], "big")
        unit_id = data[6]
        function_code = data[7]

        return ModbusPacket(
            transaction_id,
            protocol_id,
            length,
            unit_id,
            function_code,
        )
