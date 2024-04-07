import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from app.io.input import read_from_file, read_from_file_with_pandas


def test_read_from_file_returns_none_for_nonexistent_file():
    assert read_from_file("nonexistent.txt") is None


def test_read_from_file_returns_correct_content(tmpdir):
    test_file = tmpdir.join("test.txt")
    test_file.write("Hello, world!")

    assert read_from_file(test_file) == "Hello, world!"


def test_read_from_file_handles_empty_file(tmpdir):
    test_file = tmpdir.join("empty.txt")
    test_file.write("")

    assert read_from_file(test_file) == ""


def test_read_from_file_with_pandas_returns_none_for_nonexistent_file():
    assert read_from_file_with_pandas("nonexistent.csv") is None


def test_read_from_file_with_pandas_returns_correct_content(tmpdir):
    test_file = tmpdir.join("test.csv")
    test_file.write("1,2,3\n4,5,6")

    assert read_from_file_with_pandas(test_file) == "1 2 3\n4 5 6"


def test_read_from_file_with_pandas_handles_empty_file(tmpdir):
    test_file = tmpdir.join("empty.csv")
    test_file.write("")

    assert read_from_file_with_pandas(test_file) is None
