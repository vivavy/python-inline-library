from inline import inline

c: int | float

while True:
    cmd = input("katete-a katete-b/exit> ")
    if cmd == "exit":
        break

    a, b = map(eval, cmd.split(""))

    exec(inline("primer.py"))

    print("gypotinuse:", c)
