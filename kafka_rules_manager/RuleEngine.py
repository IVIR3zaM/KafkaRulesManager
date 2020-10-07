from datetime import datetime
from re import search
from re import IGNORECASE
from dateparser import parse
from typing import Tuple


class MessageStatuses:
    READY = "ready"
    NEW = "new"


class Rule:

    def __init__(self,
                 message_regex: str,
                 new_status: str = MessageStatuses.READY,
                 schedule_date_string: str = None,
                 flags: int = IGNORECASE
                 ):
        self.message_regex = message_regex
        self.new_status = new_status
        self.schedule_date_string = schedule_date_string
        self.flags = flags


class Message:

    def __init__(self, message: str, status: str, should_send_at: datetime = None):
        self.message = message
        self.status = status
        self.should_send_at = should_send_at


class Engine:

    def __init__(self, rules: Tuple[Rule]):
        self.rules = rules

    def process_message(self, message: Message):
        for rule in self.rules:
            if search(rule.message_regex, message.message, rule.flags) is not None:
                message.status = rule.new_status

                if rule.schedule_date_string is not None:
                    message.should_send_at = parse(rule.schedule_date_string)
                break
