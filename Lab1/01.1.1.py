start_a = 2
end_a = 5
start_b = 3
end_b = 9

if start_a < start_b:
    start_1 = start_a
    end_1 = end_a
    start_2 =start_b
    if end_1 < start_2:
        print("no crash")
    else:
        print("do crash")
elif start_a == start_b:
    print("crash")
else:
    start_1 = start_b
    end_1 = end_b
    start_2 =start_a
    if end_1 < start_2:
        print("no crash")
    else:
        print("do crash")
