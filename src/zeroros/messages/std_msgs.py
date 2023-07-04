import time

from . import Message


class Header:
    def __init__(self, seq: int = 0, stamp: float = None, frame_id: str = ""):
        self.seq = seq
        self.frame_id = frame_id
        self.stamp = stamp
        if stamp is None:
            self.stamp = time.time()

    def __str__(self):
        return "Header:\n  - seq={}\n  - stamp={}\n  - frame_id={})\n".format(
            self.seq, self.stamp, self.frame_id
        )

    def to_json(self):
        return {"seq": self.seq, "stamp": self.stamp, "frame_id": self.frame_id}

    def from_json(self, json):
        self.seq = json["seq"]
        self.stamp = json["stamp"]
        self.frame_id = json["frame_id"]


class GenericTypeData(Message):
    def __init__(self, data):
        self.data = data

    def to_json(self):
        return {"data": self.data}

    def from_json(self, json):
        self.data = json["data"]


class String(GenericTypeData):
    def __init__(self, data: str = ""):
        super().__init__(data)

    def __str__(self):
        return "String:\n  - data={}\n".format(self.data)


class Int(GenericTypeData):
    def __init__(self, data: int = 0):
        super().__init__(data)

    def __str__(self):
        return "Int:\n  - data={}\n".format(self.data)


class Int8(Int):
    def __str__(self):
        return "Int8:\n  - data={}\n".format(self.data)


class Int16(Int):
    def __str__(self):
        return "Int16:\n  - data={}\n".format(self.data)


class Int32(Int):
    def __str__(self):
        return "Int32:\n  - data={}\n".format(self.data)


class Int64(Int):
    def __str__(self):
        return "Int64:\n  - data={}\n".format(self.data)


class Float(GenericTypeData):
    def __init__(self, data: float = 0.0):
        super().__init__(data)

    def __str__(self):
        return "Float:\n  - data={}\n".format(self.data)


class Float32(Float):
    def __str__(self):
        return "Float32:\n  - data={}\n".format(self.data)


class Float64(Float):
    def __str__(self):
        return "Float64:\n  - data={}\n".format(self.data)


class Bool(GenericTypeData):
    def __init__(self, data: bool = False):
        super().__init__(data)

    def __str__(self):
        return "Bool:\n  - data={}\n".format(self.data)
