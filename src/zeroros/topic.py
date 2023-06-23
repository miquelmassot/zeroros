def validate_topic(topic):
    # Verify that the topic has no spaces
    if " " in topic:
        raise ValueError("Topic name cannot contain spaces")

    # Verify that the topic starts with a slash
    if not topic.startswith("/"):
        raise ValueError("Topic name must start with a slash")

    # Verify that the topic does not end with a slash
    if topic.endswith("/"):
        raise ValueError("Topic name must not end with a slash")
    return topic
