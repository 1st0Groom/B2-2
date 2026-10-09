# 5인 팀 미션 실행 가이드

이 문서는 준비 자료입니다. 실제 PR·리뷰·충돌·복구 기록은 팀원들이 직접 수행해 남깁니다.
A~E를 실제 이름으로 교체하세요. 코드 초안은 각자 이해하고 검증·수정한 뒤 자신의 커밋으로 제출하세요.

## 1. 역할과 작업 10개

| 팀원 | Issue / PR 1 | Issue / PR 2 | 두 PR의 리뷰어 | 복구 실습 |
|---|---|---|---|---|
| A | temperature 함수와 예시 | CONTRIBUTING 브랜치·커밋 규칙, amend 기록 | B | amend |
| B | text_count 함수와 예시 | CONTRIBUTING PR·리뷰 규칙, reset 기록 | C | reset --soft |
| C | average 함수와 예시 | README 실행 안내, 충돌 1 상황 확인, revert 기록 | D | revert |
| D | discount 함수와 예시 | README 실행 안내, 충돌 1 해결, stash 기록 | E | stash 실행 |
| E | time_convert 함수와 예시 | CONTRIBUTING 충돌 대응, 충돌 2 해결, 제출 인덱스 | A | stash 확인·공동 기록 |

두 번째 PR의 문서 담당자가 기록을 취합합니다. amend/reset/revert는 각 실행자가 기록하고 D/E는 stash 기록을 함께 작성합니다.
충돌 2 기록은 E가 추가합니다. E의 두 번째 PR은 다른 두 번째 PR이 모두 병합된 후 마지막으로 병합합니다.

## 2. 저장소 준비 — A가 진행, 전원 확인

1. GitHub Organization 저장소를 만들거나 개인 저장소에 4명을 Collaborator로 초대합니다.
2. 초기 README를 가진 저장소로 시작합니다. 각 팀원이 초대를 수락합니다.
3. 새 저장소를 현재 과제 폴더와 별도의 위치에 clone합니다. 현재 폴더는 상위 저장소 안에 있으므로 여기에서 무작정 `git init`하지 않습니다.

```sh
# 주소를 실제 저장소 주소로 바꿔 실행
 git clone <저장소URL> team-git-practice
 cd team-git-practice
 git config user.name "내 이름"
 git config user.email "내 GitHub 계정에 연결된 이메일"
```

4. 초기 골격으로 README, docs, src를 준비합니다. Git은 빈 폴더를 추적하지 않으므로 src에는 `.gitkeep`을 둡니다.
5. 제공된 README·문서 템플릿은 초기 골격에 사용해도 됩니다. **src의 함수 5개는 초기 커밋에 넣지 않고 각 담당자의 첫 번째 PR에서 추가합니다.**
6. 초기 골격 업로드 뒤 main 보호를 설정하고 이후 변경은 모두 PR로 처리합니다.

GitHub Settings → Rules → Rulesets 또는 Branches에서 main 대상 규칙을 만듭니다.
- PR을 통한 변경 필수
- 승인 최소 1명
- 직접 push 및 force push 금지
- 관리자 우회도 제한, 규칙 활성 상태 확인

설정 화면의 적용 대상과 실제 활성 여부를 확인하고 증빙을 남깁니다. 사용할 수 있는 보호 기능은 저장소 공개 여부와 계정 플랜에 따라 다를 수 있으므로 설정이 적용되지 않으면 교육 담당자에게 확인합니다.

## 3. Issue 10개 만들기

각자 위 표의 작업 2개를 Issue로 생성합니다. Issue에는 담당자·변경 파일·완료 조건을 적습니다.

```markdown
제목: 섭씨→화씨 변환 함수 추가
담당자: A의 실제 이름
변경 파일: src/temperature.py
완료 조건:
- 함수와 사용 예시 작성
- 정상 값과 경계값 확인
- PR 리뷰 반영 및 승인 후 병합
```

Issue 번호를 기록합니다. 아래 명령·PR 템플릿의 자리표시자는 반드시 실제 값으로 바꿉니다.

## 4. 첫 번째 PR — 각자 함수 추가

```sh
git switch main
git pull --ff-only origin main
git switch -c feature/<영문이름>-<함수주제>
# 자신의 함수 파일만 src에 복사하고 내용을 검토·수정
python src/<자신의파일>.py
git add src/<자신의파일>.py
git commit -m "feat: add <구체적인 함수 기능>"
git push -u origin feature/<영문이름>-<함수주제>
```

`git add .` 대신 해당 작업의 파일만 추가합니다. GitHub에서 base=main, compare=자신의 브랜치로 PR을 만듭니다.

```markdown
## 연결 Issue
Closes #실제번호

## What
- 변경한 함수와 예시

## Why
- 이 기능이 필요한 이유

## How
- 실행 명령
- 실제 출력과 확인한 경계값
```

