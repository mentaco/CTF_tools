import argparse
import textwrap
import itertools

def create_wordlist(str_list, num, path):
    elem = set(str_list)
    for w in list(elem):
        elem.add(w.lower())

    try:
        with open(str(path), "w") as f:
            for comb in itertools.combinations(sorted(elem), num):
                for perm in itertools.permutations(sorted(comb)):
                    s = "".join(perm)
                    f.write(f"{s}\n")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=textwrap.dedent('Combine strings and output to a file.'),
        add_help=True,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        'strings',
        nargs='*',
        type=str,
        help='Input the string you want to combine.'
    )

    parser.add_argument(
        '-n',
        type=int,
        default=2,
        metavar='number',
        help='Specify the number of elements to combine.',
    )

    parser.add_argument(
        '-o',
        type=str,
        default='wordlist.txt',
        metavar='filename',
        help='Specify the path to a file to output the generated strings.',
    )

    args = parser.parse_args()
    
    if len(args.strings) > 1:
        create_wordlist(args.strings, args.n, args.o)
    else:
        print("Arguments are few.")
        print("At least two strings are required.\n")
        print("Use --help to list all available options.\n")
