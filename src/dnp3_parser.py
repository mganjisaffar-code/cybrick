"""
Cybrick DNP3 Parser
Version 0.1
"""


class DNP3Packet:
    def __init__(self, function_code):
        self.function_code = function_code


class DNP3Parser:
    @staticmethod
    def parse(packet):
        """
        Parse a minimal DNP3 packet.

        For now, the second byte is treated as the function code.
        """
        if len(packet) < 2:
            raise ValueError("Invalid DNP3 packet")

        return DNP3Packet(function_code=packet[1])
