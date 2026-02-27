from __future__ import annotations


def get_mocked_summary() -> str:
    # Intentionally static: demo-only, no persistence, no per-user calculations.
    return (
        "Expense summary (example data)\n"
        "\n"
        "2025-01-01\n"
        "- Food: $25 (Lunch $12, Dinner $13)\n"
        "- Transport: $8 (Taxi $8)\n"
        "- Total: $33\n"
        "\n"
        "2025-01-02\n"
        "- Food: $9 (Coffee $4, Snack $5)\n"
        "- Other: $15 (Movie $15)\n"
        "- Total: $24\n"
    )
