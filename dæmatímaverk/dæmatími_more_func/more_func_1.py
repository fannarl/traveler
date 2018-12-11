#definition for music_func goes here
def music_func(genre = "Classic Rock", band = "The Beatles", vocalist = "Freddie Mercury"):
    print("The best kind of music is " + genre)
    print("The best music group is " + band)
    print("The best lead vocalist is " + vocalist)


def main():
    try:
        music, group, singer = input("Input music, group, singer: ").split(',')
        music_func(music, group, singer)
        music_func()
    except ValueError:
        music_func()

main()