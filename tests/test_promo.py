"""Tests for promotional discount calculations."""

from datetime import date

import pytest

from tdd_lab.promo import PromoError, apply_promo

TODAY = date(2026, 11, 9)


def test_save10_takes_ten_percent_off():
    assert apply_promo(10_000, "SAVE10", TODAY) == 9_000


def test_rounds_discount_down():
    # 10% of 1005 is 100.5 cents.
    # Round down to 100 cents.
    assert apply_promo(1_005, "SAVE10", TODAY) == 905


def test_flat5_at_minimum():
    # Exactly $20 qualifies.
    assert apply_promo(2_000, "FLAT5", TODAY) == 1_500


def test_flat5_below_minimum():
    # $19.99 does not qualify.
    with pytest.raises(PromoError):
        apply_promo(1_999, "FLAT5", TODAY)


def test_welcome_valid_on_last_day():
    assert apply_promo(
        10_000, "WELCOME", date(2026, 12, 31)
    ) == 8_500


def test_welcome_expired():
    with pytest.raises(PromoError):
        apply_promo(
            10_000, "WELCOME", date(2027, 1, 1)
        )


def test_welcome_rounds_discount_down():
    # 15% of 1005 = 150.75 cents.
    # Discount rounds down to 150.
    assert apply_promo(1_005, "WELCOME", TODAY) == 855


def test_case_insensitive_and_whitespace():
    assert apply_promo(
        10_000, "  sAvE10  ", TODAY
    ) == 9_000


def test_unknown_code():
    with pytest.raises(PromoError):
        apply_promo(10_000, "INVALID", TODAY)


def test_total_never_negative():
    # A negative subtotal must not result in a negative total.
    assert apply_promo(-500, "SAVE10", TODAY) == 0


def test_zero_subtotal():
    assert apply_promo(0, "SAVE10", TODAY) == 0