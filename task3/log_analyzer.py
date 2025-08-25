from sys import argv, exit
from re import match as regex_match
from collections import Counter

# Parse log line into entities.
# Returns a dictionary of parsed entities or an empty one.
def parse_log_line(line: str) -> dict:
    log_line = {}
    pattern = r'^(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)$'
    match = regex_match(pattern, line)
    if match:
        date_part, time_part, level_part, message_part = match.groups()
        log_line['date'] = date_part
        log_line['time'] = time_part
        log_line['level'] = level_part
        log_line['message'] = message_part
    return log_line

# Read the log file. Returns the list of parsed log dictionaries or an empty list.
def load_logs(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            log_lines = file.readlines()
    except FileNotFoundError:
        print('Error: The file was not found.')
        return []
    except PermissionError:
        print('Error: You do not have permission to read this file.')
        return []
    except IOError as e:
        print(f'An I/O error occurred: {e}')
        return []
    except UnicodeDecodeError:
        print('Error: Could not decode the file content. Check the encoding.')
        return []
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return []
    parsed_logs = []
    for line in log_lines:
        parsed_line = parse_log_line(line)
        if parsed_line:
            parsed_logs.append(parsed_line)
    return parsed_logs

# Get the logs of specified level.
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level.upper()]

# Count logs by level.
def count_logs_by_level(logs: list) -> dict:
    log_levels = [log['level'] for log in logs]
    return Counter(log_levels)

# Output functions:
def display_log_counts(counts: dict):
    print('----------------------------')
    print('Рівень логування | Кількість')
    print('-----------------|----------')
    for name, count in counts.items():
        print(f'{name}' + '\t\t | ' + f'{count}')

def display_details(logs: list):
    print('\n' + f'Деталі логів для рівня "{logs[0]['level'].upper()}":')
    for log in logs:
        print(f'{log['date']} {log['time']} - {log['message']}')

# ============= Main ================
def main():
    if len(argv) == 1:
        print('Usage: python log_analyzer.py <file.log> [ info | debug | error | warning ]')
        exit()
    logs = load_logs(argv[1])
    if not logs:
        print('Nothing to analyze.')
        exit()
    display_log_counts(count_logs_by_level(logs))
    if len(argv) > 2:
        if argv[2].lower() not in ['info','debug','error','warning']:
            print('\nInvalid option. Valid option is one of: info, debug, error, warning')
            exit()
        level = argv[2]
        display_details(filter_logs_by_level(logs, level))

if __name__ == '__main__':
    main()