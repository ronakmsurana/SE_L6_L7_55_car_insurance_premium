from hypothesis import given, strategies as st
from car_insurance_premium_parser import normalize_registration, total_claim_amount, driver_age

@given(st.text() | st.none())
def test_normalize_registration_no_crash(s):
    # To-Do: Using try and except complete this function.
    pass

@given(st.text() | st.none())
def test_total_claim_amount_no_crash(s):
    # To-Do: Using try and except complete this function.
    pass

@given(st.text() | st.none())
def test_driver_age_no_crash(s):
    # To-Do: Using try and except complete this function.
    pass
