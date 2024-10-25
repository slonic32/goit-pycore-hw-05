import sys
import re


def parse_log_line(line: str) -> dict:
    """parse line from log"""
    pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)"
    match = re.match(pattern, line)
    if match:
        return {
            "date": match.group(1),
            "time": match.group(2),
            "level": match.group(3),
            "message": match.group(4),
        }
    return None


def load_logs(file_path: str) -> list:
    """function to read log file"""
    logs = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                log_entry = parse_log_line(line.strip())
                if log_entry:
                    logs.append(log_entry)
    except:
        print(f"Файл {file_path} не знайдено.")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """filter logs"""
    return [log for log in logs if log["level"].upper() == level.upper()]


def count_logs_by_level(logs: list) -> dict:
    """count logs by level"""
    counts = dict()
    for log in logs:
        if log["level"] in counts.keys():
            counts[log["level"]] += 1
        else:
            counts[log["level"]] = 1
    return counts


def display_log_counts(counts: dict):
    """print stats"""
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def main():
    """main function"""
    # parse command line arguments
    if len(sys.argv) < 2:
        print("Вкажіть шлях до файлу логів як аргумент командного рядка.")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if len(sys.argv) == 3:
        # filtered
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)


if __name__ == "__main__":
    main()
