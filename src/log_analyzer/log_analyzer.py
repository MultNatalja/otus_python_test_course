#!/usr/bin/env python3

import json
import os
import re
from collections import defaultdict, Counter
from pprint import pprint
import argparse


class ParseLogsException(Exception):
    def __init__(self, path: str):
        self.path = path

    def __str__(self):
        return f'ParseLogsException Error: Check the path to log file or directory {self.path} or check your credentials.'


METHOD_PATTERN = re.compile(r'(POST|GET|PUT|DELETE|HEAD|OPTIONS)\b')
REMOTE_HOST_PATTERN = re.compile(r'^(?:\d{1,3}\.){3}\d{1,3}')
DURATION_PATTERN = re.compile(r'\s\d+\n')
DATE_PATTERN = re.compile(r'\[[\w\s/:+-]*\]')
URL_PATTERN = re.compile(r'\"https?://(\S*)\"')


def parse_log_line(line):
    try:
        method = METHOD_PATTERN.search(line).group(0)
        remote_host = REMOTE_HOST_PATTERN.search(line).group(0)
        request_duration = int(DURATION_PATTERN.search(line).group(0).replace('\n', ''))
        date = DATE_PATTERN.search(line).group(0)
        is_url = URL_PATTERN.search(line)
        url = is_url.group(1)[1:-1] if is_url else '-'
    except AttributeError as e:
        print(f"Error parsing line: {line}\nError: {e}")
        return None

    return {
        'method': method,
        'ip': remote_host,
        'duration': request_duration,
        'date': date,
        'url': url,
    }


def generate_report(all_requests):
    requests_number = len(all_requests)
    methods_dict = Counter(request['method'] for request in all_requests)
    dict_ip_requests = defaultdict(lambda: {"requests_number": 0})

    for request_info in all_requests:
        dict_ip_requests[request_info['ip']]["requests_number"] += 1

    top_ips = dict(sorted(dict_ip_requests.items(), key=lambda x: x[1]["requests_number"], reverse=True)[0:3])
    top_durations = sorted(all_requests, key=lambda x: x['duration'], reverse=True)[0:3]

    result = {
        'total_requests': requests_number,
        'total_methods': dict(methods_dict),
        'top_ips': {k: v['requests_number'] for k, v in top_ips.items()},
        'top_longest_requests': top_durations
    }

    return result


def save_to_json(result, output_path):
    with open(output_path, 'w') as json_file:
        json.dump(result, json_file, indent=4)


def print_report(result):
    pprint(result)


def parse_logs(log_file, output_path=None):
    with open(log_file, 'r') as file:
        all_requests = [parse_log_line(line) for line in file if parse_log_line(line)]

    result = generate_report(all_requests)

    if output_path is None:
        output_path = f'{log_file}.json'

    save_to_json(result, output_path)
    print_report(result)


def main():
    parser = argparse.ArgumentParser(description='Parse access logs.')
    parser.add_argument('--log_file', help='Path to log file or log directory.')
    parser.add_argument('--output_path', help='Path to save the JSON report.', default=None)
    args = parser.parse_args()

    if os.path.exists(args.log_file):
        if os.path.isfile(args.log_file):
            parse_logs(args.log_file, args.output_path)
        elif os.path.isdir(args.log_file):
            for file in os.listdir(args.log_file):
                if file.endswith(".log"):
                    path_to_logfile = os.path.join(args.log_file, file)
                    parse_logs(path_to_logfile, args.output_path)
    else:
        raise ParseLogsException(args.log_file)


if __name__ == '__main__':
    main()
