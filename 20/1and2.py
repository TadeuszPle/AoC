import sys
import math
# part 2 inspired thanks to HyperNeutrino 
# https://www.youtube.com/watch?v=lxm6i21O83k
def process_file_data(data: list[str]):
    flip_flops: dict[str, tuple[bool, list[str]]] = {}
    conjunctions: dict[str,Conjunction] = {}
    for line in data:
        name, destinations = line.split('->')
        destinations = list(map(lambda x: x.strip(), destinations.strip().split(',')))
        clean_name = name[1:].strip()  
        if name[0] == '%':
            flip_flops[clean_name] = (False, destinations)
        elif name[0] == '&':
            conjunctions[clean_name] = Conjunction(clean_name, destinations)
        else:
            init_d = [(False,clean_name, d) for d in destinations]
    all_outputs =  [(label_name, outputs) for label_name, (_, outputs) in flip_flops.items()] + [(name, c.outputs) for name, c in conjunctions.items()]
    for label_name, outputs in all_outputs:
        for out in outputs:
            if out in conjunctions:
                conjunctions[out].add(label_name)
            
    return init_d, flip_flops, conjunctions

class Conjunction:
    def __init__(self, name:str, outputs: list[str],):
        self.name = name
        self.outputs = outputs
        self.inputs = []
        self.toggles = []

    def output(self):
        return not all(self.toggles)

    def process_input(self, input:str, signal:bool):
        # update internal state
        indx = self.inputs.index(input)
        self.toggles[indx] = signal
        return self.output()
    
    def add(self, input_label:str):
        self.inputs.append(input_label)
        self.toggles.append(False)
    
    def __bool__(self, ):
        return self.output()
    
def test1():
    inv = Conjunction('a', ['b'])
    inv.add('i')
    inv.add('b')
# probably could speed up entire rocess if 
# i could jsut rememmber what state i am after a step 
# and if happen to go to a step that i know then just
#  add those output numbers and adjust to the last known state

if __name__ == "__main__":
    fname = sys.argv[1]
    repeats = int(sys.argv[2])
    _data = open(fname).read().strip().split('\n')
    button, switches, cs = process_file_data(_data)
    # print(button, switches, cs)
    def part1(rep: int):
        highs, lows = 0,rep
        for _ in range(rep):
            q: list[tuple[bool, str, str]] = [b for b in button]
            while q:
                signal, prev, cur = q.pop(0)
                if signal:
                    highs += 1
                else:
                    lows += 1
                
        return highs, lows
    def part2():
        # assert only one rx output
        (last_c, )=[name for name, c in cs.items() if 'rx' in c.outputs]
        
        cycles = {name: None for name, c in cs.items() if last_c in c.outputs}
        presses = 0
        while True:
            presses += 1
            q: list[tuple[bool, str, str]] = [b for b in button]
            while q:
                signal, prev, cur = q.pop(0)
                if cur == last_c and signal:
                    if not cycles[prev]:
                        cycles[prev] = presses
                    else:
                        assert not presses // cycles
                if cur in switches:
                # this is just nand
                    if signal:
                        continue
                    outs = switches[cur][1]
                    switches[cur] = (not switches[cur][0], outs)
                    for out in outs:
                        q.append((switches[cur][0],cur, out)) 
                elif cur in cs:
                    new_signal = cs[cur].process_input(prev, signal)
                    for out in cs[cur].outputs:
                        q.append((new_signal,cur, out))
                if all(cycles.values()):
                    out = 1
                    for val in cycles.values():
                        out = math.lcm(val, out)
                    return out

    #highs, lows = part1(repeats)
    
    output = part2()
    print(output)
    #print(f"highs: {highs}, lows: {lows}, mult: {output}")
