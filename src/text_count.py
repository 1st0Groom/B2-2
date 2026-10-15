def count_without_whitespace(text):
    """모든 공백 문자를 제외한 글자 수. 예: '안녕 세상' → 4."""
    return sum(not character.isspace() for character in text)


if __name__ == "__main__":
    assert count_without_whitespace("안녕 세상") == 4
    assert count_without_whitespace(" \t\n") == 0
    assert count_without_whitespace("") == 0
    print(count_without_whitespace("Python Git"))
