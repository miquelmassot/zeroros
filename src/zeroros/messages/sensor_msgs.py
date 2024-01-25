import numpy as np

from . import Message
from .std_msgs import Header


class LaserScan(Message):
    def __init__(self, ranges=[], intensitites=[], angles=[]):
        self.header = Header()
        self.angle_min = None
        self.angle_max = None
        self.angle_increment = None
        self.time_increment = None
        self.scan_time = None
        self.range_min = None
        self.range_max = None
        self.ranges = np.array(ranges)
        self.angles = np.array(angles)
        # Change NaNs to range_max
        if np.isnan(self.ranges).any():
            self.ranges[np.isnan(self.ranges)] = self.range_max
        self.intensities = np.array(intensitites)

    def __str__(self):
        msg = "LaserScan Message\n"
        msg += str(self.header)
        msg += "Angle Min:    " + str(self.angle_min) + "\n"
        msg += "Angle Max:    " + str(self.angle_max) + "\n"
        msg += "Angle Inc:    " + str(self.angle_increment) + "\n"
        msg += "Time Inc:     " + str(self.time_increment) + "\n"
        msg += "Scan Time:    " + str(self.scan_time) + "\n"
        msg += "Range Min:    " + str(self.range_min) + "\n"
        msg += "Range Max:    " + str(self.range_max) + "\n"
        msg += "Ranges:       " + str(self.ranges) + "\n"
        msg += "Intensities:  " + str(self.intensities) + "\n"
        msg += "Angles:       " + str(self.angles) + "\n"
        return msg

    def to_json(self):
        return {
            "header": self.header.to_json(),
            "angle_min": self.angle_min,
            "angle_max": self.angle_max,
            "angle_increment": self.angle_increment,
            "time_increment": self.time_increment,
            "scan_time": self.scan_time,
            "range_min": self.range_min,
            "range_max": self.range_max,
            "ranges": self.ranges.tolist(),
            "intensities": self.intensities.tolist(),
            "angles": self.angles.tolist(),
        }

    def from_json(self, msg):
        self.header.from_json(msg["header"])
        self.angle_min = msg["angle_min"]
        self.angle_max = msg["angle_max"]
        self.angle_increment = msg["angle_increment"]
        self.time_increment = msg["time_increment"]
        self.scan_time = msg["scan_time"]
        self.range_min = msg["range_min"]
        self.range_max = msg["range_max"]
        self.ranges = np.array(msg["ranges"])
        self.intensities = np.array(msg["intensities"])
        self.angles = np.array(msg["angles"])
