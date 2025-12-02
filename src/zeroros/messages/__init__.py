"""This module contains all the messages that are used in ZeroROS."""


class Message:
    """Empty base class for all messages."""

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        raise NotImplementedError


from .geometry_msgs import (
    Vector3,
    Vector3Stamped,
    Twist,
    Quaternion,
    Pose,
    PoseStamped,
    PoseWithCovariance,
    TwistWithCovariance,
)  # noqa: F401
from .sensor_msgs import LaserScan  # noqa: F401
from .range_bearing_msgs import RBLaserScan  # noqa: F401
from .nav_msgs import Odometry, Path  # noqa: F401
from .std_msgs import (
    Header,
    String,
    Int,
    Int8,
    Int16,
    Int32,
    Int64,
    Float,
    Float32,
    Float64,
    Bool,
)  # noqa: F401
