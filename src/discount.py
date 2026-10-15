from math import isfinite


def discounted_price(price, percent):
    """유한한 가격과 0~100 할인율로 계산. 예: (10000, 20) → 8000."""
    if not isfinite(price) or price < 0:
        raise ValueError("가격은 유한한 0 이상의 숫자여야 합니다.")
    if not isfinite(percent) or not 0 <= percent <= 100:
        raise ValueError("할인율은 0~100이어야 합니다.")
    # shortcut: 학습용 실수 계산이며 실제 결제에 사용하려면 Decimal과 반올림 규칙을 적용한다.
    return price * (1 - percent / 100)


if __name__ == "__main__":
    assert discounted_price(10000, 20) == 8000
    assert discounted_price(10000, 100) == 0
    for price, percent in [(-1, 20), (100, 101), (float("inf"), 10)]:
        try:
            discounted_price(price, percent)
        except ValueError:
            pass
        else:
            raise AssertionError("잘못된 가격 또는 할인율은 거부해야 합니다.")
    print(discounted_price(10000, 20))
