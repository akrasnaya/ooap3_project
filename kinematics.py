import roboticstoolbox as rtb
from warning import WarningNotification

class Robot():
    def __init__(self, model):
        self.model = model
        if self.model == "puma":
            self.robot = rtb.models.DH.Puma560()
        elif self.model == "ur5":
            self.robot = rtb.models.DH.UR5()
        elif self.model == "ur10":
            self.robot = rtb.models.DH.UR10()

    def show_robot_params(self):
        return self.robot.theta


class InverseKinematics:
    def __init__(self, robot):
        self.solver = rtb.IK_LM()
        self.robot = robot

    def calculate_ik(self, pose):
        etc = self.robot.etc()
        solution = self.solver.solve(etc, pose)
        if solution.success:
            return solution.q
        else:
            WarningNotification('high', solution.reason)