def count_without_whitespace(text: str) -> int:
    """모든 공백 문자를 제외한 글자 수. 문자열이 아니면 TypeError 발생.

    예: '안녕 세상' → 4.
    """
    if not isinstance(text, str):
        raise TypeError("text는 문자열이어야 합니다.")
    return sum(not character.isspace() for character in text)


if __name__ == "__main__":
    assert count_without_whitespace("안녕 세상") == 4
    assert count_without_whitespace(" \t\n") == 0
    assert count_without_whitespace("") == 0
    for invalid in (["ab", " ", "cd"], None, 123):
        try:
            count_without_whitespace(invalid)
        except TypeError:
            pass
        else:
            raise AssertionError("문자열이 아닌 입력은 거부해야 합니다.")

    print(count_without_whitespace("Python Git"))
