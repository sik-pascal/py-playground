from argparse import Action, ArgumentParser


class DriverAction(Action):
    def __call__(self, parser: ArgumentParser, namespace, values, option_string=None) -> None:
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination.lower()


def create_parser():
    parser = ArgumentParser(
        description="Back up PostgrresSql db locally or to S3"
    )
    parser.add_argument(
        "url",
        help="Url of the db to backup"
    )
    parser.add_argument(
        "--driver", '-d',
        help="driver name & destination",
        metavar=("DRIVER", "DESTINATION"),
        nargs=2, action=DriverAction, required=True
    )
    return parser


def main():
    import boto3
    import time
    from pgbackup import pgdump, storage

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    print(f"About to back up db to {args.destination} using {args.driver}")
    if args.driver == 's3':
        timestamp = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
        file_name = pgdump.dump_file_name(args.url, timestamp)
        client = boto3.client('s3')
        storage.s3(client, dump.stdout, args.destination, file_name)
        print(f"Object {file_name} has been added to {args.destination}")
    else:
        outfile = open(args.destination, 'wb')
        storage.local(dump, outfile)
