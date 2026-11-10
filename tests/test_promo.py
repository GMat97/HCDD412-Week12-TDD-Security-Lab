"""Your TDD workspace. The first test is deliberately RED -- that is step one."""
from datetime import date

from tdd_lab.promo import apply_promo

TODAY = date(2026, 11, 9)


def test_save10_takes_ten_percent_off():
    assert apply_promo(10_000, "SAVE10", TODAY) == 9_000

def test_rounds_discount_down():
    # 10% of 1005 is 100.5 cents.
    # Round the discount down to 100 cents.
    assert apply_promo(1_005, "SAVE10", TODAY) == 905

