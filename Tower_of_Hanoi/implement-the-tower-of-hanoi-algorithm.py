** start of main.py **

def hanoi_solver(n: int) -> str:
    """
    Solves the Tower of Hanoi puzzle for 'n' disks and returns a string
    representing the state of the rods at each step.

    Args:
        n (int): The number of disks to move.

    Returns:
        str: A formatted string showing the lists (rods) after every move.
    """
    moves = ''
    
    # Initialize the three rods (l1 is source, l2 is auxiliary, l3 is target)
    l1: list = []
    l2: list = []
    l3: list = []
    
    # Populate the first rod with disks. 
    # The loop goes backwards so the largest disk is at the bottom (index 0).
    for i in range(n, 0, -1):
        l1.append(i)
    
    # Record the initial state of the rods
    moves += f"{l1} {l2} {l3}\n"

    def solver(k: int, source: list, aux: list, target: list) -> None:
        """
        Recursive helper function to move disks between rods following Hanoi rules.
        """
        nonlocal moves
        if k > 0:
            # Step 1: Move k-1 disks from the source rod to the auxiliary rod
            solver(k - 1, source, target, aux)
            
            # Step 2: Move the largest remaining disk from source to target rod
            target.append(source.pop())
            moves += f"{l1} {l2} {l3}\n"
            
            # Step 3: Move the k-1 disks from the auxiliary rod to the target rod
            solver(k - 1, aux, source, target)

    # Start the recursive solving process moving disks from l1 to l3 using l2
    solver(n, l1, l2, l3)
    
    # rstrip() safely removes the trailing newline character for cleaner output
    return moves.rstrip("\n")


# --- Testing block ---
if __name__ == "__main__":
    print("--- 2 Disks ---")
    print(hanoi_solver(2))   
    
    print("\n--- 3 Disks ---")
    print(hanoi_solver(3))
    
    print("\n--- 4 Disks ---")
    print(hanoi_solver(4))
    
    print("\n--- 5 Disks ---")
    print(hanoi_solver(5))

** end of main.py **

