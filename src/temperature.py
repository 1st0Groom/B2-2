"""섭씨 온도를 화씨로 변환하는 함수와 실행 예시."""

from math import isclose


def celsius_to_fahrenheit(celsius: float) -> float:
    """섭씨 온도를 받아 화씨 온도를 반환한다.

    변환식은 F = C × 9 / 5 + 32이며, 정수와 실수 입력을 지원한다.
    온도의 물리적 유효 범위는 제한하지 않고 수치 변환만 수행한다.

    >>> celsius_to_fahrenheit(0)
    32.0
    >>> celsius_to_fahrenheit(-40)
    -40.0
    """
    return celsius * 9 / 5 + 32


if __name__ == "__main__":
    # 소수 연산의 오차를 고려해 기대 결과와 근사 비교한다.
    examples = (
        (0, 32),
        (100, 212),
        (-40, -40),
        (36.5, 97.7),
        (-273.15, -459.67),
    )
    for celsius, expected in examples:
        fahrenheit = celsius_to_fahrenheit(celsius)
        assert isclose(fahrenheit, expected, rel_tol=1e-9, abs_tol=1e-9)
        print(f"{celsius:g}°C → {fahrenheit:g}°F")

    print(f"검증 완료: {len(examples)}개 예시 통과")
