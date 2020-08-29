def solution(people, limit):
    answer = 0
    people.sort()
    start = 0
    end = len(people) - 1
    
    while start <= end:
        if start == end:
            start += 1
        elif people[end] + people[start] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        answer += 1
        
    return answer