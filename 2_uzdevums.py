from doctest import testmod
def punkta_parbaude(x, y):
    """
    Parbauda vai koordinata (x, y) atrodas uz linijas y = k * x + b.
    punkta_parbaude (1, 9)
    True
    punkta_parbaude (2, 9)
    True
    punkta_parbaude (3, 9)
    True
    punkta_parbaude (4, 9)
    True
    punkta_parbaude (0, 9)
    True
    punkta_parbaude (10, 9)
    True
    
    """
    if y == k * x + b:
        return True
    else:
        return False

if __name__ == "__main__":
    testmod(verbose=True)

    k = 9
    b = 0

    x = float(input("Ievadi x punkta koordinātas: "))
    y = float(input("Ievadi y punkta koordinātas: "))

    if punkta_parbaude(x, y) == True:
        print(f"Punkts ({x}, {y}) atrodas uz linijas.")
    else:
        print(f"Punkts ({x}, {y}) neatrodas uz linijas.")