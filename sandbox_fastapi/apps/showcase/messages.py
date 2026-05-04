"""
Message types for the showcase consumers.
"""

from typing import Any, Literal

from chanx.messages.base import BaseMessage
from pydantic import BaseModel


# Chat messages
class ChatPayload(BaseModel):
    message: str


class ChatMessage(BaseMessage):
    """Chat message for the basic chat consumer."""

    action: Literal["chat"] = "chat"
    payload: ChatPayload


class ChatNotificationMessage(BaseMessage):
    """Chat notification message."""

    action: Literal["chat_notification"] = "chat_notification"
    payload: ChatPayload


# Reliable chat messages
class ReliableChatPayload(BaseModel):
    message: str


class ReliableChatMessage(BaseMessage):
    """Reliable chat message."""

    action: Literal["reliable_chat"] = "reliable_chat"
    payload: ReliableChatPayload


class ReliableChatNotificationMessage(BaseMessage):
    """Reliable chat notification message."""

    action: Literal["reliable_chat_notification"] = "reliable_chat_notification"
    payload: ReliableChatPayload


# Notification messages
class NotificationPayload(BaseModel):
    type: str = "user"
    message: str


class NotificationMessage(BaseMessage):
    """Notification message."""

    action: Literal["notification"] = "notification"
    payload: NotificationPayload


class NotificationBroadcastMessage(BaseMessage):
    """Notification broadcast message."""

    action: Literal["notification_broadcast"] = "notification_broadcast"
    payload: NotificationPayload


# Analytics messages
class AnalyticsPayload(BaseModel):
    event: str
    data: Any = None


class AnalyticsMessage(BaseMessage):
    """Analytics message."""

    action: Literal["analytics"] = "analytics"
    payload: AnalyticsPayload


class AnalyticsNotificationMessage(BaseMessage):
    """Analytics notification message."""

    action: Literal["analytics_notification"] = "analytics_notification"
    payload: AnalyticsPayload


class SystemNotify(BaseMessage):
    action: Literal["system_notify"] = "system_notify"
    payload: str


class SystemPeriodicNotify(BaseMessage):
    action: Literal["system_periodic_notify"] = "system_periodic_notify"
    payload: str


# Passthrough event messages (forwarded directly to WebSocket clients)
class UserJoinedNotification(BaseMessage):
    """Notification when a user joins the chat."""

    action: Literal["user_joined_notification"] = "user_joined_notification"
    payload: ChatPayload


class UserLeftNotification(BaseMessage):
    """Notification when a user leaves the chat."""

    action: Literal["user_left_notification"] = "user_left_notification"
    payload: ChatPayload
