""" The standard pidprocessor """


class PIDProcessor(object):
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

    def output_normal(self, input_value):
        """
        output_normal:
            output the needed power using the current state

        Note:
            input_value is not the error but the current state
        """
        error_value = self.target_value - input_value
        self.prev_points.append(input_value)
        sample_length = 5 if len(
            self.prev_points) > 5 else len(self.prev_points)
        prev_value = self.prev_points[4] if len(
            self.prev_points) > 5 else self.prev_points[len(self.prev_points) - 1]
        error_dt = (error_value - prev_value) / (sample_length * 1.0)
        return error_value * self.k_p + error_dt * self.k_d
