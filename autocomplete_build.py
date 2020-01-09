from core.autocompleter import Autocompleter
import sys


def build():
    my_autocompleter = Autocompleter()
    my_autocompleter.import_json()


if __name__ == "__main__":
    sys.exit(build())
