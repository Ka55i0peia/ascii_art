from pyfiglet import figlet_format


def main(text='hi there!'):
    print(figlet_format(text, font='univers'))


if __name__ == '__main__':
    main()
