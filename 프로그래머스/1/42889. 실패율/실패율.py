def solution(N, stages):
    answer = []
    total_users = len(stages)

    for i in range(1, N + 1):
        if total_users == 0:
            answer.append((i, 0))
        else:
            stage_users = stages.count(i)
            failure_rate = stage_users / total_users
            answer.append((i, failure_rate))
            total_users -= stage_users

    answer.sort(key=lambda x: (-x[1], x[0]))
    return [stage for stage, _ in answer]