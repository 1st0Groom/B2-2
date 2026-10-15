# 제출 인덱스

- 팀명: TODO
- 저장소 URL: https://github.com/1st0Groom/B2-2
- 상태: 준비 초안 — 실제 협업 후 링크와 완료 여부를 작성

## 팀원별 기여

| 실명 | 만든 Issue 2개 | 병합된 PR 2개 | 다른 사람 PR 리뷰 2개 | 본인 PR 리뷰 반영 | 결과물 기여 커밋 | 트러블슈팅 참여 기록 |
|---|---|---|---|---|---|---|
| A | TODO | TODO | TODO | TODO | TODO | TODO |
| B — Kfri (@Kfri-cloud, 실명 별도 확인) | [#16 함수](https://github.com/1st0Groom/B2-2/issues/16), [#30 문서](https://github.com/1st0Groom/B2-2/issues/30) | [#17 함수](https://github.com/1st0Groom/B2-2/pull/17), [#27 문서](https://github.com/1st0Groom/B2-2/pull/27) | [#13 입력 검증 제안](https://github.com/1st0Groom/B2-2/pull/13#pullrequestreview-5528799146), [#18 반영 확인](https://github.com/1st0Groom/B2-2/pull/18#pullrequestreview-5528919992), [#23 문서 확인](https://github.com/1st0Groom/B2-2/pull/23#pullrequestreview-5529120429) | [#17 타입 검사 반영](https://github.com/1st0Groom/B2-2/commit/455403a), [#27 중복 문장 정리](https://github.com/1st0Groom/B2-2/commit/576fccc) | [함수·예시 추가](https://github.com/1st0Groom/B2-2/commit/e684343), [PR·리뷰 규칙](https://github.com/1st0Groom/B2-2/commit/4f9fd15) | [soft reset 기록](docs/troubleshooting-log.md#reset---soft--b) |
| C | TODO | TODO | TODO | TODO | TODO | TODO |
| D | TODO | TODO | TODO | TODO | TODO | TODO |
| E | TODO | TODO | TODO | TODO | TODO | TODO |

## 문서와 증빙

### B 평가 항목별 증빙

- PR #17은 Issue #16, PR #27은 Issue #30을 `Closes`로 연결했으며 두 PR 모두 병합되었다.
- 본인 PR 리뷰 반영: #17에서 Opdata의 입력 타입 검사 제안을 `455403a`에 반영했고, #27에서 중복 문장 삭제 제안을 `576fccc`에 반영했다. 각 PR의 Opdata 승인 기록에서 재확인을 확인할 수 있다.
- 타인 PR 리뷰: 위 표의 #13, #18, #23은 실제 GitHub 리뷰 링크다. #13의 개선 제안은 후속 PR #18에 반영되었다.
- 복구 실습: `5e842c5` → soft reset → `d63e6c6`. 실제 cached diff와 전후 내용 비교 결과, 실패한 중간 시도 및 보존하지 못한 출력의 범위를 로그에 구분했다.
- [Codex 활용 범위 및 결과물 링크](docs/conflict-resolution.md#codex-활용-기록--b--kfri)는 보조 증빙이다. Git 협업 수행 증빙은 위 Issue·PR·리뷰·커밋·실습 기록을 기준으로 확인한다.
- B의 실명, 팀 전체 완료 여부, main 보호 설정 및 최종 히스토리는 별도 확인이 필요하다. 이 변경으로 팀 전체 체크박스를 완료 처리하지 않는다.

- [협업 규칙](docs/CONTRIBUTING.md)
- [충돌 기록 2회](docs/conflict-resolution.md)
- [트러블슈팅 4종](docs/troubleshooting-log.md)
- Git 히스토리: docs/git-history.txt (최종 병합 후 생성)
- main 보호 설정 증빙: TODO (스크린샷 링크 권장)

## 최종 체크

- [ ] main 직접 push 금지, PR 필수, 다른 사람 1명 승인 설정
- [ ] 전원 Issue 2개와 병합된 PR 2개 이상
- [ ] 각 PR에 Closes #번호, What / Why / How 포함
- [ ] 전원 다른 사람 PR 리뷰 2개 이상
- [ ] 모든 PR에 실질 리뷰 코멘트와 작성자 응답 또는 수정 기록
- [ ] 전원 본인 PR 리뷰 반영 1회 이상
- [ ] 전원 함수 1개 이상, 사용 예시, 기여 커밋
- [ ] 충돌 해결 2회 기록, 최소 1회 같은 hunk의 비자명 충돌
- [ ] amend / soft reset / revert / stash·pop 기록
- [ ] 전원 트러블슈팅 기록 작성 참여
- [ ] 협업 문서 3종 및 히스토리 증빙
- [ ] TODO와 미실습 표시를 실제 결과로 교체
