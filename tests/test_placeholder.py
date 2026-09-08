from src.main import build_sample_summary


def test_build_sample_summary():
    result = build_sample_summary(
        topic="quarterly revenue",
        evidence=["Revenue grew 12% QoQ.", "Operating margin improved to 18%."]
    )

    assert "quarterly revenue" in result.lower()
    assert "12%" in result
    assert "18%" in result
