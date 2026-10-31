import pytest
from atm_withdrawal import withdraw, pin_check, note_breakup


# ---------- withdraw ----------
def test_simple_withdrawal():
    assert withdraw(5000, 1000, "savings", True) == 4000

def test_unknown_account():
    with pytest.raises(ValueError, match="unknown account"):
        withdraw(5000, 1000, "salary", True)

def test_zero_amount():
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(5000, 0, "savings", True)

def test_negative_amount():
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(5000, -100, "savings", True)

def test_amount_not_multiple_of_100():
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(5000, 150, "savings", True)

def test_savings_limit_exceeded():
    assert withdraw(100000, 30000, "savings", True) == "limit exceeded"

def test_savings_exactly_at_limit():
    assert withdraw(30000, 25000, "savings", True) == 5000

def test_current_account_higher_limit():
    assert withdraw(100000, 40000, "current", True) == 60000

def test_current_limit_exceeded():
    assert withdraw(100000, 60000, "current", True) == "limit exceeded"

def test_other_bank_small_amount_fee_20():
    # amount <= 10000 -> fee is only 20 (this covers the missing branch)
    assert withdraw(5000, 1000, "savings", False) == 3980

def test_other_bank_exactly_10000_fee_20():
    # boundary: 10000 is NOT > 10000
    assert withdraw(20000, 10000, "savings", False) == 9980

def test_other_bank_large_amount_fee_30():
    assert withdraw(50000, 15000, "current", False) == 34970

def test_insufficient_funds():
    assert withdraw(500, 1000, "savings", True) == "insufficient funds"

def test_insufficient_funds_due_to_fee():
    # 1000 + 20 fee = 1020 > 1000
    assert withdraw(1000, 1000, "savings", False) == "insufficient funds"

def test_balance_exactly_equals_amount_plus_fee():
    assert withdraw(1020, 1000, "savings", False) == 0


# ---------- pin_check ----------
def test_correct_pin():
    assert pin_check(1234, 1234, 0) == "ok"

def test_correct_pin_on_last_allowed_attempt():
    assert pin_check(1234, 1234, 2) == "ok"

def test_card_blocked_after_three_attempts():
    assert pin_check(1234, 1234, 3) == "card blocked"

def test_card_blocked_more_than_three_attempts():
    assert pin_check(1111, 1234, 5) == "card blocked"

def test_wrong_pin_third_attempt_blocks():
    assert pin_check(1111, 1234, 2) == "card blocked"

def test_wrong_pin_first_attempt_retry():
    assert pin_check(1111, 1234, 0) == "retry"

def test_wrong_pin_second_attempt_retry():
    assert pin_check(1111, 1234, 1) == "retry"


# ---------- note_breakup ----------
def test_note_breakup_invalid_amount():
    with pytest.raises(ValueError, match="invalid amount"):
        note_breakup(150)

def test_note_breakup_only_500s():
    assert note_breakup(1000) == (2, 0, 0)

def test_note_breakup_with_200_notes():
    assert note_breakup(700) == (1, 1, 0)

def test_note_breakup_multiple_200_notes():
    assert note_breakup(900) == (1, 2, 0)

def test_note_breakup_200_and_100_notes():
    assert note_breakup(800) == (1, 1, 1)

def test_note_breakup_without_200_notes():
    assert note_breakup(600) == (1, 0, 1)

def test_note_breakup_single_100_note():
    assert note_breakup(100) == (0, 0, 1)

def test_note_breakup_zero():
    assert note_breakup(0) == (0, 0, 0)