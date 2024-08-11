import argparse as ap
import pickle as pk
import sys
from pathlib import PurePath
from typing import Any, List

import pandas as pd

EXT: List[str] = [
    "pkl",
    "ftr",
    "json",
    "xlsx",
    "csv",
    "md",
    "latex",
    "parquet",
    "arrow",
]
EXT_SAVE_FUNC: str = ""

parser = ap.ArgumentParser(
    description="""
Convert a pandas dataframe in pickle format to another format. Mainly useful if you want to use the dataframe in another environment, like R or Julia.
"""
)

parser.add_argument(
    "-i",
    help="pickle file containing a pandas dataframe.",
    required=True,
    dest="infile",
)
parser.add_argument(
    "-o",
    help=f"""
    pickle file containing a pandas dataframe. File extension determines the output type. Choose an extension of {EXT}. Separate multiple files with spaces.""",
    nargs="*",
    dest="ofiles",
    default=[],
)
parser.add_argument(
    "-x", help=f"Write to stdout. Specify the type, one of {EXT}", dest="x"
)


def eprint(*a, **kw) -> Any:
    print(file=sys.stderr, *a, **kw)


def main() -> None:
    eprint("Hi")
    a = parser.parse_args()
    eprint(a)

    if a.infile:
        df = pd.read_pickle(a.infile)
    else:
        # May or may not work --> Maybe use Try/Except/Finally block?
        df = pk.load(sys.stdin.buffer)

    # create a map from file extension desired to a function to produce it.
    write_funcs = [
        df.to_pickle,
        df.to_feather,
        df.to_json,
        df.to_excel,
        df.to_csv,
        df.to_markdown,
        df.to_latex,
        df.to_parquet,
    ]

    f_map = dict(zip(EXT, write_funcs))
    k = f_map.keys()
    eprint(f"\nKeys: {k}")

    for ofile in a.ofiles:
        suffix = (PurePath(ofile).suffix)[1:]  # removing the period from the suffix
        f_map[suffix](
            ofile
        )  # select the function and write to the file. Traceback if user specifies invalid extension.

    if a.x:
        f_map[a.x](
            sys.stdout
        )  # select the filetype for stdout. Traceback if invalid or isnt supplied.


main()
