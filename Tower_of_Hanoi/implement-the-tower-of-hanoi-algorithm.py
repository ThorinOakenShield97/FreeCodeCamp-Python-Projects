** start of main.py **

def hanoi_solver(n):
    moves = ''
    l1 = []
    l2 = []
    l3 = []
    for i in range(n,0,-1):
        l1.append(i)
    
    moves += f"{l1} {l2} {l3}\n"

    def solver(k,source,aux,target):
        nonlocal moves
        if k > 0:
            solver(k-1,source,target,aux)
            target.append(source.pop())
            moves += f"{l1} {l2} {l3}\n"
            solver(k-1,aux,source,target)

    solver(n,l1,l2,l3)
    return moves[:-1]

print(hanoi_solver(2))   
print(hanoi_solver(3))
print(hanoi_solver(4))
print(hanoi_solver(5))

** end of main.py **

