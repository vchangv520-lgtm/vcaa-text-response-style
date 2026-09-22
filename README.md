# VCAA Text Response Style

An installable Codex skill for planning, drafting and revising VCE English and EAL Section A analytical text responses, with dedicated support for Billy Wilder's *Sunset Boulevard*.

The skill follows the decision-making rewarded in strong VCAA responses: exact topic reading, concept-led arguments, familiar and verifiable evidence, selective analysis of construction, and a natural timed-exam voice. It avoids generic AI phrasing without copying student samples or manufacturing mistakes.

## Install

Clone the repository into your Codex skills directory:

```bash
git clone https://github.com/vchangv520-lgtm/vcaa-text-response-style.git ~/.codex/skills/vcaa-text-response-style
```

Open a new Codex task so the installed skill can be discovered.

To update an existing installation:

```bash
git -C ~/.codex/skills/vcaa-text-response-style pull --ff-only
```

## Use

Invoke the skill explicitly with `$vcaa-text-response-style`.

```text
Use $vcaa-text-response-style to plan a VCE EAL response to this topic:
[exact topic]
```

```text
Use $vcaa-text-response-style to revise this paragraph. Preserve my vocabulary
and sentence range, strengthen the analysis, and remove generic AI phrasing:
[draft]
```

```text
Use $vcaa-text-response-style in English mode to draft a complete response.
Use central, widely recognised evidence and keep the voice plausible under
timed Year 12 conditions:
[exact topic]
```

For use outside Codex, complete the bracketed fields in [PROMPT_TEMPLATE.md](PROMPT_TEMPLATE.md).

## Design principles

- Read every concept, modifier and command word in the topic before selecting evidence.
- Organise paragraphs by ideas and their development, not one character per paragraph.
- Prefer central, verifiable scenes to obscure frame-by-frame details.
- Explain how construction creates meaning instead of listing techniques.
- Use English-style conceptual progression with EAL-style sentence clarity.
- Remove generic AI phrasing without imitating errors from student work.

## Repository structure

- `SKILL.md` - core workflow, register choices, evidence principles and final checks.
- `agents/openai.yaml` - Codex display metadata and default invocation prompt.
- `references/vcaa-style-guide.md` - principles distilled from official VCAA assessment reports.
- `references/sunset-boulevard-core-evidence.md` - central scenes, evidence routes and short quotations.
- `PROMPT_TEMPLATE.md` - standalone prompt for other compatible language-model interfaces.
- `EVALUATION.md` - behavioural test cases and a review rubric.
- `scripts/validate_skill.py` - dependency-free structural, language and link validation.

## Validate

Run the repository checks locally:

```bash
python3 scripts/validate_skill.py
```

For behavioural testing, use the cases in [EVALUATION.md](EVALUATION.md) with an independent model or a fresh Codex task.

## Source scope

The guidance was distilled on 22 September 2026 from official VCAA English and EAL external assessment reports for 2023, 2024 and 2025, with the 2026 Northern Hemisphere Timetable EAL report used as a consistency check.

The latest completed Victorian English/EAL report pair available at that date was 2025. This repository does not reproduce examination reports or candidate responses. It derives general writing and assessment principles and links to official material for verification.

- [VCAA English examinations and reports](https://www.vcaa.vic.edu.au/assessment/vce/examination-specifications-past-examinations-and-examination-reports/english)
- [VCAA EAL examinations and reports](https://www.vcaa.vic.edu.au/assessment/vce/examination-specifications-past-examinations-and-examination-reports/english-additional-language-eal)

## Disclaimer

This is an independent educational resource. It is not affiliated with, endorsed by or produced by the Victorian Curriculum and Assessment Authority.

The skill does not guarantee a particular mark and should not replace current VCAA specifications, teacher advice, close study of the set text or the student's own judgement. Verify quotations and scene details against the primary text before submitting assessed work. VCAA requirements and published materials may change after the source date above.
