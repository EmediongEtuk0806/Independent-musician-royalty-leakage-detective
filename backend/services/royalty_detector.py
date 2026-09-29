def calculate_royalty_leakage(
    streams: int,
    expected_rate: float,
    actual_royalty: float,
) -> dict:
    expected_royalty = streams * expected_rate
    potential_leakage = expected_royalty - actual_royalty

    if potential_leakage > 0:
        status = "POTENTIAL_LEAKAGE"
    else:
        status = "NO_LEAKAGE_DETECTED"

    return {
        "expected_royalty": round(expected_royalty, 2),
        "actual_royalty": round(actual_royalty, 2),
        "potential_leakage": round(max(potential_leakage, 0), 2),
        "status": status,
    }