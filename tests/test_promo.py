"""Tests for promotional discount calculations."""

from datetime import date

import pytest

from tdd_lab.promo import PromoError, apply_promo

TODAY = date(2026, 11, 9)


def test_save10_takes_ten_percent_off():
    assert apply_promo(10_000, "SAVE10", TODAY) == 9_000


def test_rounds_discount_down():
    # 10% of 1005 is 100.5 cents.
    # Round the discount down to 100 cents.
    assert apply_promo(1_005, "SAVE10", TODAY) == 905


def test_flat5_at_minimum():
    # Exactly $20 qualifies for the $5 discount.
    assert apply_promo(2_000, "FLAT5", TODAY) == 1_500


def test_flat5_below_minimum():
    # $19.99 does not qualify for the discount.
    with pytest.raises(PromoError):
        apply_promo(1_999, "FLAT5", TODAY)