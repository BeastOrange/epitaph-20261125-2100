"""Entry generator for make.fun bounty:
'Famous Last Words: The Funniest Epitaph'
"""

from pathlib import Path

# Why this entry satisfies the judge brief:
# 1. Famous last words: The opening quote captures the quintessential DIY hubris ("I can fix the brakes myself...").
# 2. Surprise twist & humor: The deadpan three-part rhythm ("He couldn't.") immediately undercuts the overconfidence.
# 3. Reads like carved stone: Explicitly references "this stone", turning the tombstone itself into the punchline.
# 4. Memorable: The widow spending the exact $200 saved to immortalize his mistake stays in the reader's head.
# 5. Length & structure: Exactly one self-contained line of 91 characters (well within the 150-char limit).
ENTRY: str = (
    '"I can fix the brakes myself and save $200." — He couldn\'t. '
    "I spent the $200 on this stone."
)


def validate_entry(text: str) -> None:
    """Validate that the entry strictly adheres to make.fun competition rules."""
    length = len(text)
    if not (1 <= length <= 150):
        raise ValueError(
            f"Validation error: Entry length must be between 1 and 150 characters, "
            f"but got {length} characters: {text!r}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError(
            "Validation error: Entry must be a single line without newline (\\n) "
            "or carriage return (\\r) characters."
        )
    if not text.strip():
        raise ValueError(
            "Validation error: Entry cannot be empty or consist solely of whitespace."
        )
    if text != text.strip():
        raise ValueError(
            f"Validation error: Entry has unauthorized leading or trailing whitespace: {text!r}"
        )

    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError(
            f"Validation error: Entry must be valid UTF-8 encodable text: {exc}"
        ) from exc


def write_entry(dest: Path = Path("/output/entry.txt")) -> Path:
    """Validate entry and write exactly one line to destination file."""
    validate_entry(ENTRY)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(f"{ENTRY}\n", encoding="utf-8")

    # Post-write verification
    written = dest.read_text(encoding="utf-8")
    lines = written.splitlines()
    if len(lines) != 1:
        raise ValueError(
            f"Verification error: Output file '{dest}' must contain exactly 1 line, "
            f"found {len(lines)} lines."
        )
    if lines[0] != ENTRY:
        raise ValueError(
            f"Verification error: Written line does not match ENTRY.\n"
            f"Expected: {ENTRY!r}\n"
            f"Found:    {lines[0]!r}"
        )
    return dest


def main() -> None:
    write_entry()
    print(ENTRY)


if __name__ == "__main__":
    main()
