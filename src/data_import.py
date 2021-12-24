import sqlite3

import pandas as pd


def import_data() -> pd.DataFrame:
    with open("sql/data_import.sql", "r") as f:
        query = f.read()

    with sqlite3.connect("data/plexdata.db") as conn:
        data = pd.read_sql_query(query, conn)

    data["duration"] = data["duration"] / 1000 / 60

    return data


def main():
    data = import_data()
    print(data)


if __name__ == '__main__':
    main()
