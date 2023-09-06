import requests
import pytest


class TestUserAgent:
    agent_provider = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    ]

    @pytest.mark.parametrize("user_agent", agent_provider)
    def test_user_agent(self, user_agent):
        response = requests.get(
            "https://playground.learnqa.ru/ajax/api/user_agent_check",
            headers={
                "User-Agent": user_agent
            }
        )
        headers = response.json()
        platform = headers["platform"]
        assert platform != "Unknown", f"Поле 'platform' имеет значение 'Unknown'.\nUser-Agent: {user_agent}"
        browser = headers["browser"]
        assert browser != "Unknown", f"Поле 'browser' имеет значение 'Unknown'.\nUser-Agent: {user_agent}"
        device = headers["device"]
        assert device != "Unknown", f"Поле 'device' имеет значение 'Unknown'.\nUser-Agent: {user_agent}"
