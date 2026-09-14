# Substack consistency audit — September 14, 2026

Evan asked to rethink One Word Wiser, retire melodramatic/“secret” framing, explore a simple study offer, and fix the inconsistencies on rabbi.substack.com. This task pulled `main`, read the root rules, and explained the conflict with older required wording before making corrections.

## Saved changes

| Surface | Correction |
|---|---|
| About page | Replaced outdated cadence and “secret” promises with one morning email, complete free teaching, and full weekday reflections. Exact copy: `samples/about-page.md` |
| Free benefit | “One Hebrew word and its meaning in Scripture, every morning. Free, always.” |
| Paid benefit | “The full weekday reflections on Hebrew, Jewish wisdom, and everyday life.” |
| Free welcome | Subject Welcome. Updated cadence, weekend description, current paid explanation, and dated free launch period. No unpublished book promise |
| Paid welcome | Subject Welcome. Removed two-a-day/evening/book promises, thanked supporters, described the current paid benefit, retained an account-management link |
| Imported welcome | Subject Welcome. Uses the free/general welcome; no assumption that an imported reader has paid |
| Founding welcome | Inspected; inherits the corrected paid welcome without a separate edit |
| Introduction | Replaced old A Rabbi for the World / Rabbi Sacks publication description with One Word Wiser’s Hebrew/Bible focus |
| Navigation | Hid Morning and Evening links; preserved the sections and existing post assignments |
| Subscription expiration email | Clarified that free teaching and free archives remain accessible; preserved the dynamic subscribe button |
| Automated upsell | Benefit now reflects the current paid wording. Changed “benefits you unlock” to “Paid subscribers receive.” Preserved its actual discount and checkout link |
| You Can Still Come Home | Changed only the web heading “Let It Change Your Life” to “Learning to Return.” Preserved Evan’s later title, subtitle, body, and assets |
| Happy New Year | Changed subtitle to “One Hebrew word, every morning.” Corrected the same cadence in the body and described Jewish interpretation without the old mystical-product promise |
| Two obsolete launch drafts | Labeled “Retired draft: Shanah evening letter” and “Retired draft: Earlier One Word Wiser introduction,” with subtitles explaining that they are superseded and should not be published |

## Verification and boundaries

Saved templates were reopened; the free welcome’s final paragraph remains italic. The paid welcome was also verified through the inherited founding message. The corrected About page was checked at a 390-pixel phone width, including its ending, and the temporary viewport override was reset. The one-page study PDF was rendered and visually inspected; Hebrew vowel marks, one-page length, text extraction, and all three source links were checked.

The dashboard showed 154 published posts, 22 drafts, and **no scheduled posts** at this audit. This is a snapshot, not a future monitoring promise. The upcoming September 15–20 source files remain in git; their rejected headings were corrected locally. They were not uploaded or scheduled.

The current public entry pages and relaunch copy were audited. Historical articles and the old Everyone Needs a Rabbi podcast were preserved. A historical draft’s retained body is a record of an earlier plan, not an active subscriber promise. Email headers/footers, the opt-out page, renewal email, and referral gift invitation had no conflicting product/cadence wording requiring changes.

No new post, list email, test email, price change, new discount, billing change, section deletion, or recurring automation was performed. The two existing published posts were updated on the web, not resent. Existing subscriptions and historical content remain in place.

## What remains a decision

- Whether to adopt **The Rabbi’s Notes**, one weekly reading companion, and how it relates to the existing paid reflections. It is currently only a local prototype.
- Whether the existing September 28 paid-gate plan remains right after this rethink. The current public launch wording still says letters are free through September 27.
- When to prepare and schedule the next letter. None is scheduled as of this audit.

The book is not live. Its future publication, study-companion pilot, paid-offer changes, ads, and live sessions need their own current tasks. The repository’s former revenue forecasts and automatic-looking growth schedules were replaced with clearly labeled experiments and verification requirements.
