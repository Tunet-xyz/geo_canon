"""Code lookups return None for input that is not a string, as for unknown codes."""

import pytest

from geo_canon.currencies import get_currency_by_code
from geo_canon.flags import get_country_by_iso
from geo_canon.iso_codes import get_jurisdiction_by_alpha2, get_jurisdiction_by_alpha3

LOOKUPS = [
    get_jurisdiction_by_alpha2,
    get_jurisdiction_by_alpha3,
    get_country_by_iso,
    get_currency_by_code,
]


@pytest.mark.parametrize("lookup", LOOKUPS, ids=lambda lookup: lookup.__name__)
@pytest.mark.parametrize(
    "value",
    [None, 42, 3.5, True, b"RO", ["RO"], {"code": "RO"}],
    ids=["none", "int", "float", "bool", "bytes", "list", "dict"],
)
def test_non_string_input_returns_none(lookup, value):
    assert lookup(value) is None


def test_string_codes_still_resolve_case_insensitively():
    assert get_jurisdiction_by_alpha2("ro") == "Romania"
    assert get_jurisdiction_by_alpha3("rou") == "Romania"
    assert get_country_by_iso("RO") == "Romania"
    euro = get_currency_by_code("eur")
    assert euro is not None
    assert euro == get_currency_by_code("EUR")
