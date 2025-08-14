from plyer import notification
import time

def health_notification_system():
    # First notification
    notification.notify(
        title="PLEASE DRINK WATER",
        message="Drinking 4 to 5 litres of water every day keeps you hydrated.",
        timeout=10
    )
    time.sleep(2 * 60)  # Wait 2 minutes

    # Second notification
    notification.notify(
        title="TIME FOR EXERCISE",
        message="Daily exercise keeps the doctor away.",
        timeout=5
    )
    time.sleep(3 * 60)  # Wait 3 minutes

if __name__ == "__main__":
    health_notification_system()
