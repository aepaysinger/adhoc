from unittest.mock import patch

from postgres.candy_friends import show_favorite_candy


@patch("postgres.candy_friends.get_friends_and_candy")
def test_show_favorite_candy(get_friends_and_candy_mock):
    get_friends_and_candy_mock.return_value = [['starbursts', 'rusty'], ['milk dud', 'choco'], ['starbursts', 'lemon']]
    assert show_favorite_candy() == {'starbursts': ['rusty', 'lemon'],
                                    'milk dud': ['choco']}
