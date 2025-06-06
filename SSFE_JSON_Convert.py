"""Convert raw save data into a JSON compatible dictionary."""

import json


def convert_raw_to_json(
    path: str = "INPUT.txt", output: str | None = "INPUT.json"
) -> dict:
    """Read ``path`` and return a dictionary with chapter states.

    If ``output`` is provided, the resulting dictionary is also written to that
    JSON file.
    """
    with open(path, "r") as f:
        variables = f.read()

    variables = variables.replace(" ", "").replace("\n", "")

    variables_dict = {}
    for variable in variables.split(","):
        key, value = variable.split(":")
        key = key.replace('"', "")
        value = int(value.replace('"', ""))
        variables_dict[key] = {"is_viewed": value}

    if output:
        with open(output, "w") as f:
            json.dump(variables_dict, f, indent=4)

    return variables_dict


def main() -> None:
    data = convert_raw_to_json()
    print(json.dumps(data))


if __name__ == "__main__":
    main()
