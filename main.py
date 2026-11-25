import os

LINE = ("So... do you also pretend to charge just to avoid small talk, "
        "or is my social protocol the only one that's broken?")

def main():
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        pass
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
