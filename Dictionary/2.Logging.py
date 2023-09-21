# Question 2: Logging — 3 points

from collections import defaultdict

# Question: Debugging a Complex Dictionary Problem with defaultdict — 15 points

# You are given a code snippet that uses defaultdict but has a bug. Can you identify and debug it?

# Additional Code:
def process_logs(logs):
    user_logs = defaultdict(list)
    
    for log in logs:
        user, action = log.split(':')
        user_logs[user].append(action)
    
    return user_logs

# Given data:
logs = ['user1:login', 'user2:logout', 'user1:logout', 'user2:login', 'user1:login']