지정 리뷰어가 특정 파일/라인에 실질적인 코멘트를 남깁니다. 작성자는 답글과 수정 커밋을 남깁니다.
예: 입력이 빈 목록인 경우, 공백의 정의, 할인율의 유효 범위, 초가 음수인 경우를 확인합니다.
이미 올바르게 처리되었다면 설명·검증 예시의 실제 부족한 부분을 개선합니다. 오류나 리뷰 기록을 꾸며내지 않습니다.
전원 본인 PR에서 최소 1회 수정 반영을 남기고, 리뷰어 재확인 및 승인 후 병합합니다.
히스토리를 보여주기 쉽도록 팀은 merge commit 방식으로 통일해도 됩니다.

## 5. 두 번째 PR 준비 — 같은 기준 커밋 필수

첫 번째 PR 5개를 모두 병합한 뒤 전원이 main을 갱신합니다.
**A와 E, C와 D는 상대의 두 번째 PR이 병합되기 전에 아래 브랜치를 모두 만들어야 합니다.**

```sh
git switch main
git pull --ff-only origin main
git rev-parse HEAD
# 출력 해시를 충돌 기록의 시작 커밋에 적기
git switch -c feature/<영문이름>-collaboration-docs
```

각자 담당 문서 부분을 수정합니다. C/D는 같은 README 줄, A/E는 같은 CONTRIBUTING 줄을 아래처럼 수정합니다.

### 충돌 1: C → D 순서

README의 `실행 방법: 추후 작성` 줄을 바꿉니다.
- C: `실행 방법: 프로젝트 루트에서 python src/average.py 실행`
- D: `실행 방법: Python 3.10 이상에서 각 파일을 직접 실행`

C/D가 각각 커밋·push하고 PR을 만듭니다. C가 revert 실습과 기록을 마친 PR을 먼저 리뷰·병합합니다.
D는 자신의 브랜치에서 다음 명령을 실행합니다.

```sh
git status
# 미커밋 변경이 없음을 확인
git fetch origin
git merge origin/main
```

충돌이 발생하면 실제 마커를 기록하고 양쪽 의도를 확인합니다. 예를 들어 최종 줄을 아래처럼 정리합니다.

```text
실행 방법: Python 3.10 이상에서 프로젝트 루트의 각 파일을 직접 실행한다. 예: python src/average.py
```

마커를 모두 제거하고 실제 함수 실행을 확인합니다. D가 충돌 기록을 작성합니다.

```sh
git add README.md docs/conflict-resolution.md
git commit -m "docs: resolve conflicting README execution instructions"
git push
```

D의 PR을 E가 리뷰하고 D가 응답한 뒤 승인·병합합니다.
충돌이 없으면 시작 커밋과 수정 위치를 확인합니다. 충돌이 없었던 결과를 충돌 해결로 기록하지 않습니다.

### 충돌 2: A → E 순서

CONTRIBUTING의 `작업 시작: 협업 규칙 확인` 줄을 바꿉니다.
- A: `작업 시작: Issue 생성 후 feature/<이름>-<작업> 브랜치 생성`
- E: `작업 시작: 최신 main 확인 후 담당 작업과 충돌 가능성 공유`

A가 amend 실습 및 기록을 완료하고 PR을 먼저 병합합니다.
E는 자기 브랜치에서 `git fetch origin`, `git merge origin/main`을 실행합니다.
실제 마커를 기록하고 Issue 생성·main 갱신·작업 공유·브랜치 생성 절차를 함께 담도록 해결합니다.
문서에서 마커가 남지 않았는지 확인하고 docs/conflict-resolution.md에 충돌 2를 기록합니다.
담당 파일을 add → 해결 commit → push → A의 리뷰와 E의 응답 → 승인 순서로 진행합니다.
E의 PR은 제출 인덱스까지 정리해 마지막에 병합합니다.

## 6. 복구 실습 — 두 번째 feature 브랜치에서 진행

실습 전 `git status`와 `git log -3 --oneline`을 확인합니다. 다른 사람의 변경이나 공유 히스토리를 취소하지 않습니다.
문서의 실제 담당 내용을 활용해 실습하고 전후 출력·해시를 기록합니다.

### A: 최근 로컬 메시지 amend

담당 문서 변경을 stage하고 잘못된 함수명이 들어간 구체적인 메시지로 커밋합니다. 아직 push하지 않습니다.

```sh
git add docs/CONTRIBUTING.md
git commit -m "docs: describe temperature branch naming rules"
git log -1 --oneline
git commit --amend -m "docs: define team branch naming and commit rules"
git log -1 --oneline
```

전후 메시지와 해시를 기록하고 자신의 기록 부분만 추가 커밋한 뒤 push합니다.

### B: 로컬 커밋 취소, 변경 유지

```sh
git add docs/CONTRIBUTING.md
git commit -m "docs: define PR and review requirements"
git log -2 --oneline
git reset --soft HEAD~1
git status
git diff --cached
git commit -m "docs: define issue-linked PR and substantive review requirements"
```

