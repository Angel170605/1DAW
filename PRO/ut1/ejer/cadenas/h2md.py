# ****************************
# CONVIRTIENDO HTML A MARKDOWN
# ****************************


def run(html: str) -> str:
    hashtag_product = html[2]
    clean_word = html[4:-5]
    hashtags = '#' * int(hashtag_product)
    markdown = str(hashtags) + (' ') + clean_word
    return markdown


if __name__ == '__main__':
    run('<h1>Core</h1>')
