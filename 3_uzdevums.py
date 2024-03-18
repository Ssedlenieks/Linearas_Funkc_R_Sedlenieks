def punkta_parbaude(x, y, b):
    """
    Parbauda vai koordinata (x, y) atrodas uz linijas y = k * (x - (-5)) + b.
    punkta_parbaude (5, 8)
    False
    punkta_parbaude (4, 3)
    False
    punkta_parbaude (1, 7)
    False
    punkta_parbaude (2, 4)
    False
    punkta_parbaude (-5, 6)
    True
    punkta_parbaude (10, 9)
    False

    """
    if x == -5:
        return True
    k = (y - b) / (x - (-5))
    if y == k * (x - (-5)) + b:
        return True
    else:
        return False
        
if __name__ == "__main__":
    b = 0

    x = float(input("Ievadi x punkta koordinātas: "))
    y = float(input("Ievadi y punkta koordinātas: "))

    if punkta_parbaude(x, y, b) == True:
        print(f"Punkts ({x}, {y}) atrodas uz linijas")
    else:
        print(f"Punkts ({x}, {y}) neatrodas uz linijas")