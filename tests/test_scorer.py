from url_risk.scorer import score_url

def test_numeric_host():
    score, features = score_url("http://192.168.0.1/login")
    assert "numeric-host" in features
    assert score >= 2
