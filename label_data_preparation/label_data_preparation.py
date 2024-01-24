import argparse
import json

import pandas as pd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", type=str, required=True, help="This is annotated data for a Boundary Detection task, coming from Label Studio in JSON format.")
    parser.add_argument("--output_file", type=str, required=True, help="The output results of the Boundary Detection task's annotated data, saved in CSV format.")
    args = parser.parse_args()

    tokenize_file = open(args.input_file)
    tokenize_data = json.load(tokenize_file)

    results = []
    event_type = None
    event_type_set = {"FIND", "IMP"}
    for data in tokenize_data:
        tokenize_text = list(data["data"]["Text"])
        hosp_id = data["data"]["Hosp_id"]
        text_tag = data["data"]["Tag"]
        if text_tag in event_type_set:
            event_type = text_tag
        section = event_type if text_tag == "EVENT" else text_tag
        ents_sorted = sorted(data["annotations"][0]["result"], key=lambda x: x["value"]["start"])
        shift = 0
        for ent in ents_sorted:
            tokenize_text.insert(ent["value"]["start"] + shift, " ")
            shift += 1
        results.append(("".join(tokenize_text), section, text_tag, hosp_id))

    df_results = pd.DataFrame(results, columns=["Text", "Section", "Tag", "Hosp_id"])
    df_results.to_csv(args.output_file, index=False)


if __name__ == '__main__':
    main()
