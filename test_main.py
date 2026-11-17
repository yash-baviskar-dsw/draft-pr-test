"""Tests for the example application."""

from main import greet


def test_greet_returns_personalized_greeting() -> None:
    """The greeting includes the provided name."""
    assert greet("Python") == "Hello, Python!"
