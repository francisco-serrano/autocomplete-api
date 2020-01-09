from services import autocompleter
import sys


def build():
    my_autocompleter = autocompleter.Autocompleter()
    my_autocompleter.import_json()


if __name__ == "__main__":
    sys.exit(build())
