# Python doesn't really have interfaces like C#.

# Instead it commonly uses:

# Abstract classes
# Protocols (modern approach)


# Protocols are a way to define a common interface for a group of classes without using inheritance.
from typing import Protocol

class Notifier(Protocol):

    def send(self) -> None:
        ... # Use ellipsis (...) to show no implementation code here

# 2. Create concrete implementations (No explicit inheritance required)
class SMSNotifier:
    def send(self, message: str) -> bool:
        print(f"Sending SMS: {message}")
        return True

class EmailNotifier:
    def send(self, message: str) -> bool:
        print(f"Sending Email: {message}")
        return True

# 3. Use the protocol as a type hint
def broadcast_alert(notifier: Notifier, alert_msg: str):
    notifier.send(alert_msg)

# Execution
sms = SMSNotifier()
email = EmailNotifier()

broadcast_alert(sms, "System maintenance at 12 PM")    # Valid
broadcast_alert(email, "System maintenance at 12 PM")  # Valid        