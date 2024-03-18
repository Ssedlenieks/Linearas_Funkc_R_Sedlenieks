from doctest import testmod
def punkta_parbaude(x, y):
    """
    Parbauda vai koordinata (x, y) atrodas uz linijas y = k * x + b.

    punkta_parbaude (6, 7)
    True
    punkta_parbaude (5, 3)
    False
    punkta_parbaude (0, 0)
    False
    
    """
    if y == k * x + b:
        return True
    else:
        return False
if __name__ == "__main__":
    testmod(verbose=True)

    x = float(input("Ievadi x punkta koordinātas: "))
    y = float(input("Ievadi y punkta koordinātas: "))
    k = 3.5
    b = -14

    if punkta_parbaude(x, y) == True:
        print(f"Punkts ({x}, {y}) atrodas uz linijas.")
    else:
        print(f"Punkts ({x}, {y}) neatrodas uz linijas.")