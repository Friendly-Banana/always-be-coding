import time


def time_it(func, *args, tries=10, name="func", precision=0.8):
    dur = []
    for i in range(tries):
        start = time.process_time()  # perf_counter
        func(*args)
        end = time.process_time()  # process_time
        dur.append(end - start)
        # print(f"{name} took {end - start:{precision}f}")
    print(name)
    print(f"tries: {tries}")
    # print(f"times: {dur}")
    print(f"average: {sum(dur)/tries:{precision}f}")
    print(f"total: {sum(dur):{precision}f}\n")


def compare(*functions: dict):
    for func in functions.keys:
        time_it(func, dict[func])


from LinkedList import LinkedList

l = LinkedList()
for i in range(10):
    time_it(l.append, i, name="append")
    time_it(l.__getitem__, i, name="get")
    time_it(l.__setitem__, i, i, name="set")
    time_it(l.__len__, name="len")
    time_it(l.__delitem__, i, name="del")

# time_it(l.append, 2, name="app")
