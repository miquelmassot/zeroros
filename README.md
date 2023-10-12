<p align="center">
<img src="imgs/logo.png?raw=true)" width="600"/>
</p>

# Zero-dependency ROS-like middleware for Python
This library is intended to be used for small projects that require a simple middleware
for communication between processes. It is not intended to be a replacement for ROS.

<p align="center">
    <a href="https://pypi.org/project/zeroros/">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/zeroros">
    </a>
    <a href="https://github.com/miquelmassot/zeroros/actions/workflows/python-publish.yml">
        <img alt="Wheels" src="https://github.com/miquelmassot/zeroros/actions/workflows/python-publish.yml/badge.svg">
    </a>
    <a href="https://github.com/miquelmassot/zeroros">
    	<img src="https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-blue.svg" alt="platforms" />
    </a>
    <a href="https://github.com/miquelmassot/zeroros">
    	<img src="https://static.pepy.tech/badge/zeroros" alt="Downloads" />
    </a>
    <a href="https://github.com/miquelmassot/zeroros/blob/main/LICENSE">
        <img alt="License" src="https://img.shields.io/badge/License-BSD_3--Clause-blue.svg">
    </a>
    <br/>
</p>

## Why ZeroROS?
See these discussions in [ROS Discourse](https://discourse.ros.org/t/teaching-with-ros-or-zeroros-at-university/32124) and this one in [reddit/ROS](https://www.reddit.com/r/ROS/comments/14kh7pt/teaching_ros_zeroros_at_university_students/).

## Installation
Use pip to install the library:

```bash
pip install zeroros
```

## Usage
The library is composed of three main classes: `Publisher`,  `Subscriber` and 
`MessageBroker`.

### MessageBroker
The `MessageBroker` class is used to create a message broker that can be used by
publishers and subscribers to communicate with each other.

```python
from zeroros import MessageBroker

broker = MessageBroker()
```

### Publisher
The `Publisher` class is used to publish messages to a topic. The constructor takes two
arguments: the topic name and the message type. The topic name is a string, while the
message type is a Python class. The message type is used to serialize and deserialize
messages.

```python
from zeroros import Publisher

pub = Publisher("topic_name", String)
pub.publish("Hello world!")
```

### Subscriber
The `Subscriber` class is used to subscribe to a topic and receive messages. The constructor
takes two arguments: the topic name and the message type. The topic name is a string, while
the message type is a Python class. The message type is used to serialize and deserialize
messages.

```python
import time
from zeroros import Subscriber

def callback(msg):
    print(msg)

sub = Subscriber("topic_name", String, callback)
while True:
    # Do something else
    time.sleep(1)

# Stop the subscriber
sub.stop()
```

### Messages
The library comes with a few built-in messages that can be used out of the box. The
following messages are available:

* `std_msgs.String`
* `std_msgs.Int`
* `std_msgs.Float`
* `std_msgs.Bool`
* `std_msgs.Header`
* `geometry_msgs.Vector3`
* `geometry_msgs.Vector3Stamped`
* `geometry_msgs.Twist`
* `geometry_msgs.Quaternion`
* `geometry_msgs.Pose`
* `geometry_msgs.PoseStamped`
* `geometry_msgs.PoseWithCovariance`
* `geometry_msgs.TwistWithCovariance`
* `nav_msgs.Odometry`
* `nav_msgs.Path`
* `sensors_msgs.LaserScan`
* More to come...

