# 충돌 해결 기록

충돌 1은 작성 템플릿이며, 충돌 2는 실제 발생한 충돌과 해결 내용을 기록했습니다. 미완료 항목은 후속 작업 후 작성합니다.

## 충돌 1 — README 실행 안내

- 해결자: D(실명)
- 상대: C(실명)
- 상태: 미실습
- 두 브랜치가 출발한 커밋: TODO
- 브랜치 / 파일: TODO / README.md
- 상황: 같은 줄을 서로 다른 실행 안내로 수정하고 C의 PR을 먼저 병합했다.

### 실제 충돌 마커

```text
TODO: 실제 <<<<<<< / ======= / >>>>>>> 블록 붙여넣기
```

### 명령과 해결

```sh
# 실제 수행한 명령으로 교체
```

- 선택한 최종 문장과 이유: TODO
- 검증 명령과 출력: TODO
- 결과 PR / 해결 커밋 링크: TODO
- 상대 팀원 확인: TODO
- 배운 점: TODO

## 충돌 2 — CONTRIBUTING 작업 시작 절차

- 해결자: E (SeungEon)
- 상대: A (ysh)
- 상태: 충돌 해결·A 확인·PR #26 병합 완료. 기록의 증빙 링크를 후속 PR에서 보완한다.
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
- 결과 PR / 해결 커밋 링크: [PR #26](https://github.com/1st0Groom/B2-2/pull/26), [해결 merge commit 33c2a4b](https://github.com/1st0Groom/B2-2/commit/33c2a4b9248ae2c95fd8cf0ab91a72ebb35e5ca3), [main 병합 8a806a6](https://github.com/1st0Groom/B2-2/commit/8a806a6380ad8461dd46d333e3881ed2e1c70e7f).
- 상대 팀원 확인: [A의 리뷰·승인](https://github.com/1st0Groom/B2-2/pull/26#pullrequestreview-5529273018). Issue·브랜치 생성 및 최신 main 확인·작업 공유 의도가 모두 보존되었음을 확인했고, 이 기록의 TODO 보완을 요청했다.
- 커밋 구조 확인: `33c2a4b`의 부모는 E의 변경 `d35c053b117dabdc75e25e9838091f9761c8fc71`과 A 문서 PR이 병합된 `09b7a4a43233ef1d54fcfdf1b5b06b63275fb188`이다. `git merge-base d35c053b117dabdc75e25e9838091f9761c8fc71 5ca673ef6936cd7f479ae3db9dcccabb1d10a7ab`의 실제 출력은 `bf0304e7c57d12b08f92aedaceaa6c8898421fdd`였다.
- 배운 점: 같은 줄을 병렬로 수정하면 충돌할 수 있으며, 양쪽 변경의 의도를 확인한 뒤 내용을 통합해야 한다.
