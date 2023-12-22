#!/usr/bin/python3
''' log parsing '''
import sys
import re


def parse_log_line(line, metrics):
    ''' extract file size and status code '''
    # Define a regular expression pattern to match the desired components
    pattern = (
               r'(\d+\.\d+\.\d+\.\d+) - \[('
               r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] '
               r'"GET /projects/260 HTTP/1.1" (\d+) (\d+)'
    )

    # Use re.match to find the components in the input line
    match = re.match(pattern, line)

    if match:
        # Extract matched components
        status_code = int(match.group(3))
        file_size = int(match.group(4))

        metrics['total_file_size'] += file_size
        metrics['status_codes'][status_code] = (
                metrics['status_codes'].get(status_code, 0) + 1
        )

    else:
        print("Failed to parse the input line.")


def print_metrics(metrics):
    ''' print metrcs '''
    print(f"File size: {metrics['total_file_size']}")

    for status_code in sorted(metrics['status_codes']):
        count = metrics['status_codes'][status_code]
        print(f"{status_code}: {count}")


def main():
    ''' read stdin '''
    try:
        metrics = {
                'total_file_size': 0,
                'status_codes': {
                    200: 0,
                    301: 0,
                    400: 0,
                    401: 0,
                    403: 0,
                    404: 0,
                    405: 0,
                    500: 0
                    }
                }
        line_count = 0
        print_interval = 10

        # Read a line from standard input
        for line in sys.stdin:
            parse_log_line(line.strip(), metrics)
            line_count += 1

            if line_count % print_interval == 0:
                print_metrics(metrics)
        print_metrics(metrics)
    except KeyboardInterrupt:
        print_metrics(metrics)


if __name__ == "__main__":
    main()
