def is_isbn_or_key(word):
    """
    helper function to check the keyword is key or isbn
    """
    # parameters: q/isbn ; (start count) = page
    # 如果是q调用keyword api，如果是isbn就要调用isbn api
    # 默认user用的是keyword
    # isbn分为isbn13（13个0-9的数字） 和 isbn10（10个0-9的数字，但会含有-）
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
