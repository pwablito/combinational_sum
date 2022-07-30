from combinational_sum.gui.app import App

import argparse
import sys


def main():
    parser = argparse.ArgumentParser("Combinational Sum Solver")
    parser.add_argument("--no-gui", action="store_true")
    args = parser.parse_args()
    if args.no_gui:
        # TODO implement the non-gui version of the application
        pass
    else:
        sys.exit(App().run())


if __name__ == "__main__":
    main()
