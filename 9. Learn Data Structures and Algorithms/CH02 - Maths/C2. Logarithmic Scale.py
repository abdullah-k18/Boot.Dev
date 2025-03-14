import math

def log_scale(data, base):
    logs = []
    for i in data:
        nlog = math.log(i, base)
        logs.append(nlog)
    return logs
