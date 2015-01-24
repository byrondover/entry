import pytest
from thingstance import Thing
from thingstance.representations.json import content_type


def test_json_content_type():
    assert content_type == "application/json"


def test_empty_thing_as_json():
    thing = Thing()
    data = thing.json
    assert data == '{}\n'


def test_empty_thing_from_json():
    thing = Thing()
    thing.json = ('{}')
    assert thing.json == ('{}\n')


def test_empty_thing_from_json_with_whitespace():
    thing = Thing()

    thing.json = ('{}\n')
    assert thing.json == ('{}\n')

    thing.json = ('   {  }\n\n')
    assert thing.json == ('{}\n')


def test_unserializable__as_json():
    thing = Thing(name='foo', unserializable=pytest)
    with pytest.raises(AttributeError):
        thing.json


def test_ignore_private_as_json():
    thing = Thing()
    thing._zero = "to be removed"
    thing.one = "one value"
    thing._two = "should be removed"
    thing.two = "two value"
    thing._three = "three"

    data = thing.json
    assert data == ('{"one": "one value", "two": "two value"}\n')


def test_postaladdress_as_json():
    thing = Thing()
    thing.streetAddress = "Aviation House, 125 Kingsway"
    thing.addressLocality = "Holborn"
    thing.addressRegion = "London"
    thing.postcode = "WC2B 6NH"
    thing.addressCountry = "GB"

    data = thing.json
    assert data == ('{"addressCountry": "GB",'
                    ' "addressLocality": "Holborn",'
                    ' "addressRegion": "London",'
                    ' "postcode": "WC2B 6NH",'
                    ' "streetAddress": "Aviation House, 125 Kingsway"}\n')


def test_postaladdress_from_json():
    thing = Thing()
    thing.json = ('{"addressCountry": "GB",'
                  ' "addressLocality": "Holborn",'
                  ' "addressRegion": "London",'
                  ' "postcode": "WC2B 6NH",'
                  ' "streetAddress": "Aviation House, 125 Kingsway"}\n')

    assert thing.streetAddress == "Aviation House, 125 Kingsway"
    assert thing.addressLocality == "Holborn"
    assert thing.addressRegion == "London"
    assert thing.postcode == "WC2B 6NH"
    assert thing.addressCountry == "GB"


def test_set_of_tags_as_json():
    thing = Thing(name='foo', fields={'a', 'b', 'c', 'a'})
    data = thing.json
    assert data == ('{"fields": ["a", "b", "c"], "name": "foo"}\n')


def test_set_of_tags_from_json():
    thing = Thing()
    thing.json = ('{"fields": ["a", "b", "c"], "name": "foo"}')
    assert thing.name == 'foo'
    assert thing.fields == ['a', 'b', 'c']
