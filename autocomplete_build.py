import autocompleter
import sys


def build():
    my_autocompleter = autocompleter.Autocompleter()
    my_autocompleter.import_json("sample_conversations.json")
    my_autocompleter.save()

if __name__ == "__main__":
    sys.exit(build())
