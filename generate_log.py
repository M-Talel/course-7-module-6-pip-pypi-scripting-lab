from lib.generate_log import build_log_entries, generate_log

if __name__ == "__main__":
    entries = build_log_entries()
    generate_log(entries)
