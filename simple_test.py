class TestMath:
    def test_math(self):
        a = 1
        b = 3
        expected_sum = 3
        assert a + \
            b == expected_sum, f"Сумма операндов не равна ожидаемому значению: {expected_sum}"
