# Git 트러블슈팅 기록

이 문서는 템플릿입니다. 실습 전에는 완료 증빙으로 제출하지 않습니다.
각 사례에 실제 명령·출력·커밋 링크를 넣으세요.

## amend — A

- 참여자 / 역할: ysh (@netrunnerr25) / A
- 상태: 로컬 amend 실습 완료 (2026-10-15), [PR #23](https://github.com/1st0Groom/B2-2/pull/23)의 [B 승인](https://github.com/1st0Groom/B2-2/pull/23#pullrequestreview-5529120429) 및 병합 확인
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
- 브랜치: `feature/ysh-collaboration-docs`. A의 시작 커밋은 `bf0304e7c57d12b08f92aedaceaa6c8898421fdd`이며, E의 병합 전 변경과 A 문서 커밋의 merge-base도 같은 해시임을 확인했다. [충돌 2의 실제 커밋 구조와 A 확인](conflict-resolution.md#충돌-2--contributing-작업-시작-절차)을 참조한다.
- 증빙: [수정 후 커밋](https://github.com/1st0Groom/B2-2/commit/393795e3537eb5f6a33a55e2adbcd42d19619654), [담당 Issue #10](https://github.com/1st0Groom/B2-2/issues/10), [충돌 실습 Issue #22](https://github.com/1st0Groom/B2-2/issues/22). 수정 전 커밋은 push하지 않았다.
- 선택 이유: 최근 로컬 커밋의 메시지만 수정하기 위해서.
- 주의점: 커밋 해시가 바뀐다. 이 실습은 push 전에 한다.

## reset --soft — B

- 참여자 / 역할: Kfri (@Kfri-cloud) / B
- 상태: 최초 및 추가 실습과 사후 검증 완료 (2026-10-15). [Issue #30](https://github.com/1st0Groom/B2-2/issues/30), [PR #27](https://github.com/1st0Groom/B2-2/pull/27)에서 기록 제출 및 리뷰 진행
- 브랜치: `feature/kfri-collaboration-docs`
- 상황: push 전 CONTRIBUTING의 PR·리뷰 규칙 변경 커밋을 취소하고 변경은 유지한 뒤 더 구체적인 메시지로 다시 커밋했다.
- 절차: `git reset --soft HEAD~1`, `git status`, `git diff --cached`, 다시 커밋. PowerShell 명령 기록에서 soft reset 및 cached diff 명령을 확인했다. 당시 status와 cached diff의 터미널 출력은 별도 보존되지 않아 재구성하지 않았다.
- 사후 확인 명령: `git log -3 --oneline`, `git reflog -10`
- 실제 reflog 출력 중 해당 실습 구간:

```text
15850c0 HEAD@{0}: commit: docs: define issue-linked PR and substantive review requirements
09b7a4a HEAD@{1}: reset: moving to HEAD~1
c7e787b HEAD@{2}: commit: docs: define PR and review requirements
```

- 취소 전 커밋: `c7e787b docs: define PR and review requirements`
- 다시 만든 커밋: `15850c0 docs: define issue-linked PR and substantive review requirements`
- 내용 검증: `git diff c7e787b 15850c0 --exit-code`는 출력 없이 종료 코드 0으로 끝났다. 취소 전과 다시 만든 커밋의 파일 내용이 동일함을 확인했다.
- 검증 당시 `git status --short --branch` 실제 출력 (이 기록 문서를 수정하기 전):

```text
## feature/kfri-collaboration-docs...origin/main [ahead 1]
```

- 결과: 로컬 커밋 취소 후 동일한 문서 변경으로 새 커밋을 만들었다. 사진에는 커밋 취소 후 변경 파일이 유지된 상태가 남아 있다. staged 상태 자체는 당시 터미널 출력이 없어 별도 증빙하지 못했다.
- 증빙: 로컬 reflog와 스크린샷 `kfri-1_commit.jpg`, `kfri-2_reset.jpg`, `kfri-2_reset2.jpg`, `kfri-3_commit.jpg`. 스크린샷은 앞선 반복 실습 장면이며, 위 해시는 최종 실습 구간 기준이다. 업로드 후 PR과 최종 커밋 링크를 추가한다.
- 선택 이유: 커밋을 취소하면서 변경을 staged 상태로 유지하기 위해서.
- 주의점: 직전 커밋이 존재해야 한다. 공유·push된 커밋에는 이 실습을 하지 않는다.

### B 추가 실습 — staged 변경 출력 확인

첫 재시도에서는 최초 commit이 실패했지만 reset을 실행하여 원격과 로컬 이력이 갈라졌다. 내용이 동일함을 확인한 뒤 `git merge --no-edit origin/feature/kfri-collaboration-docs`로 양쪽 이력을 보존했고, 병합 커밋 `6f1bc7e`를 push했다. 이 시도는 정상적인 soft reset 증빙으로 사용하지 않는다.

이후 실제 문서 변경을 확인하고 새 로컬 커밋으로 다시 실습했다. 아래 명령 사이에는 push하지 않았다.

```sh
git add docs/CONTRIBUTING.md
git commit -m "docs: update review guidance"
git reset --soft HEAD~1
git status
git --no-pager diff --cached
git commit -m "docs: clarify review and re-review requirements"
git --no-pager log -2 --oneline
```

취소 전 실제 commit 출력:

```text
[feature/kfri-collaboration-docs 5e842c5] docs: update review guidance
 1 file changed, 12 insertions(+), 13 deletions(-)
```

reset 후 사용자가 보존한 `git --no-pager diff --cached` 출력에는 다음 staged 변경이 포함되었다 (발췌):

```diff
diff --git a/docs/CONTRIBUTING.md b/docs/CONTRIBUTING.md
index fa06435..8e2bb6e 100644
--- a/docs/CONTRIBUTING.md
+++ b/docs/CONTRIBUTING.md
+- 재리뷰 요청 시 수정 커밋과 재검증 결과를 함께 안내한다.
```

위 diff는 발췌이며 전체 패치가 아니다. cached diff에 문서 변경이 출력되어 staged 상태 유지가 확인됐다. 당시 `git status` 출력은 대화에 제공되지 않아 재구성하지 않았다.

재커밋 실제 출력:

```text
[feature/kfri-collaboration-docs d63e6c6] docs: clarify review and re-review requirements
 1 file changed, 12 insertions(+), 13 deletions(-)
d63e6c6 (HEAD -> feature/kfri-collaboration-docs) docs: clarify review and re-review requirements
6f1bc7e (origin/feature/kfri-collaboration-docs) Merge remote-tracking branch 'origin/feature/kfri-collaboration-docs' into feature/kfri-collaboration-docs
```

사후 검증: `git diff 5e842c5 d63e6c6 --exit-code`가 출력 없이 종료 코드 0으로 끝났다. 취소 전과 재커밋의 파일 내용은 같다. reflog에서도 `5e842c5` 커밋 → `6f1bc7e`로 reset → `d63e6c6` 재커밋 순서를 확인했다.

실습 변경에 A 담당 두 줄의 의도하지 않은 복원이 포함되어, 재커밋 후 별도 수정으로 A의 작업 시작 안내와 브랜치 예시를 복원했다. 기존 공유 커밋을 다시 reset하거나 force push하지 않았다.

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
- 확인 및 공동 기록 작성자: E (`1st0Groom`, PR #25 리뷰에서 확인)
- 상태: 실행 및 E 확인 완료
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
- stash 전과 pop 후 동일하게 확인한 `git diff -- README.md` 출력:

  ```diff
  diff --git a/README.md b/README.md
  index 7a82253..94146d0 100644
  --- a/README.md
  +++ b/README.md
  @@ -14,7 +14,7 @@
   ## 실행 방법
  
  -실행 방법: 추후 작성
  +실행 방법: Python 3.10 이상에서 각 파일을 직접 실행
  ```

- 실행 결과: `main` 전환 후 원래 브랜치로 복귀했으며, `stash pop`으로 README 실행 안내 한 줄이 정상 복원되었다. pop 성공 후 stash 항목은 삭제되었다.
- 결과 / 증빙 링크: [Issue #20](https://github.com/1st0Groom/B2-2/issues/20), [PR #25](https://github.com/1st0Groom/B2-2/pull/25), [E의 stash 확인 리뷰](https://github.com/1st0Groom/B2-2/pull/25#discussion_r4280047517)
- 선택 이유: 미완성 변경을 커밋하지 않고 잠시 보관하기 위해서.
- 주의점: 기본 stash는 새 untracked 파일을 보관하지 않는다. pop 충돌 시 stash가 남을 수 있으므로 상태를 확인한다.
