def sum_the_list(arr):
    if not arr:
        return 0
    head, *tail = arr
    return (head**4 if head <= 0 else 0) + sum_the_list(tail)

def recurse_test_cases(remaining, **results):
    if remaining == 0:
        return list(results.values())
    try:
        x = int(input().strip())
        values = list(map(int, input().split()))
    except (EOFError, ValueError):
        results[str(len(results) + 1)] = -1
        return recurse_test_cases(remaining - 1, **results)

    if len(values) != x:
        results[str(len(results) + 1)] = -1
    else:
        results[str(len(results) + 1)] = sum_the_list(values)
    return recurse_test_cases(remaining - 1, **results)

def print_results(lst):
    if not lst:
        return
    head, *tail = lst
    print(head)
    print_results(tail)

def main():
    try:
        n = int(input().strip())
    except (EOFError, ValueError):
        return
    answers = recurse_test_cases(n)
    print_results(answers)

if __name__ == "__main__":
    main()
