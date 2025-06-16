# position_initializer.py


class PositionInitializer:
    def __init__(self):
        self.piece_positions = [100] * 32

    def initialize_position(self, position_param):
        if not position_param:
            position_param = "I0,H0,G0,F0,E0,D0,C0,B0,A0,H2,B2,I3,G3,E3,C3,A3|A9,B9,C9,D9,E9,F9,G9,H9,I9,B7,H7,A6,C6,E6,G6,I6"
        positions = position_param.split("|")
        for i, pos in enumerate(positions[0].split(",")):
            self.piece_positions[i] = int(pos[1]) * 10 + ord(pos[0]) - ord("A")
