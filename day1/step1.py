if __name__ == "__main__":
    pointer = 50
    zeroCounter = 0

    with open("step1.txt", "r") as file:
        for line in file:
            letter = line[0]
            move = int(line[1:])
            if letter == "L":
                pointer = (pointer + move) % 100
            else:
                pointer = (pointer - move)
                if pointer < 0:
                    pointer = abs(0 - (pointer % 100))
            if pointer == 0:
                zeroCounter = zeroCounter + 1
            print(f"{letter} {move} {pointer}")

    print(f"{zeroCounter}")








