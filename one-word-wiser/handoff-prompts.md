# Handoff prompts — paste one of these into the agent

All three agents work from the same repository: **github.com/ravebm/rabbi**. Give each one repo access (a clone, a connected GitHub account, or an upload of the folder), then paste the matching prompt. Every prompt starts with "read `AGENTS.md`," which is what keeps them in sync — if you change a skill or a doc in any one of them and it's committed, the others see it on their next pull.

---

## Hermes — operate Substack

> You have access to my repository `ravebm/rabbi` (pull the latest first). Read `AGENTS.md` at the root, then follow `one-word-wiser/operator-brief-substack-setup.md` exactly, start to finish. I am logged into Substack at rabbi.substack.com. Paste every piece of copy verbatim from the brief — do not rewrite anything. Do not publish, email, or change anything the brief does not list. When you finish, reply with the checklist at the end of the brief, and if anything in Substack's interface didn't match the brief, tell me which step rather than improvising. If you had to change anything in the repository (you shouldn't need to), commit it with a one-line message and push.

## Codex — operate Substack *or* write posts

Codex is best at working inside the repository. If your Codex setup can drive a browser, use the operator prompt above word for word (it's agent-agnostic). For writing, use this:

> Open my repository `ravebm/rabbi` and pull the latest. Read `AGENTS.md` at the root, then `skills/one-word-wiser/SKILL.md`, then the two Monday samples in `one-word-wiser/samples/`. Using `one-word-wiser/word-bank.md`, draft the remaining posts for Week 1 — Tuesday through Friday, morning and evening — plus Saturday's Havdalah and Sunday's Week Ahead for Week 2. Follow the skill's output contract exactly: word → meaning → application, morning free and complete with a door at the end, evening 250–350 words with two lines above `[PAYWALL]`. Hebrew Bible only unless the word walks into a Gospel on its own. Save each post as `one-word-wiser/posts/2026-09-DD-morning.md` or `-evening.md`, commit with the message "Week 1 drafts: <words>", and push to a branch named `posts/week-01`. Do not publish anything. Below the drafts, list any citation you are less than certain of.

## Claude — write, edit, or update the system

> Pull `ravebm/rabbi`, read `AGENTS.md`, and [write Tuesday's posts for *shema* / write the week / draft Saturday's recap / update the skill so that … ]. Commit and push whatever you change so Hermes and Codex see it.

---

## When you change something

Make the change in any one agent, and make sure it ends in a commit to the repo. That's it. The other two agents pull before they work, so they inherit it. If an agent ever seems to be working from an old version, tell it: "pull the latest and re-read `AGENTS.md`."

## One-time setup you need to do

1. **Merge the pull request** so these files are on the repository's default branch — agents that clone fresh will otherwise get the old branch. (The repo's default branch is currently `claude/integrate-fal-ai-Oo0sx`; it would be cleaner to rename it `main` in GitHub → Settings → Branches.)
2. Give Hermes and Codex access to the repository.
3. Upload the two logo files to `one-word-wiser/brand/` (any agent can do this if you give it the files) so the operator brief can point to them.
