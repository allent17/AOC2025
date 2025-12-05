if __name__ == "__main__":
    pointer = 50
    zeroCounter = 0

    with open("step1.txt", "r") as file:
        for line in file:
            letter = line[0]
            move = int(line[1:])
            count = move
            if letter == "L":
                while count > 0:
                    pointer += 1
                    if pointer == 100:
                        pointer = 0
                        zeroCounter += 1
                    count -= 1
            else:
                while count > 0:
                    pointer += -1
                    if pointer == 0:
                        zeroCounter += 1
                    if pointer == -1:
                        pointer = 99
                    count -= 1
            print(f"{letter} {move} {pointer} {zeroCounter}")

    print(f"{zeroCounter}")








