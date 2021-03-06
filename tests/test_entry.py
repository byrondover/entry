import pytest
from entry import Entry


def test_new_empty_entry():
    entry = Entry()

    with pytest.raises(AttributeError):
        entry.zog


def test_new_entry_from_params():
    entry = Entry(foo="Foo Value", bar="Bar Value")
    assert entry.foo == "Foo Value"
    assert entry.bar == "Bar Value"

    with pytest.raises(AttributeError):
        entry.zog
