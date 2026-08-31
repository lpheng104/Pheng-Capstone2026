# AI Usage Log — Acountabilibuddy

**Owner:** Liam Pheng · **Policy set:** <2026-08-30> · **Last entry:** <2006-08-30>

## Policy

**Spine rule.** The human stays in the loop where the judgment lives. AI accelerates;
I decide, I verify, and I am accountable for everything in this repository.

**The line I do not cross.** I will not delegate a judgment I cannot defend. If I
cannot explain a decision in this repository in my own words, under questions,
without the tool in front of me, it does not go in.

### Tools I have decided to use

| Tool / product | Model or version, as best I can name it | What I will use it for | What I will never use it for |
|---|---|---|---|
| ChatGPT | 5.6-Luna | Debugging Code and Proofreading documentation | Writing my code or writing my documentation |
| GitHub CoPilot | 1.388.x Visual Studio Extension | Assist in Code generation | Completely write my code or documentation |

### Zones

| Zone | Covers | What I owe |
|---|---|---|
| Green (assistive) | error-message explanation, reformatting, grammar, boilerplate I fully understand, rubber-ducking a design I already drafted | nothing; work normally |
| Amber (generative) | drafted requirements, scaffolded code I keep, generated tests, proposed architecture, documentation prose | one row in the table below, the day it happens |
| Red (prohibited) | generated decision records, memos, or reflections submitted as mine; a choice I cannot defend; another person's private data or a classmate's unsubmitted work; code I cannot explain line by line | do not |

### Disclosure

Every Amber-zone use appears below. Generated code that survives into `src/` carries a
comment naming the date of the log entry that covers it. Nothing in `docs/adr/`, the
memos, or the reflections is generated text.

## Entries

| Date | Tool / model | What I asked | What I kept | What I changed | How I verified |
|---|---|---|---|---|---|
| 08-31-2026 | ChatGPT 5.6-Luna | "Can you check my spelling and punctuation to ensure grammatical correctness. Do not change my original wording and only fix punctuation and grammar" + Copied and Pasted first candidate idea into ChatGPT (it gave me a proofread version of what I wrote, but it changed my wording and completely rewrote some of my sentences) I then resubmitted my original text and said "Only proofread punctuation issues"  (it gave me a proofread version of my original text) | I kept the version of my original text only proofread with corrected punctuation and grammar | I replaced my unproofread candidate idea with the proofread one| Compared side by side the proofread version and the originally written version to ensure my wording is the same and ChatGPT only changed the puncutation |

<!--
  A BAD entry (do not imitate):
    | Week 3 | ChatGPT | requirements | most of it | some | looked fine |

  A GOOD entry:
    | 2026-09-22 | <assistant + the model version you actually used>
    | "Interview me about a household food-tracking app and list functional requirements."
    | 6 of 19 proposed requirements, as raw material only.
    | Rewrote all 6 into FR form with actor + condition; deleted 13 as out of scope
      (it invented multi-household sharing and a mobile app I never mentioned).
    | Checked each against my Week-2 scoping decision; confirmed FR-004's "3 days"
      threshold with my actual user instead of accepting the model's default.

  The good entry takes ninety seconds and is evidence of judgment.
  The bad one is evidence of nothing.
-->
