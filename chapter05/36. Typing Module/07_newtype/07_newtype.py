from typing import NewType

# Allows creating distinct types based on existing types

UserId = NewType('UserId', int)

def get_user(user_id: UserId) -> None:
    """
    Retrieves a user based on their user ID.

    Parameters:
    user_id (UserId): The ID of the user to retrieve, represented as a distinct type.
    """
    pass
