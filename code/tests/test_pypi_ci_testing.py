from pypi_ci_testing import hello


def test_hello_returns_a_message() -> None:
    assert hello().startswith("Hello from ")
