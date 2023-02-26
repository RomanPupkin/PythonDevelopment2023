import argparse
from cowsay import cowsay, list_cows
import sys
from os.path import exists

def solve():
    """
    Help on function cowsay in module cowsay:

    cowsay(message, cow='default', preset=None, eyes='oo', tongue='  ', width=40, wrap_text=True, cowfile=None) -> str
    Similar to the cowsay command. Parameters are listed with their 
    corresponding options in the cowsay command. Returns the resulting cowsay
    string

    :param message: The message to be displayed
    :param cow: -f – the available cows can be found by calling list_cows
    :param preset: -[bdgpstwy]
    :param eyes: -e or eye_string
    :param tongue: -T or tongue_string
    :param width: -W
    :param wrap_text: -n
    :param cowfile: a string containing the cow file text (chars are not
    decoded as they are in read_dot_cow) if this parameter is provided the
    cow parameter is ignored

    """
    parser = argparse.ArgumentParser(description="cowsay emulation")
    # -b  -d  -e  -f  -g  -h  -l  -n  -p  -s  -t  -T  -w  -W  -y 
    parser.add_argument("message", type=str, nargs='?', default='', help='message to say')
    parser.add_argument('-b', dest='b', help='Borg mode', action='store_true')
    parser.add_argument('-d', dest='b', help='Dead cow', action='store_true')
    parser.add_argument('-e', dest='e', default='oo', help='Eyes', type=str)
    parser.add_argument('-f', dest='f', default='default', help='Cowfile', type=str)
    parser.add_argument('-g', dest='g', help='Greedy mod', action='store_true')
    parser.add_argument('-n', dest='n', help='Disable text wrapping', action='store_true')
    parser.add_argument('-p', dest='p', help='Paranoia', action='store_true')
    parser.add_argument('-s', dest='s', help='Stoned', action='store_true')
    parser.add_argument('-t', dest='t', help='Tired', action='store_true')
    parser.add_argument('-T', dest='T', default='  ', help='Tongue', type=str)
    parser.add_argument('-w', dest='w', help='Wired mode', action='store_true')
    parser.add_argument('-W', dest='W', default=40, help='Width', type=int)
    parser.add_argument('-y', dest='y', help='Youthful appearance', action='store_true')
    parser.add_argument('-l', dest='l', help='List cowfiles', action='store_true')
    args = parser.parse_args()

    if args.l:
        print(list_cows())
    else:
        preset_list = "bdgpstwy"
        preset = None
        for key, val in args._get_kwargs():
            if key in preset_list[::-1] and val:
                preset = key
                break

        cow_type = args.f
        cow_file = None
        if exists(args.f):
            cow_type = 'default'
            cow_file = args.f
        
        message=""
        if args.message:
            message=args.message
        else:
            lines = []
            for line in sys.stdin:
                lines.append(line.strip())
            message = ''.join(line)

        print(cowsay(message=message,
                    cow=cow_type,
                    preset=preset,
                    eyes=args.e,
                    tongue=args.T,
                    width=args.W,
                    cowfile=cow_file,
                    wrap_text=not args.n))

if __name__ == "__main__":
    solve()
