from dataclasses import dataclass
from typing import Union, Optional, List, Tuple, Dict, Set
from itertools import product

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

@dataclass
class Rule:
    id_: int
    body: Union[CharRuleBody, RefRuleBody]

    def matches(self, string):
        return string in self.body.matches
        # if isinstance(self.body, CharRuleBody):
        #     return (string[0] == self.body.ch)
        # else:
        #     for ref in self.body.refs:
        #         for rule, idx in zip(ref, range(len(string))):
        #             if not rules[rule].matches(string[idx:]):
        #                 print(rule, string[idx:])
        #                 break
        #         else:
        #             return True
        #     else:
        #         return False


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

while not all([rule.body.resolve() for rule in rules.values()]):
    pass

count = 0
for message in received_messages:
    if rules[0].matches(message):
        count += 1

print(count)
