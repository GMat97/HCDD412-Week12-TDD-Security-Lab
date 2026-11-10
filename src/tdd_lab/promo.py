"""Promo-code pricing -- the feature you will build with TDD (Red-Green-Refactor).

Business rules (from the product owner):

* ``SAVE10``  - 10% off the subtotal (round the discount DOWN to a whole cent).
* ``FLAT5``   - $5.00 off, but only when the subtotal is at least $20.00.
* ``WELCOME`` - 15% off, valid only on or before 2026-12-31.
* Codes are case-insensitive and surrounding whitespace is ignored.
* An unknown, expired, or ineligible code must raise ``PromoError`` -- never
  silently return the full price.
* The total can never go below zero.

All money is integer cents. Dates are ``datetime.date``.

Right now this is only a stub. Write failing tests FIRST (Red), then make them
pass (Green), then clean up (Refactor).
"""
from datetime import date


class PromoError(ValueError):
    """Raised when a promo code cannot be applied."""

def apply_promo(subtotal_cents: int, code: str, today: date) -> int:
    """Return the new total in cents after applying ``code``."""
    if code == "SAVE10":
        discount = subtotal_cents // 10
        return subtotal_cents - discount

    if code == "FLAT5":
        if subtotal_cents < 2_000:
            raise PromoError("FLAT5 requires a $20 minimum")
        return subtotal_cents - 500

    raise PromoError("Unsupported promo code")