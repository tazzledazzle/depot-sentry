# backend/src/routes/notification_routes.py

from flask import Blueprint, request, jsonify
from src.services.notification_service import NotificationService

notification_bp = Blueprint('notification', __name__)
notification_service = NotificationService()


@notification_bp.route('/notify', methods=['POST'])
def notify_user():
    data = request.get_json()
    user = data.get('user')
    message = data.get('message')

    if not user or not message:
        return jsonify({"error": "User and message are required"}), 400

    success = notification_service.send_notification(user, message)

    if success:
        return jsonify({"status": "Notification sent successfully"}), 200
    else:
        return jsonify({"error": "Failed to send notification"}), 500
