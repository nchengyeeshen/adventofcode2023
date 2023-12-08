import sys
import math
import functools


def part_one(steps, nodes):
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

    return count


def part_two(steps, nodes):
    counts = []
    starting_nodes = [node for node in nodes.keys() if node.endswith("A")]
    for starting_node in starting_nodes:
        count = 0
        step_i = 0

        stack = [starting_node]
        while len(stack) > 0:
            node = stack.pop()

            if node.endswith("Z"):
                counts.append(count)
                break

            stack.append(nodes[node][0 if steps[step_i] == "L" else 1])

            count += 1
            step_i += 1
            step_i %= len(steps)

        counts.append(count)
    return functools.reduce(math.lcm, counts)


if __name__ == "__main__":
    with open("input.txt" if len(sys.argv) < 2 else sys.argv[1]) as f:
        contents = f.read()

    nodes = {}
    steps, node_map = contents.split("\n\n")
    for entry in node_map.splitlines():
        node_id, edges = entry.split(" = ")
        left, right = edges[1:-1].split(",")
        nodes[node_id] = (left.strip(), right.strip())

    print("Part 1:", part_one(steps, nodes))
    print("Part 2:", part_two(steps, nodes))
