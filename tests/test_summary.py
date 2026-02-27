from services.summary import get_mocked_summary


def test_mocked_summary_is_deterministic() -> None:
    a = get_mocked_summary()
    b = get_mocked_summary()
    assert a == b


def test_mocked_summary_contains_expected_sections() -> None:
    s = get_mocked_summary()
    assert "Expense summary" in s
    assert "2025-01-01" in s
    assert "Food" in s
    assert "Transport" in s
    assert "Total" in s
