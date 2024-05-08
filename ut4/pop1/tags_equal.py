# **********************
# ETIQUETAS EQUIVALENTES
# **********************


def tags_cleaner(tag1: str, tag2: str) -> tuple:
    tag1 = (tag1.strip('<>')).lower()
    tag2 = (tag2.strip('<>')).lower()
    return tag1, tag2


def run(tag1: str, tag2: str) -> bool:
    tag1, tag2 = tags_cleaner(tag1, tag2)
    return (tag1.split(' '))[0] == (tag2.split(' '))[0]
