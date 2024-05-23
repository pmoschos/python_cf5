from typing import NewType
# Allows creating distinct types based on existing types

UserId = NewType('UserId', int)

def get_user(user_id: UserId) -> None:
    pass
