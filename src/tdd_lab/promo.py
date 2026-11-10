"""Promo-code pricing -- TDD (Red-Green-Refactor).

Business rules (from the product owner):

* SAVE10 - 10% off the subtotal (round the discount DOWN to a whole cent).
* FLAT5 - $5.00 off, but only when the subtotal is at least $20.00.
* WELCOME - 15% off, valid only on or before 2026-12-31.
* Codes are case-insensitive and surrounding whitespace is ignored.
* An unknown, expired, or ineligible code must raise PromoError.
* The total can never go below zero.

All money is integer cents. Dates are datetime.date.
"""

from datetime import date


class PromoError(ValueError):
    """Raised when a promo code cannot be applied."""


def apply_promo(subtotal_cents: int, code: str, today: date) -> int:
    """Return the new total in cents after applying a promo code."""

    # Normalize the code to ignore capitalization and surrounding spaces.
    normalized_code = code.strip().upper()

    # SAVE10: Apply a 10% discount, rounding down to a whole cent.
    if normalized_code == "SAVE10":
        discount = subtotal_cents // 10
        return max(subtotal_cents - discount, 0)

    # FLAT5: Apply a $5 discount only when subtotal is at least $20.
    if normalized_code == "FLAT5":
        if subtotal_cents < 2_000:
            raise PromoError("FLAT5 requires a $20 minimum")

        return max(subtotal_cents - 500, 0)

    # WELCOME: Apply a 15% discount through December 31, 2026.
    if normalized_code == "WELCOME":
        if today > date(2026, 12, 31):
            raise PromoError("WELCOME promo code has expired")

        discount = (subtotal_cents * 15) // 100
        return max(subtotal_cents - discount, 0)

    # Reject unknown promotional codes.
    raise PromoError("Unsupported promo code")