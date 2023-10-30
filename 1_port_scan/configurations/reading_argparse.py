import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog='CLI Looking for open ports',
        usage='%(prog)s port_scanner_1.py '
              '[--targets] '
              '[--ports] ',
        description='Identify all open ports')
    parser.add_argument(
        '-t',
        '--targets',
        type=str,
        help='Enter Targets To Scan(split them by ",")',
        required=True)
    parser.add_argument(
        '-p',
        '--ports',
        type=str,
        help='Enter How Many Ports You Want To Scan',
        required=True)
    args = parser.parse_args()
    return args


def get_argparse():
    args = parse_args()
    targets = args.targets
    ports = int(args.ports)

    return targets, ports
