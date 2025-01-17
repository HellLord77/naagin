from enum import IntEnum


class FriendshipStateEnum(IntEnum):
    SENT = 1
    RECEIVED = 2
    ACCEPTED = 3
    UNINVITED = 4
    BLOCKED = 5
    RETRACTED = 6
    REJECTED = 7
