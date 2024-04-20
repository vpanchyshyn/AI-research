"""
This module contains 2 functions. The first function returns the set of all \
    keywords used in the film, while the second one returns a list of films \
    that have the most keywords.
"""
# link on cms: https://cms.ucu.edu.ua/mod/vpl/view.php?id=306656&userid=10019

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
    keywords_of_film = set()
    for keyword, films in film_keywords.items():
        if film_name in films:
            keywords_of_film.add(keyword)

    return keywords_of_film

def find_films_with_keywords(film_keywords: dict, num_of_films: int) -> list[tuple]:
    """
    The function returns a list of tuples sorted by the number of keywords \
        (starting with the film with the largest number, if the number is \
        the same, the films should be displayed in lexicographic order).
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
    films = []
    if num_of_films == 0:
        return films

    for films_for_keyword in film_keywords.values():
        for film in films_for_keyword:
            for i, (film_name, keyword_count) in enumerate(films):
                if film_name == film:
                    films[i] = (film_name, keyword_count + 1)
                    break
            else:
                films.append((film, 1))
    films = sorted(films, key=lambda x: (-x[1], x[0]))
    return films[:num_of_films]
