# Generate a list of positions to go to scan the map with a range of 10
def generate_positions_to_scan():
    positions = []
    for i in range(5, 40, 5):
        positions.append((i, 5))
        positions.append((i, 25))
    for i in range(5, 30, 5):
        positions.append((5, i))
        positions.append((30, i))
    return positions
