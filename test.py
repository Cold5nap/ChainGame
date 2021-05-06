from logic.logic import Level

def main():
    level = Level(1)
    mtx_cells = level.convert_matrix_word_to_cells(level.read_matrix_words_from_file("matrix_levels/level1.txt"))
    for row in mtx_cells:
        for cell in row:
            print(cell.__str__())
    print()
    exit(0)

if __name__ == '__main__':
    main()
