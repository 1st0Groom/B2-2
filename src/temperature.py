from math import isclose


def celsius_to_fahrenheit(celsius):
    """섭씨를 화씨로 변환한다. 예: celsius_to_fahrenheit(0) == 32.

    정수와 실수를 지원하며, 물리적 유효 범위는 제한하지 않는다.
    """
    return celsius * 9 / 5 + 32


if __name__ == "__main__":
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(100) == 212
    # 소수 계산에는 부동소수점 오차가 있어 근사 비교한다.
    assert isclose(celsius_to_fahrenheit(36.5), 97.7, rel_tol=1e-9, abs_tol=1e-9)
    assert isclose(celsius_to_fahrenheit(-273.15), -459.67, rel_tol=1e-9, abs_tol=1e-9)
    print(celsius_to_fahrenheit(100))
    print("검증 완료: 5개 예시 통과")
