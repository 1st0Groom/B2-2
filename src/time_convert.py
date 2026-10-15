def seconds_to_hms(seconds):
    """0 이상의 정수 초를 (시, 분, 초)로 변환. 예: 3661 → (1, 1, 1)."""
    if type(seconds) is not int or seconds < 0:
        raise ValueError("초는 0 이상의 정수여야 합니다.")
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds


if __name__ == "__main__":
    assert seconds_to_hms(3661) == (1, 1, 1)
    assert seconds_to_hms(0) == (0, 0, 0)
    assert seconds_to_hms(59) == (0, 0, 59)
    assert seconds_to_hms(60) == (0, 1, 0)
    assert seconds_to_hms(3599) == (0, 59, 59)
    assert seconds_to_hms(3600) == (1, 0, 0)
    assert seconds_to_hms(86400) == (24, 0, 0)
    for invalid in [-1, 1.5, True]:
        try:
            seconds_to_hms(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("잘못된 초는 거부해야 합니다.")
    print(seconds_to_hms(3661))
