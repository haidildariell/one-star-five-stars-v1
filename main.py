"""One Star, Five Stars for the Food.

Writes a single-sentence alien tourist review of Earth to
/output/entry.txt: a one-star complaint about the locals' mornings
that still compliments the food (satay) enough to want a second visit.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

SENTENCE = (
    "One star: the locals drink bitter bean water just to endure "
    "their own mornings, yet one skewer of satay had me filing "
    "for a second invasion."
)


def sentence_bytes():
    """Return the review sentence encoded as UTF-8 bytes."""
    return SENTENCE.encode("utf-8")


def verify_entry(path=OUTPUT_PATH):
    """Read the written file back and confirm it matches the sentence."""
    with open(path, "rb") as handle:
        return handle.read() == sentence_bytes()


def write_entry(path=OUTPUT_PATH):
    """Write the sentence bytes to path, creating its directory first."""
    data = sentence_bytes()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(data)
    if not verify_entry(path):
        raise RuntimeError("written entry does not match the sentence")
    return len(data)


def main():
    written = write_entry()
    return 0 if written == len(sentence_bytes()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
