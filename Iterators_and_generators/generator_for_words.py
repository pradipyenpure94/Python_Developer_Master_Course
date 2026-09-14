"""Generator for Words Longer Than N Characters."""

from collections.abc import Generator


def generator_for_longer_words(words: list[str], minimum_length: int = 5) -> Generator[str]:
    """Generate the longer words."""

    for word in words:
        if len(word) > minimum_length:
            yield word


if __name__ == "__main__":
    words = ["Python", "Java", "Programming", "AI", "Developer"]
    longer_words = generator_for_longer_words(words=words)
    print(next(longer_words))
    print(next(longer_words))
    for word in longer_words:
        print(word)
