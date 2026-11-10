"""Promo-code pricing using test-driven development.

Business rules:
- SAVE10: 10% off, rounding the discount down.
- FLAT5: $5 off when subtotal is at least $20.
- WELCOME: 15% off through December 31, 2026.
- Codes ignore surrounding whitespace and capitalization.
- Invalid, expired, or ineligible codes raise PromoError.
- Final totals cannot be negative.

All monetary amounts are integer cents.
"""

from datetime import date


class PromoError(ValueError):
    """Raised when a promotional code cannot be applied."""


def apply_promo(subtotal_cents: int, code: str, today: date) -> int:
    """Calculate the total after applying a valid promotional code."""

    normalized_code = code.strip().upper()

    if normalized_code == "SAVE10":
        discount = subtotal_cents // 10

    elif normalized_code == "FLAT5":
        if subtotal_cents < 2_000:
            raise PromoError("FLAT5 requires a $20 minimum")

        discount = 500

    elif normalized_code == "WELCOME":
        if today > date(2026, 12, 31):
            raise PromoError("WELCOME promo code has expired")

        discount = (subtotal_cents * 15) // 100

    else:
        raise PromoError("Unsupported promo code")

    return max(subtotal_cents - discount, 0)
