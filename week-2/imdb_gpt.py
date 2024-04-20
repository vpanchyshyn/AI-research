"""
IMDB."""
# посилання на завдання на cms: https://cms.ucu.edu.ua/mod/vpl/view.php?id=361864&userid=10019

# ChatGPT у промпті отримав лише початковий код та прохання оптимізувати його роботу.
# З першої спроби він надав код, у якому з 0.62 та 3.16 секунд(перша та друга ф-я відповідно) час скоротився до 
# 0.52 та 1.98 секунд, відповідно. У першій ф-ї це стається завдяки використанню словника для безпосередньої побудови набору
# ключових слів для даного фільму, дозволяючи уникнути непотрібних ітерацій і підвищити продуктивність.
# У другій ж такий підхід уникає непотрібних вкладених циклів.

def find_film_keywords(film_keywords: dict, film_name: str) -> set:
    """
    This function returns the set of all keywords used in the film_name.
    If no such film_name is found, the function returns an empty set.
    >>> find_film_keywords({
    ...     'Action': ['Mr. Bean', 'Fight CLub', 'The Mother'],
    ...     'Dystopia': ['Fight club', 'The Black Mirror', 'The Platform'],
    ...     'Comedy': ['Mr. Bean', 'Fight club', 'The Platform']
    ... }, 'The Mother')
    {'Action'}
    >>> find_film_keywords({
    ...     'Action': ['Mr. Bean', 'Fight club', 'The Mother'],
    ...     'Dystopia': ['Fight club', 'The Black Mirror', 'The Platform'],
    ...     'Comedy': ['Mr. Bean', 'Fight club', 'The Platform']
    ... }, 'Isle of Dogs')
    set()
    """
    return {keyword for keyword, films in film_keywords.items() if film_name in films}

def find_films_with_keywords(film_keywords: dict, num_of_films: int) -> list[tuple]:
    """
    The function returns a list of tuples sorted by the number of keywords 
    (starting with the film with the largest number, if the number is the same, 
    the films should be displayed in lexicographic order).
    >>> find_films_with_keywords({
    ...     'Action': ['Mr. Bean', 'Fight club', 'The Mother'],
    ...     'Dystopia': ['Fight club', 'The Black Mirror', 'The Platform'],
    ...     'Comedy': ['Mr. Bean', 'Fight club', 'The Platform']
    ... }, 3)
    [('Fight club', 3), ('Mr. Bean', 2), ('The Platform', 2)]
    >>> find_films_with_keywords({
    ...     'Action': ['Mr. Bean', 'Fight club', 'The Mother'],
    ...     'Dystopia': ['Fight club', 'The Black Mirror', 'The Platform'],
    ...     'Comedy': ['Mr. Bean', 'Fight club', 'The Platform']
    ... }, 1)
    [('Fight club', 3)]
    >>> find_films_with_keywords({
    ...     'Action': ['Mr. Bean', 'Fight club', 'The Mother'],
    ...     'Dystopia': ['Fight club', 'The Black Mirror', 'The Platform'],
    ...     'Comedy': ['Mr. Bean', 'Fight club', 'The Platform']
    ... }, 0)
    []
    """
    films_count = {}
    for films_for_keyword in film_keywords.values():
        for film in films_for_keyword:
            films_count[film] = films_count.get(film, 0) + 1

    sorted_films = sorted(films_count.items(), key=lambda x: (-x[1], x[0]))
    return sorted_films[:num_of_films] if num_of_films > 0 else []
