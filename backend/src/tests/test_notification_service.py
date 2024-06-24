# backend/src/tests/test_notification_service.py

from src.services.notification_service import NotificationService


def test_send_notification(mocker):
    # Mock the print function to test notification sending without actual printing
    mock_print = mocker.patch("builtins.print")

    service = NotificationService()
    result = service.send_notification("testuser@example.com", "This is a test notification.")

    # Assert the print function was called with the correct message
    mock_print.assert_called_with("Sending notification to testuser@example.com: This is a test notification.")

    # Assert the result is True
    assert result is True
