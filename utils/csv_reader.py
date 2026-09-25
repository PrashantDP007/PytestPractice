import csv
import os


class CSVReader:

    @staticmethod
    def read_csv(file_name):
        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "test_data",
            file_name
        )

        with open(
            file_path,
            mode="r",
            newline="",
            encoding="utf-8"
        ) as file:

            return list(csv.DictReader(file))