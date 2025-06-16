class MoveListHandler:
    def __init__(self):
        self.step_list_xyf = [0] * 512
        self.step_list_xyt = [0] * 512
        self.step_no = 0
        self.step_num = 0

    def initialize_move_list(self, move_list_param):
        if move_list_param:
            steps = move_list_param.split(",")
            for i, step in enumerate(steps):
                from_pos, to_pos = step.split("-")
                self.step_list_xyf[i] = int(from_pos)
                self.step_list_xyt[i] = int(to_pos)
            self.step_num = len(steps)
