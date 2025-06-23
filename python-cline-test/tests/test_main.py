"""Tests for the main module.

This module contains unit tests for the main.py module,
demonstrating proper testing practices for Cline rules validation.
"""

import pytest
from unittest.mock import patch
from src.main import hello_world, calculate_sum, get_user_info


class TestHelloWorld:
    """Test cases for hello_world function."""

    def test_hello_world_returns_string(self):
        """Test that hello_world returns a string."""
        result = hello_world()
        assert isinstance(result, str)

    def test_hello_world_contains_expected_text(self):
        """Test that hello_world returns expected message."""
        result = hello_world()
        assert "Hello from Python Cline Test!" in result

    @patch("src.main.logger")
    def test_hello_world_logs_message(self, mock_logger):
        """Test that hello_world logs the greeting message."""
        hello_world()
        mock_logger.info.assert_called_once()


class TestCalculateSum:
    """Test cases for calculate_sum function."""

    def test_calculate_sum_empty_list(self):
        """Test sum of empty list."""
        result = calculate_sum([])
        assert result == 0

    def test_calculate_sum_single_number(self):
        """Test sum of single number."""
        result = calculate_sum([5])
        assert result == 5

    def test_calculate_sum_multiple_numbers(self):
        """Test sum of multiple numbers."""
        result = calculate_sum([1, 2, 3, 4, 5])
        assert result == 15

    def test_calculate_sum_negative_numbers(self):
        """Test sum with negative numbers."""
        result = calculate_sum([-1, -2, 3, 4])
        assert result == 4

    def test_calculate_sum_zero_included(self):
        """Test sum with zero included."""
        result = calculate_sum([0, 1, 2])
        assert result == 3

    def test_calculate_sum_invalid_input_type(self):
        """Test that non-list input raises TypeError."""
        with pytest.raises(TypeError, match="Input must be a list"):
            calculate_sum("not a list")

    def test_calculate_sum_invalid_element_type(self):
        """Test that non-integer elements raise ValueError."""
        with pytest.raises(ValueError, match="All elements must be integers"):
            calculate_sum([1, 2, "3", 4])

    def test_calculate_sum_mixed_invalid_types(self):
        """Test that mixed invalid types raise ValueError."""
        with pytest.raises(ValueError, match="All elements must be integers"):
            calculate_sum([1, 2.5, 3])


class TestGetUserInfo:
    """Test cases for get_user_info function."""

    def test_get_user_info_valid_id(self):
        """Test getting user info with valid ID."""
        result = get_user_info(123)

        assert isinstance(result, dict)
        assert result["id"] == 123
        assert result["name"] == "User 123"
        assert result["email"] == "user123@example.com"
        assert result["active"] is True

    def test_get_user_info_different_valid_id(self):
        """Test getting user info with different valid ID."""
        result = get_user_info(456)

        assert result["id"] == 456
        assert result["name"] == "User 456"
        assert result["email"] == "user456@example.com"

    def test_get_user_info_zero_id_raises_error(self):
        """Test that zero ID raises ValueError."""
        with pytest.raises(ValueError, match="User ID must be positive"):
            get_user_info(0)

    def test_get_user_info_negative_id_raises_error(self):
        """Test that negative ID raises ValueError."""
        with pytest.raises(ValueError, match="User ID must be positive"):
            get_user_info(-1)

    def test_get_user_info_large_id(self):
        """Test getting user info with large ID."""
        result = get_user_info(999999)

        assert result["id"] == 999999
        assert result["name"] == "User 999999"

    @patch("src.main.logger")
    def test_get_user_info_logs_retrieval(self, mock_logger):
        """Test that get_user_info logs the retrieval."""
        get_user_info(123)
        mock_logger.info.assert_called_once_with("Retrieved user info for ID 123")


class TestIntegration:
    """Integration tests combining multiple functions."""

    def test_workflow_with_user_data(self):
        """Test a complete workflow using multiple functions."""
        # Get user info
        user = get_user_info(1)
        assert user["id"] == 1

        # Use user ID in calculation
        user_numbers = [user["id"], 2, 3]
        total = calculate_sum(user_numbers)
        assert total == 6

        # Generate greeting
        greeting = hello_world()
        assert isinstance(greeting, str)
