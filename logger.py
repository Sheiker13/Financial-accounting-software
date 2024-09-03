import datetime

LOG_FILE = "data/logs.txt"

def log_operation(operation_type, username, description):
    with open(LOG_FILE, 'a') as f:
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {operation_type} | {username} | {description}\n")
