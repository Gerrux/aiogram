from typing import Optional

from aiogram.methods import TelegramMethod
from aiogram.methods.base import TelegramType
from aiogram.utils.exceptions.base import TelegramAPIError


class RetryAfter(TelegramAPIError):
    url = "https://core.telegram.org/bots/faq#my-bot-is-hitting-limits-how-do-i-avoid-this"

    def __init__(
        self,
        method: TelegramMethod[TelegramType],
        message: str,
        retry_after: int,
    ) -> None:
        super().__init__(method=method, message=message)
        self.retry_after = retry_after

    def render_description(self) -> str:
        description = f"Flood control exceeded on method {type(self.method).__name__!r}"
        if chat_id := getattr(self.method, "chat_id", None):
            description += f" in chat {chat_id}"
        description += f". Retry in {self.retry_after} seconds."
        return description


class MigrateToChat(TelegramAPIError):
    url = "https://core.telegram.org/bots/api#responseparameters"

    def __init__(
        self,
        method: TelegramMethod[TelegramType],
        message: str,
        migrate_to_chat_id: int,
    ) -> None:
        super().__init__(method=method, message=message)
        self.migrate_to_chat_id = migrate_to_chat_id

    def render_message(self) -> Optional[str]:
        description = (
            f"The group has been migrated to a supergroup with id {self.migrate_to_chat_id}"
        )
        if chat_id := getattr(self.method, "chat_id", None):
            description += f" from {chat_id}"
        return description