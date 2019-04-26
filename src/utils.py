import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def json_print(json_str):
    print(bcolors.OKBLUE + "__________________________________________________________" + bcolors.ENDC)
    print()
    print(bcolors.OKBLUE + json.dumps(json_str, indent=4, sort_keys=True) + bcolors.ENDC)
    print(bcolors.OKBLUE + "__________________________________________________________" + bcolors.ENDC)