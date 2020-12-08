from dataclasses import dataclass

@dataclass
class Operation:
    op: str
    arg: int

class Console:
    def __init__(self, ops: list[Operation]):
        self.acc = 0
        self.ops = ops

    def run(self):
        pos = 0
        nruns = {i: 0 for i in range(len(self.ops))}
        while pos < len(self.ops):
            op = self.ops[pos]
            nruns[pos] += 1
            if nruns[pos] == 2:
                return False
            if op.op == "acc":
                self.acc += op.arg
            elif op.op == "jmp":
                pos += op.arg
                continue
            pos += 1
        return True

ops = []
with open("day8.in") as f:
    for line in f:
        op, arg = line.split()
        ops.append(Operation(op, int(arg)))

console = Console(ops)
console.run()
print("part 1:", console.acc)

for i in range(len(ops) - 1):
    if ops[i].op == "acc":
        continue
    elif ops[i].op == "jmp":
        new_op = Operation("nop", ops[i].arg)
    elif ops[i].op == "nop":
        new_op = Operation("jmp", ops[i].arg)
    new_ops = ops[:i] + [new_op] + ops[i+1:]
    console = Console(new_ops)
    result = console.run()
    if result:
        print("part 2:", console.acc)

