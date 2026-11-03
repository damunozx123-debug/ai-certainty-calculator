"""Pure, auditable arithmetic for user-provided sensitivity scenarios."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Scenario:
    monthly_variance: float
    annual_variance: float
    hypothetical_payback_days: float | None

def calculate(monthly_spend: float, variance_pct: float, assumed_audit_fee: float = 5000.0) -> Scenario:
    for name, value in (("monthly_spend", monthly_spend), ("variance_pct", variance_pct), ("assumed_audit_fee", assumed_audit_fee)):
        if not isinstance(value, (int, float)) or not (float("-inf") < value < float("inf")):
            raise ValueError(f"{name} must be finite")
    if monthly_spend < 0 or assumed_audit_fee < 0 or not 0 <= variance_pct <= 100:
        raise ValueError("Nonnegative spend/fee and percentage in [0,100] required")
    monthly = monthly_spend * variance_pct / 100
    payback = assumed_audit_fee / monthly * 30 if monthly > 0 else None
    return Scenario(monthly_variance=monthly, annual_variance=monthly * 12, hypothetical_payback_days=payback)
