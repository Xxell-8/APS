def solution(record):
    user_info = {}
    log_list = []
    for rec in record:
        if rec.startswith('L'):
            status, user_id = rec.split()
        else:
            status, user_id, username = rec.split()

        if status == 'Enter':
            user_info[user_id] = username
            log = [user_id, '님이 들어왔습니다.']
            log_list.append(log)
        elif status == 'Leave':
            log = [user_id, '님이 나갔습니다.']
            log_list.append(log)
        elif status == 'Change':
            user_info[user_id] = username

    answer = list(map(lambda x: user_info[x[0]] + x[1], log_list))

    return answer