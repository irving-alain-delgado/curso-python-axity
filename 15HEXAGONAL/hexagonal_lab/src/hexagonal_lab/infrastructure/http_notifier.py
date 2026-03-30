class HttpNotifier:
    def notify(self, message: str) -> None:
        print(f"Sending HTTP notification: {message}")