def read_and_preview_file(file_path, preview_chars=99, verbose=True):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    if verbose:
        print(f"file name: {file_path}")
        print(f"total number of characters: {len(text)}")
        print(text[:preview_chars])
        print("-" * 60)

    return text


def main():
    # Book 1
    book1_text = read_and_preview_file("text_files/aa-a-man-thinketh.txt", 99, False)

    # Book 2
    verdict_text = read_and_preview_file("text_files/the-verdict.txt")

    # Book 3
    school_of_life_text = read_and_preview_file(
        "text_files/the-school-of-life-an-emotional-education.txt"
    )


if __name__ == "__main__":
    main()
