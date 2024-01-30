if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    tot=0
    for score in student_marks[query_name]:
        tot += score
    tot="%.2f" % (tot/3)
    print(tot)
