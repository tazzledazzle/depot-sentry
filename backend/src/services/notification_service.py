# backend/src/services/notification_service.py

class NotificationService:
    def send_notification(self, user, message):
        """
        Sends a notification to the specified user.

        :param user: The user to send the notification to.
        :param message: The message content of the notification.
        """
        # This is a mock implementation. In a real-world scenario,
        # you would integrate with an email service, Slack API, etc.
        print(f"Sending notification to {user}: {message}")
        return True


# Example usage:
if __name__ == "__main__":
    service = NotificationService()
    service.send_notification("testuser@example.com", "This is a test notification.")
