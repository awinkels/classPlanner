
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Class:
    name: str
    code: str
    pre_reqs: Optional[List["Class"]] = None
    co_reqs: Optional[List["Class"]] = None
    availability: List[bool] = field(default_factory=list)

if __name__ == "__main__":
    c = Class(
        name="physics",
        code="PHYS101",
        availability=[True, True]
    )

    c1 = Class(
        name="calculus",
        code="MATH101",
        pre_reqs=[c],
        availability=[True, True]
    )

    #print(c.name)
    for p in c1.pre_reqs:
        print(p.code)
