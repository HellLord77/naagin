from enum import IntEnum


class FriendshipStateEnum(IntEnum):
    SENT = 1
    RECEIVED = 2
    ACCEPTED = 3
    RETRACTED = 4
    BLOCKED = 5
    UNINVITED = 6
    REJECTED = 7
