import argparse
import cowsay
import sys

def solve():
    parser = argparse.ArgumentParser(description="cowsay emulation")
    # -b  -d  -e  -f  -g  -h  -l  -n  -p  -s  -t  -T  -w  -W  -y 
    parser.add_argument('-b', dest='b', help='Borg mode', action='store_true')
    parser.add_argument('-d', dest='b', help='Dead cow', action='store_true')
    parser.add_argument('-e', dest='e', default='oo', help='Eyes')
    parser.add_argument('-f', dest='f', default='default', help='Cowfile')
    parser.add_argument('-g', dest='g', help='Greedy mod', action='store_true')
    parser.add_argument('-n', dest='n', help='Disable text wrapping', action='store_true')
    parser.add_argument('-p', dest='p', help='Paranoia', action='store_true')
    parser.add_argument('-s', dest='s', help='Stoned', action='store_true')
    parser.add_argument('-t', dest='t', help='Tired', action='store_true')
    parser.add_argument('-T', dest='T', default='  ', help='Tongue')
    parser.add_argument('-w', dest='w', help='Wired mode', action='store_true')
    parser.add_argument('-W', dest='W', default=40, help='Width')
    parser.add_argument('-y', dest='y', help='Youthful appearance', action='store_true')
    parser.add_argument('-l', dest='l', help='List cowfiles', action='store_true')
    args = parser.parse_args()

    if args.l:
        print(cowsay.list_cows())
    else:
        print("test")


if __name__ == "__main__":
    solve()
    #print(cowsay.cows_list())
