import time
from datetime import datetime


def sleep(duration):
    if duration < 0.0:
        return
    else:
        time.sleep(duration)


class Rate:
    """
    Convenience class for sleeping in a loop at a specified rate
    """

    def __init__(self, frequency_hz):
        """
        Constructor.
        @param frequency_hz: Frequency rate in Hz to determine sleeping
        @type  frequency_hz: float
        """
        self.last_time = float(datetime.timestamp(datetime.utcnow()))
        self.sleep_dur = 1.0 / frequency_hz

    def _remaining(self, curr_time):
        """
        Calculate the time remaining for rate to sleep.
        @param curr_time: current time
        @type  curr_time: L{Time}
        @return: time remaining
        @rtype: L{Time}
        """
        # detect time jumping backwards
        if self.last_time > curr_time:
            self.last_time = curr_time

        # calculate remaining time
        elapsed = curr_time - self.last_time
        return self.sleep_dur - elapsed

    def remaining(self):
        """
        Return the time remaining for rate to sleep.
        @return: time remaining
        @rtype: L{Time}
        """
        curr_time = float(datetime.timestamp(datetime.utcnow()))
        return self._remaining(curr_time)

    def sleep(self):
        """
        Attempt sleep at the specified rate. sleep() takes into
        account the time elapsed since the last successful
        sleep().
        """
        curr_time = float(datetime.timestamp(datetime.utcnow()))
        sleep(self._remaining(curr_time))
        self.last_time = self.last_time + self.sleep_dur

        # detect time jumping forwards, as well as loops that are
        # inherently too slow
        if curr_time - self.last_time > self.sleep_dur * 2:
            self.last_time = curr_time


if __name__ == "__main__":
    import random

    r = Rate(10.0)
    curr_time = float(datetime.timestamp(datetime.utcnow()))
    while True:
        diff = 1.0 / (float(datetime.timestamp(datetime.utcnow())) - curr_time)
        curr_time = float(datetime.timestamp(datetime.utcnow()))
        x = random.random() / 10.0
        print(diff, x)
        # Random time-lenght long computation
        time.sleep(x)
        r.sleep()
