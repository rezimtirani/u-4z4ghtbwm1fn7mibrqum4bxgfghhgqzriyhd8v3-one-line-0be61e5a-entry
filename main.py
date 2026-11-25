"""One Line, One Laugh.

Writes one funny line to $MAKEFUN_OUTPUT_DIR/entry.txt: the joke
about an AI that took "act more human" a little too literally.
Standard library only.
"""

import os

JOKE = "I asked my AI to act more human. Now it ignores my texts and blames the Wi-Fi."


def check_joke(text):
    """Check the joke against the competition gate before writing it.

    The gate needs UTF-8 text of 1 to 140 characters, not only white
    space, in a single line: one funny line, short enough to read in
    a breath and whole enough to land on its own. Returns the cleaned
    text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("joke must not be only whitespace")
    if len(cleaned) > 140:
        raise ValueError(
            "joke is %d characters, over the 140 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("joke must be exactly one line")
    return cleaned


def joke_shape(text):
    """Small shape check on the joke, for a last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A one-liner that is too short to carry a joke
    is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_joke(JOKE)
    shape = joke_shape(text)
    if shape["words"] < 5:
        raise ValueError("joke is too short to carry a punchline")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
