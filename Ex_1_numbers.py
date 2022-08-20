first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

lines = int(input())

for _ in range(lines):
    command_line = input().split()

    if command_line[0] == 'Add':
        if command_line[1] == 'First':
            first_sequence = first_sequence.union([int(x) for x in command_line[2:]])
        else:
            second_sequence = second_sequence.union([int(x) for x in command_line[2:]])
    elif command_line[0] == 'Remove':
        if command_line[1] == 'First':
            first_sequence = first_sequence.difference([int(x) for x in command_line[2:]])
        else:
            second_sequence = second_sequence.difference([int(x) for x in command_line[2:]])
    elif command_line[0] == 'Check':
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print('True')
        else:
            print('False')
print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')
