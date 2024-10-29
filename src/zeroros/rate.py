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
        self.last_time = datetime.utcnow().timestamp()
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
        curr_time = datetime.utcnow().timestamp()
        return self._remaining(curr_time)

    def reset(self):
        """
        Reset the rate timer.
        """
        self.last_time = datetime.utcnow().timestamp()

    def sleep(self):
        """
        Attempt sleep at the specified rate. sleep() takes into
        account the time elapsed since the last successful
        sleep().
        """
        curr_time = datetime.utcnow().timestamp()
        sleep(self._remaining(curr_time))
        self.last_time = self.last_time + self.sleep_dur

        # detect time jumping forwards, as well as loops that are
        # inherently too slow
        if curr_time - self.last_time > self.sleep_dur * 2:
            self.last_time = curr_time


if __name__ == "__main__":
    import random

    count = 0

    r = Rate(10.0)
    curr_time = datetime.utcnow().timestamp()
    while True and count < 10:
        diff = 1.0 / (datetime.utcnow().timestamp() - curr_time)
        curr_time = datetime.utcnow().timestamp()
        x = random.random() / 10.0
        print(diff, x)
        # Random time-length long computation
        time.sleep(x)
        r.sleep()
        count += 1

    r = Rate(1.0)
    count = 0
    while True:
        x = random.random() / 10.0
        time.sleep(x)
        if r.remaining() <= 0:
            diff = 1.0 / (datetime.utcnow().timestamp() - curr_time)
            curr_time = datetime.utcnow().timestamp()
            print(diff, x, r.remaining())  # Random time-length long computation
            r.reset()
            count += 1
        if count >= 10:
            break
