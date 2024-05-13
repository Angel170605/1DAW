# **********
# ONLY WORDS
# **********


def run(items: list) -> int:
    items_to_sum = []
    for item in items:
        if isinstance(item, str):
            items_to_sum.append(len(item))
    sum_words = sum(items_to_sum)

    return sum_words


if __name__ == '__main__':
    run([99, 'x', 3, 5, 'hello', 'banana', 4])