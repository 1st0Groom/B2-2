# Git 트러블슈팅 기록

이 문서는 템플릿입니다. 실습 전에는 완료 증빙으로 제출하지 않습니다.
각 사례에 실제 명령·출력·커밋 링크를 넣으세요.

## amend — A

- 참여자 / 역할: TODO
- 상태: 미실습
- 상황: push 전 최근 커밋의 메시지에 잘못된 함수명이 들어갔다.
- 절차: `git commit --amend -m "정확한 메시지"`
- 수정 전후 `git log -1 --oneline` 출력: TODO
- 결과 / 증빙 링크: TODO
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

- 참여자 / 역할: TODO
- 상태: 미실습
- 상황: 개인 feature 브랜치에 잘못된 안내를 commit·push했다.
- 절차: `git revert <잘못된커밋해시>`, 다시 push
- 실제 명령 / 출력: TODO
- 원래 커밋 / 취소 커밋 / PR 링크: TODO
- 결과: TODO
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
