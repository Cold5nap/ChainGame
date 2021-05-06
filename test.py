from logic.logic import Level


def main():

    for row in mtx_cells:
        for cell in row:
            print(cell.__str__())
        print()
    exit(0)


if __name__ == '__main__':
    main()
