# Git 트러블슈팅 기록

이 문서는 템플릿입니다. 실습 전에는 완료 증빙으로 제출하지 않습니다.
각 사례에 실제 명령·출력·커밋 링크를 넣으세요.

## amend — A

- 참여자 / 역할: ysh (@netrunnerr25) / A
- 상태: 로컬 amend 실습 완료 (2026-10-15), PR 리뷰·승인은 별도 진행
- 상황: push 전 최근 커밋의 메시지에 잘못된 함수명이 들어갔다.
- 절차: CONTRIBUTING의 A 담당 변경만 stage하고 아직 push하지 않은 최근 커밋의 메시지를 수정했다.

```sh
git status --short --branch
git log -5 --oneline
git diff --check
git add docs/CONTRIBUTING.md
git commit -m "docs: describe temperature branch naming rules"
git log -1 --format='%H %s'
git commit --amend -m "docs: define team branch naming and commit rules"
git log -1 --format='%H %s'
git status --short
```

- 수정 전 실제 출력:

```text
2721900a19a59cdf786f38f612799c52d0fef10a docs: describe temperature branch naming rules
```

- 수정 후 실제 출력:

```text
393795e3537eb5f6a33a55e2adbcd42d19619654 docs: define team branch naming and commit rules
```

- 결과: 메시지와 커밋 해시가 변경되었다. amend 직후 `git status --short` 출력은 비어 있었다.
- 내용 검증: `git diff 2721900a19a59cdf786f38f612799c52d0fef10a 393795e3537eb5f6a33a55e2adbcd42d19619654 --exit-code`가 출력 없이 종료 코드 0으로 끝나 파일 내용이 같음을 확인했다.
- 브랜치: `feature/ysh-collaboration-docs`. E와의 동일 기준 커밋 확인은 별도 확인이 필요하다.
- 증빙: [수정 후 커밋](https://github.com/1st0Groom/B2-2/commit/393795e3537eb5f6a33a55e2adbcd42d19619654), [담당 Issue #10](https://github.com/1st0Groom/B2-2/issues/10), [충돌 실습 Issue #22](https://github.com/1st0Groom/B2-2/issues/22). 수정 전 커밋은 push하지 않았다.
- 선택 이유: 최근 로컬 커밋의 메시지만 수정하기 위해서.
- 주의점: 커밋 해시가 바뀐다. 이 실습은 push 전에 한다.

## reset --soft — B

- 참여자 / 역할: TODO
- 상태: 미실습
- 상황: push 전 최근 커밋을 취소하고 변경은 유지하려 한다.
- 절차: `git reset --soft HEAD~1`, `git status`, `git diff --cached`, 다시 커밋
- 실제 명령 / 출력: TODO
- 결과 / 증빙 링크: TODO
- 선택 이유: 커밋을 취소하면서 변경을 staged 상태로 유지하기 위해서.
- 주의점: 직전 커밋이 존재해야 한다. 공유·push된 커밋에는 이 실습을 하지 않는다.

## revert — C

- 참여자 / 역할: C — 이성준 (@Opdata) / 실행 및 기록
- 상태: 완료
- 상황: 개인 feature 브랜치 `feature/opdata-collaboration-docs`에 README 끝 `실습용 잘못된 안내: main에 직접 push한다.`를 commit·push했다.
- 절차: `git revert <잘못된커밋해시>`, 다시 push
- 실제 명령 / 출력:

```sh
$ git commit -m "docs: add intentionally incorrect direct-push instruction for revert practice"
$ git log -1 --oneline
d1736e3 docs: add intentionally incorrect direct-push instruction for revert practice
$ git push
   1726bee..d1736e3  feature/opdata-collaboration-docs -> feature/opdata-collaboration-docs
$ git revert d1736e3 --no-edit
[feature/opdata-collaboration-docs ec60562] Revert "docs: add intentionally incorrect direct-push instruction for revert practice"
 1 file changed, 1 deletion(-)
$ git push
   d1736e3..ec60562  feature/opdata-collaboration-docs -> feature/opdata-collaboration-docs
$ git log --oneline -3
ec60562 Revert "docs: add intentionally incorrect direct-push instruction for revert practice"
d1736e3 docs: add intentionally incorrect direct-push instruction for revert practice
1726bee docs: add README execution instructions for average script
```

- 원래 커밋 / 취소 커밋 / PR 링크: `d1736e3` / `ec60562` / [PR #24](https://github.com/1st0Groom/B2-2/pull/24)
- 결과: README에서 잘못된 안내 줄이 제거되었고, 원래 커밋과 취소 커밋이 모두 히스토리에 남았다. 17번 줄 실행 안내(`1726bee`)는 그대로 유지되었다.
- 선택 이유: 공개된 히스토리를 유지하면서 반대 변경을 새 커밋으로 남기기 위해서.
- 주의점: 일반 커밋 하나를 대상으로 실습한다. merge commit은 사용하지 않는다.

## stash / stash pop — D, E

- 실행자: D (`hay-dev2024`)
- 확인 및 공동 기록 작성자: E (`1st0Groom`, PR에서 확인 예정)
- 상태: 실행 완료 — E 확인 대기
- 상황: 추적 중인 파일에 미커밋 변경이 있는 상태에서 브랜치 전환이 필요하다.
- 절차: `git stash push -m "practice: preserve pending README edit"`, 브랜치 전환, 원래 브랜치 복귀, `git stash pop`
- 실제 명령:

  ```sh
  git status --short --branch
  git diff -- README.md
  git stash push -m "practice: preserve pending README edit"
  git stash list
  git switch main
  git switch feature/hay-collaboration-docs
  git stash pop
  git status --short --branch
  git diff -- README.md
  ```

- 실행 전 상태: `feature/hay-collaboration-docs`에서 `README.md`가 수정된 unstaged 상태였다.
- stash 확인: `stash@{0}: On feature/hay-collaboration-docs: practice: preserve pending README edit`
- 실행 결과: `main` 전환 후 원래 브랜치로 복귀했으며, `stash pop`으로 README 실행 안내 한 줄이 정상 복원되었다. pop 성공 후 stash 항목은 삭제되었다.
- 결과 / 증빙 링크: Issue #20, PR 생성 후 링크 추가 예정
- 선택 이유: 미완성 변경을 커밋하지 않고 잠시 보관하기 위해서.
- 주의점: 기본 stash는 새 untracked 파일을 보관하지 않는다. pop 충돌 시 stash가 남을 수 있으므로 상태를 확인한다.
