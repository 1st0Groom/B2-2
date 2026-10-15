# 협업 규칙

작업 시작: 최신 main 확인 후 담당 작업과 충돌 가능성 공유

## 브랜치 전략과 이름 — A 담당

- main은 실행 가능한 상태를 유지한다. 직접 push하지 않는다.
- 작업은 Issue 생성 → 최신 main 확인 → feature 브랜치 → PR → 리뷰 → 승인 → 병합 순서로 한다.
- 브랜치 이름: `feature/<영문이름>-<작업>` (예: `feature/kim-temperature`).
- 공유 브랜치의 히스토리를 재작성하지 않는다. 합의 없는 force push와 rebase를 하지 않는다.

## 커밋 메시지 — A 담당

- `feat: add Celsius to Fahrenheit conversion`
- `fix: reject empty input in average function`
- `docs: document stash recovery steps`
- 변경 대상과 효과를 적는다. `update`, `fix`, `temp`, `wip`, `final`, `bug fix`만 적지 않는다.

## PR 작성 — B 담당

본문에 `Closes #실제이슈번호`, What(변경), Why(이유), How(검증 명령과 결과)를 적는다.
검증하지 않은 항목은 완료로 표시하지 않는다.
최소 다른 팀원 1명의 승인 후 병합한다. 모든 feature 브랜치는 PR로 main에 병합한다.

## 리뷰 — B 담당

- 본인 PR을 제외하고 각자 최소 2개 PR을 리뷰한다.
- 모든 PR에 특정 파일·라인에 근거한 실질 코멘트 1개 이상을 남긴다.
- LGTM만 작성하지 않는다. 입력 경계, 사용 예시, 설명의 정확성 등을 확인한다.
- 작성자는 답글을 남기고 필요한 수정을 커밋한다. 리뷰어는 수정 내용을 확인한다.
- 각자 최소 한 번 본인 PR에 리뷰를 반영하고 증빙 링크를 제출한다.

## 충돌 대응 — E 담당

충돌 발생 → 상대 팀원에게 상황 공유 → 양쪽 의도 확인 → 해결 → 실행 확인 → 커밋 → 기록 순서로 한다.
해결자는 `docs/conflict-resolution.md`에 시작 커밋, 브랜치, 파일, 마커, 명령, 이유, 결과를 적는다.
상대 팀원은 최종 결과가 자신의 의도를 보존하는지 확인한다.

> 이 문서는 준비된 초안이다. A/B/E는 맡은 부분을 읽고 팀 합의에 맞게 수정하여 자신의 두 번째 PR로 제출한다.
