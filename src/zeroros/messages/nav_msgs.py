from typing import List

from . import Message
from .geometry_msgs import PoseWithCovariance, TwistWithCovariance
from .std_msgs import Header


class Odometry(Message):
    def __init__(
        self,
        header=Header(),
        child_frame_id="",
        pose=PoseWithCovariance(),
        twist=TwistWithCovariance(),
    ):
        self.header = header  # type: Header
        self.child_frame_id = child_frame_id  # type: str
        self.pose = pose  # type: PoseWithCovariance
        self.twist = twist  # type: TwistWithCovariance

    def __str__(self):
        return "Odometry(header={}, child_frame_id={}, pose={}, twist={})".format(
            self.header, self.child_frame_id, self.pose, self.twist
        )

    def to_json(self):
        return {
            "header": self.header.to_json(),
            "child_frame_id": self.child_frame_id,
            "pose": self.pose.to_json(),
            "twist": self.twist.to_json(),
        }

    def from_json(self, json):
        self.header.from_json(json["header"])
        self.child_frame_id = json["child_frame_id"]
        self.pose.from_json(json["pose"])
        self.twist.from_json(json["twist"])


class Path(Message):
    def __init__(self, header=Header(), poses: List[PoseWithCovariance] = []):
        self.header = header  # type: Header
        self.poses = poses  # type: list

    def __str__(self):
        return "Path(header={}, poses={})".format(self.header, self.poses)

    def to_json(self):
        return {
            "header": self.header.to_json(),
            "poses": [pose.to_json() for pose in self.poses],
        }

    def from_json(self, json):
        self.header.from_json(json["header"])
        self.poses = [PoseWithCovariance().from_json(pose) for pose in json["poses"]]
