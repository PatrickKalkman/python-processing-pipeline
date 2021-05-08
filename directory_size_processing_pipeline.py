import os
import itertools
import glob


def create_processing_pipeline(start_generator, filters):
    generator = start_generator
    for filter in filters:
        generator = filter(generator)
    return generator


def search_filter(paths):
    for path in paths:
        return itertools.chain(glob.iglob(path + '/**', recursive=True),
                               glob.iglob(path + '/.**', recursive=True))


def size_filter(files):
    for file in files:
        yield os.path.getsize(file)


def sum_filter(size):
    yield sum(size)


filters = [
    search_filter,
    size_filter,
    sum_filter,
]

pipeline = create_processing_pipeline(
    ['./'], filters)

print(next(pipeline))
