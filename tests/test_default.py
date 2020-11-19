def inc(x: int) -> int:
    return x + 1


def test_answer_incorrect() -> None:
    assert True == (inc(3) != 5)


def test_answer_correct() -> None:
    assert inc(3) == 4
