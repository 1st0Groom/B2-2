# 충돌 해결 기록

아래는 작성 템플릿이며 아직 실습한 기록이 아닙니다. 실제 출력과 링크로 교체하세요.

## 충돌 1 — README 실행 안내

- 해결자: D (`hay-dev2024`)
- 상대: C — 이성준 (`Opdata`)
- 상태: 해결 및 커밋 완료 — E 확인 완료, C 확인 대기
- 두 브랜치가 출발한 커밋: `bf0304e7c57d12b08f92aedaceaa6c8898421fdd`
- 브랜치 / 파일: `feature/hay-collaboration-docs`, `feature/opdata-collaboration-docs` / `README.md`
- 상황: 같은 줄을 서로 다른 실행 안내로 수정하고 C의 PR을 먼저 병합했다.

### 실제 충돌 마커

```text
<<<<<<< HEAD
실행 방법: Python 3.10 이상에서 각 파일을 직접 실행
=======
실행 방법: 프로젝트 루트에서 python src/average.py 실행
>>>>>>> origin/main
```

### 명령과 해결

```sh
git status --short --branch
git fetch origin
git merge origin/main
# Auto-merging README.md
# CONFLICT (content): Merge conflict in README.md
# Automatic merge failed; fix conflicts and then commit the result.
```

- 선택한 최종 문장: `실행 방법: Python 3.10 이상에서 프로젝트 루트의 각 파일을 직접 실행한다. 예: python src/average.py`
- 선택 이유: D의 Python 버전·전체 파일 실행 안내와 C의 프로젝트 루트·average 실행 예시를 모두 보존했다.
- 검증 명령과 출력:

  ```text
  python src/temperature.py  → 212.0
                               검증 완료: 숫자 입력 5개와 문자열 TypeError 예시 통과
  python src/text_count.py   → 9
  python src/average.py      → 20.0
  python src/discount.py     → 8000.0
  python src/time_convert.py → (1, 1, 1)
  ```

- 결과 PR / 해결 커밋 링크: [PR #25](https://github.com/1st0Groom/B2-2/pull/25) / [`cf7db10`](https://github.com/1st0Groom/B2-2/commit/cf7db10)
- 상대 팀원 확인: E의 [충돌 해결 확인 리뷰](https://github.com/1st0Groom/B2-2/pull/25#discussion_r4280045006) 완료, C 확인 대기
- 배운 점: 같은 시작 커밋에서 같은 줄을 다르게 수정하면 나중에 main을 merge할 때 Git이 어느 내용을 선택할지 판단하지 못해 충돌이 발생한다. 양쪽 의도를 확인한 뒤 마커를 제거하고 결과를 검증해야 한다.

## 충돌 2 — CONTRIBUTING 작업 시작 절차

- 해결자: E(실명)
- 상대: A(실명)
- 상태: 미실습
- 두 브랜치가 출발한 커밋: TODO
- 브랜치 / 파일: TODO / docs/CONTRIBUTING.md
- 상황: 같은 줄을 서로 다르게 수정하고 A의 PR을 먼저 병합했다.
- 실제 충돌 마커: TODO
- 실제 명령과 해결 과정: TODO
- 최종 내용과 선택 이유: TODO
- 검증 명령과 결과: TODO
- 결과 PR / 해결 커밋 링크: TODO
- 상대 팀원 확인: TODO
- 배운 점: TODO
