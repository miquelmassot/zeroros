from zeroros import MessageBroker


def main():
    _ = MessageBroker()
    print("Running message broker in a separate thread.")
    print("Press Ctrl+C to stop.")


if __name__ == "__main__":
    main()
