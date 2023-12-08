import sys

if __name__ == "__main__":
    with open("input.txt" if len(sys.argv) < 2 else sys.argv[1]) as f:
        contents = f.read()

    nodes = {}
    steps, node_map = contents.split("\n\n")
    for entry in node_map.splitlines():
        node_id, edges = entry.split(" = ")
        left, right = edges[1:-1].split(",")
        nodes[node_id] = (left.strip(), right.strip())

    count = 0
    step_i = 0
    stack = ["AAA"]
    while len(stack) > 0:
        node = stack.pop()

        if node == "ZZZ":
            break

        stack.append(nodes[node][0 if steps[step_i] == "L" else 1])

        count += 1
        step_i += 1
        step_i %= len(steps)

    print("Steps:", count)
