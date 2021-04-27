def file_filter(file_names):
    for file_name in file_names:
        with open(file_name, "r") as file:
            yield file


def line_filter(open_files):
    for open_file in open_files:
        for file in open_file:
            yield file


def bytes_filter(file):
    for line in file:
        bytes_string = line.rsplit(None, 1)[1]
        yield bytes_string


def convert_bytes_filter(bytes_string):
    return (int(bytes) for bytes in bytes_string if bytes != '-')


def sum_filter(bytes):
    yield sum(bytes)


def create_processing_pipeline(start_generator, filters):
    generator = start_generator
    for filter in filters:
        generator = filter(generator)
    return generator


filters = [
    file_filter,
    line_filter,
    bytes_filter,
    convert_bytes_filter,
    sum_filter,
]

pipeline = create_processing_pipeline(
    ['./apache_access.log'], filters)

print(next(pipeline))