취소 전 커밋이 아직 push되지 않았는지 확인합니다. 결과를 기록한 뒤 push합니다.

### C: push된 잘못된 안내 revert

먼저 README의 올바른 담당 변경을 커밋합니다. 이후 별도 커밋으로 README 끝에 `실습용 잘못된 안내: main에 직접 push한다.`를 추가합니다.

```sh
git add README.md
git commit -m "docs: add intentionally incorrect direct-push instruction for revert practice"
git log -1 --oneline
# 위 해시를 기록
git push -u origin feature/<C의영문이름>-collaboration-docs
git revert <방금기록한잘못된커밋해시>
git push
```

잘못된 문장이 사라지고 원래 커밋과 취소 커밋이 모두 남는지 확인합니다. 실제 공유 main에 잘못된 내용을 병합하지 않습니다.

### D/E: stash와 pop

D가 자기 브랜치의 추적 중인 README를 수정하되 아직 커밋하지 않습니다. E가 전후 상태를 확인하고 공동으로 기록합니다.

```sh
git status
git diff
git stash push -m "practice: preserve pending README edit"
git stash list
git switch main
git switch feature/<D의영문이름>-collaboration-docs
git stash pop
git status
git diff
```

변경이 복구되었는지 확인합니다. D는 실행자, E는 확인·공동 작성자로 기록합니다.
pop 충돌 시 상태와 stash 목록을 확인하고 충돌을 해결합니다. 변경 확인 전 stash를 삭제하지 않습니다.

### 기록 파일 공동 편집 순서

A → B → C → D/E 순서로 기록을 작성·병합하면 불필요한 문서 충돌을 줄일 수 있습니다.
각자 최신 main을 자신의 브랜치에 병합한 뒤 자기 기록 부분만 편집합니다.
같은 기록 파일을 동시에 수정했다면 앞선 실습처럼 양쪽 기록을 모두 보존하여 해결합니다.

## 7. 제출 인덱스와 히스토리

E는 각 팀원에게 Issue, PR, 리뷰, 수정 커밋, 복구 기록 링크를 받아 SUBMISSION.md를 채웁니다.
자기 PR 링크는 열린 상태에서도 적을 수 있으며 승인·병합은 실제 완료 후 체크합니다.

E의 PR까지 병합한 후 Git 히스토리를 생성합니다.

```sh
git switch main
git pull --ff-only origin main
git fetch origin
git log --oneline --graph --all > /tmp/team-git-history.txt
```

10개 PR만으로 마무리하려면 GitHub Issue에 이 텍스트를 첨부하고 SUBMISSION.md의 히스토리 증빙을 그 링크로 사용합니다.
SUBMISSION에 최종 링크를 넣기 위해 E의 PR을 병합하기 전에 증빙용 Issue를 만들고 그 Issue 링크를 미리 적습니다. 최종 병합 후 그 Issue에 실제 히스토리를 게시합니다.
저장소 안의 docs/git-history.txt로 제출하려면 추가 Issue와 PR을 만들어 파일을 커밋합니다. PR은 최소 2개이므로 추가 PR도 허용됩니다.
최종 체크박스 확인이나 링크 수정이 남았다면 추가 PR로 처리합니다. main에 직접 push하지 않습니다.

## 8. 20시간 배분

| 시간 | 할 일 |
|---|---|
| 0~2 | 저장소·초대·골격·보호 규칙 |
| 2~3 | Issue 10개·역할·규칙 합의 |
| 3~7 | 함수·예시·assert 검증 |
| 7~10 | 첫 PR 5개 리뷰·수정·병합 |
| 10~14 | 문서 작업·충돌 2회 |
| 14~17 | 복구 실습·기록 |
| 17~19 | 두 번째 PR 리뷰·병합·인덱스 |
| 19~20 | 실행·히스토리·최종 점검 |

## 9. 설명할 수 있어야 하는 개념

- 브랜치: 커밋을 가리키는 이동 가능한 이름이다. 별도 작업 흐름을 유지한다.
- GitHub Flow: main에서 작업 브랜치를 만들고 PR 리뷰 후 병합하는 흐름이다.
- PR: 변경 이유·검증·리뷰를 함께 남기고 병합을 제안한다.
- 충돌: Git이 변경을 자동으로 합치지 못하는 상황이다. 마커는 양쪽 변경 경계를 표시한다.
- reset --soft: 브랜치 위치를 되돌리면서 변경을 staged 상태로 유지한다.
- revert: 기존 커밋의 반대 변경을 새 커밋으로 남긴다.
- stash: 미커밋 작업을 잠시 보관한다. pop은 적용을 시도하고 성공하면 해당 항목을 제거한다.

선택 과제인 rebase와 CODEOWNERS는 기본 시나리오에서 제외합니다.
