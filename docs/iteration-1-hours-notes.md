# Week 10 hours provenance

Liam Pheng reported “right now I have 14 hours” on 2026-11-01. The new row is explicitly a RECONSTRUCTED weekly aggregate with blank start/end because no session intervals or activity breakdown were supplied. AI assistance is true for the increment; that flag does not assert that each of the 14 hours was AI-assisted. 15 planned hours is the existing weekly project-capacity assumption, not a fabricated original estimate for this aggregate. Further personal review/demo time must be added when actually worked.

The submission log now has the ten Appendix B columns plus ai_assisted (eleven). docs/hours-log-through-week9-original.csv preserves the exact pre-normalization twelve-column file, including calibration. All original eleven source-column values and hours remain unchanged.

Pre-existing exceptions are not silently repaired: October 19 has overlapping 08:12–10:24 reviewer/developer records; October 25 has an end time 00:00 and zero logged hours; some earlier durations are rounded differently from clock intervals. Week 8's 1.45-hour remainder was already explicitly reconstructed. Personal correction requires Liam Pheng's actual records. The legacy tools/hours_report.py summarizes totals but does not detect these interval patterns, so a clean exit is not a no-pattern-flags claim.
