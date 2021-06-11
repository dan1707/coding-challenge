from typing import Optional


def first_non_repeating_char(word: str) -> Optional[str]:
    repeating_chars = set()
    non_repeating_chars = []

    for c in word:
        if c in repeating_chars:
            continue

        if c in non_repeating_chars:
            repeating_chars.add(c)
            non_repeating_chars.remove(c)
            continue

        non_repeating_chars.append(c)

    if non_repeating_chars:
        return non_repeating_chars[0]
