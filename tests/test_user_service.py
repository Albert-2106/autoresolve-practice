from src.user_service import get_user_name


def test_get_user_name():
    assert get_user_name({"name": "Albert"}) == "Albert"


def test_get_user_name_returns_none_for_none_input():
    assert get_user_name(None) is None
