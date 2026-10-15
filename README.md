# 생활 Python 유틸 모음

5명이 Python 함수와 GitHub Flow 협업을 연습하는 프로젝트입니다.

## 팀원과 함수

| 팀원(실명으로 교체) | 파일 | 기능 |
|---|---|---|
| A | [temperature.py](src/temperature.py) | 섭씨를 화씨로 변환 |
| B | [text_count.py](src/text_count.py) | 공백을 제외한 글자 수 |
| C | [average.py](src/average.py) | 숫자 목록의 평균 |
| D | [discount.py](src/discount.py) | 할인 후 가격 |
| E | [time_convert.py](src/time_convert.py) | 초를 시·분·초로 변환 |

## 실행 방법

실행 방법: 프로젝트 루트에서 python src/average.py 실행

Python 3.10 이상에서 프로젝트 루트에서 실행합니다.

```sh
python src/temperature.py
python src/text_count.py
python src/average.py
python src/discount.py
python src/time_convert.py
```

각 파일은 사용 예시와 assert 검증을 포함합니다. assert 검증 시 `python -O`를 사용하지 않습니다.

## 협업 문서

- [팀 진행 가이드](MISSION_GUIDE.md)
- [협업 규칙](docs/CONTRIBUTING.md)
- [충돌 해결 기록](docs/conflict-resolution.md)
- [Git 트러블슈팅 기록](docs/troubleshooting-log.md)
- [제출 인덱스](SUBMISSION.md)

GitHub Flow를 선택한 이유: 작은 작업을 브랜치로 분리하여 main을 안정적으로 유지한다.
PR에서 리뷰와 검증을 진행한다.
승인된 작업만 병합해 변경 이유와 과정을 추적한다.
