from calculator import calculate
import pytest

def test_reference_scenario():
    r = calculate(200_000, 35, 5_000)
    assert r.monthly_variance == 70_000
    assert r.annual_variance == 840_000
    assert r.hypothetical_payback_days == pytest.approx(5000/70000*30)

def test_zero_variance_is_not_a_payback():
    r = calculate(1000, 0)
    assert r.monthly_variance == 0
    assert r.hypothetical_payback_days is None

@pytest.mark.parametrize("spend,pct,fee",[(-1,10,0),(100,101,0),(100,-1,0),(100,10,-1),(float("nan"),10,0)])
def test_invalid_input(spend,pct,fee):
    with pytest.raises(ValueError):
        calculate(spend,pct,fee)
