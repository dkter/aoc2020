from dataclasses import dataclass
from typing import Union, Optional, List, Tuple, Dict, Set
from itertools import product, count
import re

@dataclass
class CharRuleBody:
    ch: str

    def resolve(self):
        return True

    @property
    def matches(self):
        return {self.ch}

@dataclass
class RefRuleBody:
    # (a, b), (c, d)
    refs: List[List[int]]
    matches: Optional[Set[str]] = None

    def resolve(self):
        # returns done state (is done yet)
        if self.matches is not None:
            return True

        self.matches = []
        for ref in self.refs:
            strings = [""]
            for rule_id in ref:
                rule = rules[rule_id]
                if rule.body.matches is None:
                    self.matches = None
                    return False
                else:
                    strings = product(strings, rule.body.matches)
                    strings = ["".join(string) for string in strings]
            self.matches += strings
        return True

    def resolve_recursive_8(self):
        self.matches = [
            "(" +
            "|".join(rules[42].body.matches) +
            ")+"
        ]

    def resolve_recursive_11(self):
        max_len = len(max(received_messages, key=len))
        self.matches = [
            "(" +
            "|".join(rules[42].body.matches) +
            "){" + str(i) + "}" +
            "(" +
            "|".join(rules[31].body.matches) +
            "){" + str(i) + "}"
            for i in range(1, max_len)
        ]

@dataclass
class Rule:
    id_: int
    body: Union[CharRuleBody, RefRuleBody]

    def matches(self, string):
        for m in self.body.matches:
            # i know there's a flag to only match the entire string but i'm too lazy to look it up
            match = re.match("^" + m + "$", string) 
            if match:
                return True


rules: Dict[int, Rule] = {}
received_messages: List[str] = []
with open("day19.in") as f:
    file_iter = iter(f)
    for line in file_iter:
        if not line.strip():
            # blank line
            break

        id_ = int(line.split(":")[0])
        if "\"" in line:
            rules[id_] = Rule(id_, CharRuleBody(line.split("\"")[1]))
        else:
            rules[id_] = Rule(id_, RefRuleBody(
                [[int(other_id) for other_id in choice.split(" ") if other_id] for choice in line.split(":")[1].split("|")]
            ))
    for line in file_iter:
        received_messages.append(line.strip())

while not all([rule.body.resolve() for rule in rules.values() if rule.id_ not in (0, 8, 11)]):
    pass

rules[8].body.resolve_recursive_8()
rules[11].body.resolve_recursive_11()
rules[0].body.resolve()

count = 0
for message in received_messages:
    if rules[0].matches(message):
        count += 1

print(count)
