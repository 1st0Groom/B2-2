def average(numbers: list[float]) -> float:
    """비어 있지 않은 숫자 목록의 평균. 예: average([1, 2, 3]) == 2."""
    if not numbers:
        raise ValueError("숫자 목록이 비어 있습니다.")
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    assert average([1, 2, 3]) == 2
    assert average([-2, 2]) == 0
    assert average([5]) == 5
    assert average([1.5, 2.5]) == 2.0
    try:
        average([])
    except ValueError:
        pass
    else:
        raise AssertionError("빈 목록은 거부해야 합니다.")
    print(average([10, 20, 30]))
