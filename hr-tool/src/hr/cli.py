from argparse import ArgumentParser
from genericpath import isfile


def parse():
    parser = ArgumentParser(
        description="System's user info into file"
    )
    parser.add_argument(
        '--format', '-f',
        default='json',
        choices=['json', 'csv'],
        help='The format of final file'
    )
    parser.add_argument(
        '--path', '-p',
        help='File location'
    )

    return parser.parse_args()


def main():
    import sys
    from hr import users

    args = parse()
    is_file = True
    if args.path:
        file = open(args.path, 'w', newline='')
    else:
        file = sys.stdout
        is_file = False

    try:
        if args.format == 'json':
            users.to_json(file)
        elif args.format == 'csv':
            users.to_csv(file)
        else:
            raise Exception(f"Unsupported format {args.format}")

        print(
            f"\nResult is written to {file.name if args.path else 'to console'}")
    finally:
        if is_file:
            file.close()
