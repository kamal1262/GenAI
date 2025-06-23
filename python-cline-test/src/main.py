"""Main module for Python Cline Test project.

This module serves as the entry point and contains basic functionality
for testing Cline's agentic coding rules with Python.
"""

import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def hello_world() -> str:
    """Return a simple greeting message.

    Returns:
        str: A greeting message
    """
    message = "Hello from Python Cline Test!"
    logger.info(f"Generated greeting: {message}")
    return message


def calculate_sum(numbers: list[int]) -> int:
    """Calculate the sum of a list of numbers.

    Args:
        numbers: List of integers to sum

    Returns:
        int: Sum of all numbers

    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-integer values
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")

    result = sum(numbers)
    logger.debug(f"Calculated sum of {numbers}: {result}")
    return result


def get_user_info(user_id: int) -> Dict[str, Any]:
    """Simulate getting user information.

    This is a placeholder function for testing purposes.

    Args:
        user_id: The ID of the user to retrieve

    Returns:
        Dict containing user information

    Raises:
        ValueError: If user_id is not positive
    """
    if user_id <= 0:
        raise ValueError("User ID must be positive")

    # Simulate user data
    user_data = {
        "id": user_id,
        "name": f"User {user_id}",
        "email": f"user{user_id}@example.com",
        "active": True,
    }

    logger.info(f"Retrieved user info for ID {user_id}")
    return user_data


if __name__ == "__main__":
    print(hello_world())
    print(f"Sum of [1, 2, 3, 4, 5]: {calculate_sum([1, 2, 3, 4, 5])}")
    print(f"User info: {get_user_info(123)}")
