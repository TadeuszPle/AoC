import sys
from queue import Queue

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
    print(inv.process_input('i', True))
    print(inv.process_input('b', True))
    print(inv.process_input('i', False))
    print(inv.process_input('i', True))   
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
        highs, lows = 0,0
        for iter in range(rep):
            q: Queue[tuple[bool, str, str]] = Queue()
            for b in button:
                q.put(b)
            cur_highs, cur_lows = 0,len(button)+1
            while not q.empty():
                signal, prev, cur = q.get(block=False)
                if cur in switches:
                    # this is just exclusive or 
                    if signal:
                        continue
                    outs = switches[cur][1]
                    switches[cur] = (not switches[cur][0], outs)
                    for out in outs:
                        q.put((switches[cur][0],cur, out)) 
                    if switches[cur][0]:
                        cur_highs += len(outs)
                    else:
                        cur_lows += len(outs)
                elif cur in cs:
                    new_signal = cs[cur].process_input(prev, signal)
                    for out in cs[cur].outputs:
                        q.put((new_signal,cur, out))
                    if new_signal:
                        cur_highs += len(cs[cur].outputs)
                    else:
                        cur_lows += len(cs[cur].outputs)
                else:
                    rx = signal
                q.task_done()
            highs += cur_highs
            lows += cur_lows
            if not rx:
                print(iter)
        return highs, lows
    highs, lows = part1(repeats)
    output = lows*highs
    print(f"highs: {highs}, lows: {lows}, mult: {output}")