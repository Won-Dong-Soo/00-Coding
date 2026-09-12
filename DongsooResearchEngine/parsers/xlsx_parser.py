import pandas as pd

def parse_xlsx(path):

    sheets = pd.read_excel(
        path,
        sheet_name=None
    )

    text = []

    for _, df in sheets.items():

        text.append(
            df.to_string()
        )

    return "\n".join(text)