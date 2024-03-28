import argparse
import subprocess, sys

def main():
    parser = argparse.ArgumentParser(description='Process some arguments')
    parser.add_argument('-m', '--message', type=str, help='Message')
    parser.add_argument('-p', '--push', nargs='+', help='Push')

    args = parser.parse_args()

    subprocess.run("git add .", shell = True, executable="/bin/bash")

    if args.message:
        subprocess.run(f"git commit -m '{args.message}' ", shell = True, executable="/bin/bash")

    if args.push:
        if len(args.push) < 2:
            print("Required both remote branch and local. \n\tExample: -p origin main")
            return
        print(args.push[1])
        subprocess.run(f"git push -u {args.push[0]} {args.push[1]} ", shell = True, executable="/bin/bash")


if __name__ == "__main__":
    main()
