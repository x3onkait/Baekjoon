destination      = int(input())
current_position = 1
hop              = 1

while destination > current_position:
    current_position += 6 * hop
    hop              += 1

print(hop)