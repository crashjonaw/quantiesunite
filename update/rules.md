# Feedback Fix Rules

Rules to follow when addressing feedback from `feedback.csv`:

1. **Do not ever spawn Python scripts to address any fixes.** Instead, spawn agents to use LLM Opus to resolve the issues.
2. **Determine if it's a systematic issue.** If it is, deploy the fix across all modules/topics — not just the one reported. Examples: alignment issues, graphs, shapes that are out of the box, LaTeX display issues.
3. **Only automatically fix feedback submitted by the admin.** For feedback submitted by non-admin users, do not attempt to fix them.
4. **Once a fix has been resolved, terminate the current server session and redeploy the website via `./run.sh`.**
5. **Never attempt to read, write, or access files outside of the `quantiesunite` parent folder.**
6. **Update the CSV after fixing.** Mark `fixed?` as `yes`, fill in `fix_summary`, `fixed_at`, and `fixed_by` columns so there is an audit trail and the same feedback is not re-processed.
7. **Don't fix multiple feedbacks in one pass.** Resolve one at a time, redeploy, then pick up the next. This avoids compounding breakages.
8. **Never modify `feedback.csv` rows submitted by users beyond the fix columns.** Do not alter the original description, user, or page_link fields.
9. **If a fix cannot be determined confidently, skip it.** Mark it with a note in `fix_summary` (e.g., "needs manual review") rather than attempting a risky change. Send a Telegram notification via `from telegram.notify import send_manual_review`.
10. **Send Telegram notifications for key events.** Use `send_manual_review()` for items that need human attention, `send_fix_deployed()` after a successful fix, and `send_skipped()` when feedback is skipped for any reason.
11. **After each fix, send a Telegram notification with the page link** so the admin can verify the fix immediately on mobile. Use the public URL format: `https://quantiesunite.sg{page_link}` (e.g., `https://quantiesunite.sg/topic/k_counting/learn/01_what_is_counting`). Call via: `python3 -c "from telegram.notify import send_fix_deployed; send_fix_deployed(ID, 'summary', 'https://quantiesunite.sg/path')"`
12. **For systematic issues, append an entry to `update/notes.md`** documenting the problem, scope, fix applied, and date. This prevents duplicate work across future loop passes.
