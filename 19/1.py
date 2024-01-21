from typing import List, Tuple, Dict
import sys
class Part:
    def __init__(self, x:int, m: int, a: int, s:int) -> None:
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def sum(self) -> int:
        return self.x + self.m + self.a + self.s

class Section:
    def __init__(self, cur_workflow, x, m ,a, s) -> None:
        self.cur_workflow = cur_workflow
        self.x = x
        self.m = m
        self.a = a
        self.s = s

class Rule:
    def __init__(self, attr: str, sign: str, val: int, dest: str) -> None:
        self.attr = attr
        self.greater = sign == '>'
        self.val = val
        self.dest = dest

    def compare(self, part: Part):
        part_val = getattr(part, self.attr)
        if self.greater and part_val > self.val:
            return self.dest
        elif not self.greater and part_val < self.val:
            return self.dest
        return None
        
def get_input_data(f_path: str):
    ws, ps = open(f_path).read().strip().split('\n\n')
    workflows: Dict[str, Tuple[List[Rule], str]] = {}
    # parts = [list(map(int,n[2:])) for p in ps.split() for n in p[1:-1].split(',') ]
    parts = [map(int,[n.split('=')[1] for n in p[1:-1].split(',')]) for p in ps.split()]
    parts = [Part(*part) for part in parts]
    for w in ws.split():
        workflow = []
        name, rs = w.strip().split('{')
        rs, last_dest = rs[:-1].split(',')[:-1], rs[:-1].split(',')[-1]
        for r in rs:
            a, dest = r.split(':')
            workflow.append(Rule(a[0], a[1], int(a[2:]), dest))
        workflows[name] = (workflow, last_dest)
    return parts, workflows

def part1(f_name: str):
    parts, workflows = get_input_data(f_name)
    output = 0
    for part in parts:
        cur_workflow = 'in'
        while cur_workflow != 'A' and cur_workflow != 'R':
            ws, last_dest = workflows[cur_workflow]
            for w in ws:
                cur_workflow = w.compare(part)
                if cur_workflow:
                    break
            if not cur_workflow:
                cur_workflow = last_dest
        if cur_workflow == 'A':
            output += part.sum()
    return output

def part2(f_name: str):
    _, workflows = get_input_data(f_name)
    cur_workflow = 'in'
    start_botd = [(-float('inf'), float('inf'))]*4
    cur_sect = Section(cur_workflow, *start_botd)


if __name__ == "__main__":
    f_name = sys.argv[1]
    print(part1(f_name))
    