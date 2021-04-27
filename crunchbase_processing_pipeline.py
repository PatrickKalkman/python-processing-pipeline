import csv
import logging


def log_filter(input):
    log = logging.getLogger("log_filter")
    handler = logging.StreamHandler()
    log.addHandler(handler)
    log.setLevel(logging.INFO)

    for item in input:
        log.info(f"{input} => {item}")
        yield item


def file_filter(file_names):
    for file_name in file_names:
        with open(file_name, "r") as file:
            yield file


def dict_filter(open_files):
    for open_file in open_files:
        dict_reader = csv.DictReader(open_file)
        for row in dict_reader:
            yield row


def serie_a_filter(dict_row):
    for item in dict_row:
        if item["round"] == "a":
            yield item


def sum_filter(dict_row):
    sum = 0
    for item in dict_row:
        sum += int(item["raisedAmt"])
    yield sum


def create_processing_pipeline(start_generator, filters):
    generator = start_generator
    for filter in filters:
        generator = filter(generator)
    return generator


filters = [
    file_filter,
    dict_filter,
    serie_a_filter,
    log_filter,
    sum_filter,
]

pipeline = create_processing_pipeline(
    ['./crunchbase_funding.csv'], filters)

print(next(pipeline))
