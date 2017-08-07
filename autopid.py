""" The examing auto-turning pid system """


class AutoPID(object):
    """
    PIDProcessor:
    the standard PIDProcessor
    """

    def __init__(self, kP, kD, kI, target):
        """
        __init__:
        Args:
            kP(double):
            kD(double):
            kI(double):
            target(double):
        """
        self.k_p = kP
        self.k_d = kD
        self.k_i = kI
        self.target_value = target
        self.prev_points = []
        self.prev_dt = []
        self.error_dt = 0.0
        self.error_ddt = 0.0

    def output_normal(self, input_value):
        """
        output_normal:
            output the needed power using the current state

        Note:
            input_value is not the error but the current state
        """
        # updating prev list
        error_value = self.target_value - input_value
        self.prev_points.append(input_value)
        self.update_curve()
        # updating P value
        # -1 is the middle value of error_dt, so k_p should be increasing before and decreasing after
        if len(self.prev_points) == 1:
            test_p = self.target_value * 0.8
        else:
            print(self.error_dt)

        return error_value * self.k_p + self.error_dt * self.k_d

    def update_curve(self):
        """
        update_curve:
            update info about curve
        """
        if len(self.prev_points) > 5:
            sample_length = 5
            prev_value = self.prev_points[4]
        else:
            sample_length = len(self.prev_points)
            prev_value = self.prev_points[len(self.prev_points) - 1]
        self.error_dt = (
            self.prev_points[0] - prev_value) / (sample_length * 1.0)
        self.prev_dt.append(self.error_dt)
        if len(self.prev_points) > 5:
            prev_dt = self.prev_dt[4]
        else:
            prev_dt = self.prev_dt[len(self.prev_points) - 1]
        self.error_ddt = (self.prev_dt[0] - prev_dt) / (sample_length * 1.0)
