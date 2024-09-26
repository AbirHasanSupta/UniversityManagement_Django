import random



password_set = [
    [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ],
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
]

def random_password_generator():
    password = ""
    for i in range(10):
        x = random.randint(0, len(password_set) - 1)
        y = random.randint(0, len(password_set[x]) - 1)
        password += str(password_set[x][y])
    return password
