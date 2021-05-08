class Solution:
    def exclusiveTime(self, n: int, logs):
        stack, res = [], [0] * n
        for log in logs:
            id, func, curr_time = log.split(":")
            id, curr_time = int(id), int(curr_time)
            if func == "start":
                stack.append((id, curr_time))
            elif func == "end" and id == stack[-1][0]:
                pop_id, insert_time = stack.pop()
                time_taken = curr_time - insert_time + 1
                res[pop_id] += time_taken
                if stack:
                    res[stack[-1][
                        0]] -= time_taken
        return res

if __name__ == '__main__':
    #n = 2
    #logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    n = 1
    logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
    ex_t = Solution()
    res = ex_t.exclusiveTime(n,logs)
    for count,time in enumerate(res):
        print('Function {0} has exclusive time of {1}'.format(count,time))
