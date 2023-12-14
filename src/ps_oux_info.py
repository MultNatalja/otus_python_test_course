#!/usr/bin/env python3

import subprocess
import datetime


def parse_ps_output(output):
    processes = output.splitlines()[1:]
    user_processes = {}
    total_memory = 0.0
    total_cpu = 0.0
    max_memory_process: type[str, float] = ('', 0.0)
    max_cpu_process: type[str, float] = ('', 0.0)

    for process in processes:
        fields = process.split()
        username = fields[0]
        memory = float(fields[3])
        cpu = float(fields[2])

        total_memory += memory
        total_cpu += cpu

        if username in user_processes:
            user_processes[username] += 1
        else:
            user_processes[username] = 1

        if memory > max_memory_process[1]:
            max_memory_process = (fields[10][:20], memory)

        if cpu > max_cpu_process[1]:
            max_cpu_process = (fields[10][:20], cpu)

    return user_processes, total_memory, total_cpu, max_memory_process, max_cpu_process


def generate_report(user_processes, total_memory, total_cpu, max_memory_process, max_cpu_process):
    report = f"Отчёт о состоянии системы ({datetime.datetime.now()}):\n"
    report += f"Пользователи системы: {', '.join(user_processes.keys())}\n"
    report += f"Процессов запущено: {sum(user_processes.values())}\n"
    report += "Пользовательских процессов:\n"
    for user, count in user_processes.items():
        report += f"{user}: {count}\n"
    report += f"Всего памяти используется: {total_memory:.1f} mb\n"
    report += f"Всего CPU используется: {total_cpu:.1f}%\n"
    report += f"Больше всего памяти использует: ({max_memory_process[0]}, {max_memory_process[1]:.1f} MB)\n"
    report += f"Больше всего CPU использует: ({max_cpu_process[0]}, {max_cpu_process[1]:.1f}%)\n"

    return report


def save_report_to_file(report):
    filename = datetime.datetime.now().strftime("%m-%d-%Y-%H:%M-scan.txt")
    with open(filename, 'w') as file:
        file.write(report)


def main():
    try:
        result = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE, text=True, check=True)
        ps_output = result.stdout
        user_processes, total_memory, total_cpu, max_memory_process, max_cpu_process = parse_ps_output(ps_output)
        report = generate_report(user_processes, total_memory, total_cpu, max_memory_process, max_cpu_process)
        print(report)
        save_report_to_file(report)
    except subprocess.CalledProcessError as e:
        print(f"Error executing 'ps aux': {e}")


if __name__ == "__main__":
    main()
