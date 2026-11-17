"""Small example application for the pull request CI demo."""


def greet(name: str) -> str:
    """Return a greeting for ``name``."""
    return f"Hello, {name}!"


def main() -> None:
    """Print the example greeting."""
    print(greet("CI, is so cool, here!"))


if __name__ == "__main__":
    main()
