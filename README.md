# JLPT N3 Daily Challenge – GitHub Pages

## Setup (no terminal required)
1. Extract the ZIP, then upload its **contents** to the root of `nguyenbaodieulien-lab/jlpt-n3-daily-challenge`. Include the hidden `.github` directory and the `scripts` and `data` directories. Use GitHub's Add file > Upload files. If the hidden folder cannot be uploaded, create `.github/workflows/daily-publish.yml` using Add file > Create new file, and paste the file contents.
2. Check Settings > Pages: Deploy from a branch, `main`, `/(root)`.
3. Open the game URL and check the header shows `Chương 1 · Bài 1` and the published date.
4. In Actions, open `Publish JLPT N3 Daily Lesson`, select Run workflow, enter `2026-11-04` to test the initial reviewed bank, and run it. This commits `data/daily.json` if it changes.
5. In Settings > Actions > General > Workflow permissions, grant **Read and write permissions** if the workflow fails on `git push` with HTTP 403 (subject to your account/organization policy).

## Daily operation
The GitHub Actions cron `0 23 * * *` runs at **08:00 Japan time the next calendar day** (UTC 23:00 previous day). GitHub scheduled workflows can be delayed; this is not a guaranteed exact 08:00 execution. Every 6-day cycle: 5 lessons and 1 review. On a day with no reviewed bank, the workflow **fails safely and does not replace the previous published lesson**. You must add and review the next bank before that date. The game displays the publication date so learners can spot stale content.

Bank naming: `data/banks/chapter-01-lesson-02.json` through lesson 05, then `data/banks/chapter-01-review.json`; repeat through chapter 12. Copy the structure of `chapter-01-lesson-01.json`, set `chapter`, `lesson`, `title`, `reviewed` (only after checking readings/answers), and provide at least 10 original reviewed vocabulary records. For review banks use `"lesson":"review"`. `reviewed: true` is a manual editorial assertion, **not** automated fact checking.

## Limitations and safety
- The initial included bank contains 20 previously authored example terms for Chapter 1 Lesson 1. No claim is made that later JTest lessons have been collected. This package does **not** scrape JTest, automatically generate new JLPT questions, or copy protected exercises. Use the site as a reference subject to its terms; author and check your own questions.
- The game still uses local browser storage and share/import codes; Firebase real-time leaderboard **is not implemented**.
- This repository is public: **never commit email addresses, passwords, Firebase service credentials, Outlook tokens, or secrets**.
- No email is sent by this workflow. Outlook invitations remain manual and should only be sent after verifying the public game link.
- The existing game has a fixed 10-question round and vocabulary-based contexts. Some vocabulary entries may need expert review; synthesized pronunciation still depends on installed Japanese voices.
