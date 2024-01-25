import numpy as np

from . import Message
from .std_msgs import Header


class Vector3(Message):
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x  # type: float
        self.y = y  # type: float
        self.z = z  # type: float

    def __str__(self):
        return "Vector3(x={}, y={}, z={})".format(self.x, self.y, self.z)

    def to_json(self):
        return {"x": self.x, "y": self.y, "z": self.z}

    def from_json(self, json):
        self.x = json["x"]
        self.y = json["y"]
        self.z = json["z"]


class Vector3Stamped(Message):
    def __init__(self, header=Header(), vector=Vector3()):
        self.header = header  # type: Header
        self.vector = vector  # type: Vector3

    def __str__(self):
        return "Vector3Stamped(header={}, vector={})".format(self.header, self.vector)

    def to_json(self):
        return {"header": self.header.to_json(), "vector": self.vector.to_json()}

    def from_json(self, json):
        self.header.from_json(json["header"])
        self.vector.from_json(json["vector"])


class Twist(Message):
    def __init__(self, linear=Vector3(), angular=Vector3()):
        self.linear = linear  # type: Vector3
        self.angular = angular  # type: Vector3

    def __str__(self):
        return "Twist(linear={}, angular={})".format(self.linear, self.angular)

    def to_json(self):
        return {"linear": self.linear.to_json(), "angular": self.angular.to_json()}

    def from_json(self, json):
        self.linear.from_json(json["linear"])
        self.angular.from_json(json["angular"])


class Quaternion(Message):
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 0.0):
        self.x = x  # type: float
        self.y = y  # type: float
        self.z = z  # type: float
        self.w = w  # type: float

    def __str__(self):
        return "Quaternion(x={}, y={}, z={}, w={})".format(
            self.x, self.y, self.z, self.w
        )

    def from_euler(self, roll: float, pitch: float, yaw: float):
        cy = np.cos(yaw * 0.5)
        sy = np.sin(yaw * 0.5)
        cp = np.cos(pitch * 0.5)
        sp = np.sin(pitch * 0.5)
        cr = np.cos(roll * 0.5)
        sr = np.sin(roll * 0.5)

        self.w = cy * cp * cr + sy * sp * sr
        self.x = cy * cp * sr - sy * sp * cr
        self.y = sy * cp * sr + cy * sp * cr
        self.z = sy * cp * cr - cy * sp * sr

    def to_euler(self):
        roll = np.arctan2(
            2.0 * (self.w * self.x + self.y * self.z),
            1.0 - 2.0 * (self.x * self.x + self.y * self.y),
        )
        pitch = np.arcsin(2.0 * (self.w * self.y - self.z * self.x))
        yaw = np.arctan2(
            2.0 * (self.w * self.z + self.x * self.y),
            1.0 - 2.0 * (self.y * self.y + self.z * self.z),
        )
        return roll, pitch, yaw

    def to_json(self):
        return {"x": self.x, "y": self.y, "z": self.z, "w": self.w}

    def from_json(self, json):
        self.x = json["x"]
        self.y = json["y"]
        self.z = json["z"]
        self.w = json["w"]


class Pose(Message):
    def __init__(self, position=Vector3(), orientation=Quaternion()):
        self.position = position  # type: Vector3
        self.orientation = orientation  # type: Quaternion

    def __str__(self):
        return "Pose(position={}, orientation={})".format(
            self.position, self.orientation
        )

    def to_json(self):
        return {
            "position": self.position.to_json(),
            "orientation": self.orientation.to_json(),
        }

    def from_json(self, json):
        self.position.from_json(json["position"])
        self.orientation.from_json(json["orientation"])


class PoseStamped(Message):
    def __init__(self, header=None, pose=Pose()):
        self.header = header  # type: Header
        self.pose = pose  # type: Pose

    def __str__(self):
        return "PoseStamped(header={}, pose={})".format(self.header, self.pose)

    def to_json(self):
        return {"header": self.header.to_json(), "pose": self.pose.to_json()}

    def from_json(self, json):
        self.header.from_json(json["header"])
        self.pose.from_json(json["pose"])


class PoseWithCovariance(Message):
    def __init__(self, pose=Pose(), covariance=[]):
        self.pose = pose  # type: Pose
        self.covariance = covariance  # type: list

    def __str__(self):
        return "PoseWithCovariance(pose={}, covariance={})".format(
            self.pose, self.covariance
        )

    def to_json(self):
        return {"pose": self.pose.to_json(), "covariance": self.covariance}

    def from_json(self, json):
        self.pose.from_json(json["pose"])
        self.covariance = json["covariance"]


class TwistWithCovariance(Message):
    def __init__(self, twist=Twist(), covariance=[]):
        self.twist = twist  # type: Twist
        self.covariance = covariance  # type: list

    def __str__(self):
        return "TwistWithCovariance(twist={}, covariance={})".format(
            self.twist, self.covariance
        )

    def to_json(self):
        return {"twist": self.twist.to_json(), "covariance": self.covariance}

    def from_json(self, json):
        self.twist.from_json(json["twist"])
        self.covariance = json["covariance"]
