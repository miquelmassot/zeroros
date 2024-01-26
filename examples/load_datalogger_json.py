"""
Example of loading a datalogger json file and saving the data as a csv file.
"""

import json
import pandas as pd
import argparse


def flatten_dict(nested_dict):
    res = {}
    if isinstance(nested_dict, dict):
        for k in nested_dict:
            flattened_dict = flatten_dict(nested_dict[k])
            for key, val in flattened_dict.items():
                key = list(key)
                key.insert(0, k)
                res[tuple(key)] = val
    else:
        res[()] = nested_dict
    return res


def rename_dict_keys(nested_dict):
    # Rename tupled keys to be joined by "_", e.g. (a, b, c) -> a_b_c
    new_dict = {}
    count = 0
    for k, v in nested_dict.items():
        if isinstance(k, tuple):
            new_dict[("_".join(k))] = v
            if count > 2:
                break
    return new_dict


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("input", type=str, help="Input json file")
    parser.add_argument(
        "--output", type=str, default="datalogger_output.csv", help="Output csv file"
    )
    args = parser.parse_args()

    data = []
    with open(args.input, "r") as f:
        for line in f:
            data.append(json.loads(line))

    flatten_data = []
    for d in data:
        flatten_data.append(rename_dict_keys(flatten_dict(d)))

    df = pd.DataFrame(flatten_data)
    df.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()
