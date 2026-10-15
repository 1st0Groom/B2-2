# 충돌 해결 기록

충돌 1은 작성 템플릿이며, 충돌 2는 실제 발생한 충돌과 해결 내용을 기록했습니다. 미완료 항목은 후속 작업 후 작성합니다.

## 충돌 1 — README 실행 안내

- 해결자: D (`hay-dev2024`)
- 상대: C — 이성준 (`Opdata`)
- 상태: 해결 및 커밋 완료 — C/E 확인 완료
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
- 상대 팀원 확인: C의 [의도 보존 확인 리뷰](https://github.com/1st0Groom/B2-2/pull/25#pullrequestreview-5529465738), E의 [충돌 해결 확인 리뷰](https://github.com/1st0Groom/B2-2/pull/25#discussion_r4280045006)
- 배운 점: 같은 시작 커밋에서 같은 줄을 다르게 수정하면 나중에 main을 merge할 때 Git이 어느 내용을 선택할지 판단하지 못해 충돌이 발생한다. 양쪽 의도를 확인한 뒤 마커를 제거하고 결과를 검증해야 한다.

## 충돌 2 — CONTRIBUTING 작업 시작 절차

- 해결자: E (SeungEon)
- 상대: A (ysh)
- 상태: 파일 내용 해결 완료, 해결 커밋 및 상대 확인 대기
- 두 브랜치의 공통 기준 커밋: `bf0304e7c57d12b08f92aedaceaa6c8898421fdd`
- 작업 브랜치: `feature/SeungEon-collaboration-docs`
- 병합 대상: `origin/main` (`09b7a4a43233ef1d54fcfdf1b5b06b63275fb188`)
- 파일: `docs/CONTRIBUTING.md`
- 상황: 같은 줄을 서로 다르게 수정하고 A의 PR을 먼저 병합했다. E의 브랜치에서 최신 main을 병합하면서 같은 hunk의 내용 충돌이 발생했다.

### 실제 충돌 마커

```text
<<<<<<< HEAD
작업 시작: 최신 main 확인 후 담당 작업과 충돌 가능성 공유
=======
작업 시작: Issue 생성 후 feature/ysh-collaboration-docs 브랜치 생성
>>>>>>> origin/main
```

### 실제 명령과 해결 과정

```sh
git fetch origin
git merge origin/main
```

자동 병합이 실패하여 CONTRIBUTING.md의 충돌 마커 구간을 아래 문장으로 교체했다.

```text
작업 시작: Issue 생성 → 최신 main 확인 → 담당 작업과 충돌 가능성 공유 → feature/<영문이름>-<작업> 브랜치 생성
```

- 선택 이유: A의 Issue·브랜치 생성 안내와 E의 최신 main 확인·작업 공유 안내를 하나의 순서로 통합하여 양쪽 의도를 보존했다.
- 검증: 협업 규칙 파일에서 충돌 마커가 제거되고 위 문장이 포함된 것을 확인했다. 기록 문서의 마커는 증빙으로 보존했다.
- 결과 PR / 해결 커밋 링크: TODO (커밋·push 후 작성)
- 상대 팀원 확인: TODO (A의 리뷰 후 작성)
- 배운 점: 같은 줄을 병렬로 수정하면 충돌할 수 있으며, 양쪽 변경의 의도를 확인한 뒤 내용을 통합해야 한다.

## Codex 활용 기록 — B / Kfri

- 작성일: 2026-10-15
- 활용 목적: Git 실습 안내, 문서 수정, PR 작성 및 리뷰 반영 보조
- 본인 수행: 로컬 커밋, `reset --soft` 실행, staged diff 확인, 재커밋
- Codex 수행:
  - B 담당 PR·리뷰 규칙 정리
  - 실제 커밋 해시와 제공된 출력에 근거한 복구 실습 기록 작성
  - PR #27 제목·본문 정리 및 Issue #30 연결
  - Opdata의 리뷰에 따라 중복 문장 한 줄 삭제
  - 수정 커밋 `576fccc` 생성 및 push

### 관련 증빙

- [담당 Issue #30](https://github.com/1st0Groom/B2-2/issues/30)
- [문서 및 복구 실습 PR #27](https://github.com/1st0Groom/B2-2/pull/27)
- [리뷰 반영 커밋 576fccc](https://github.com/1st0Groom/B2-2/commit/576fccc)
- soft reset 실습 해시: 취소 전 `5e842c5` → 재커밋 `d63e6c6`
- 상세 실습 기록: [troubleshooting-log.md의 B 항목](troubleshooting-log.md#reset---soft--b)

### 기록 범위

보존되지 않은 터미널 출력은 생성하지 않았으며, 누락된 증빙과 실패한 중간 시도는 실습 기록에 구분했다. 이 항목은 B의 Codex 활용 내역이며, B가 A/E 충돌 해결을 수행했다는 의미는 아니다. GitHub 링크는 결과물을 확인하는 자료이며 Codex 대화 자체를 증명하지는 않는다. 대화 캡처는 아직 이 문서에 첨부하지 않았다.
