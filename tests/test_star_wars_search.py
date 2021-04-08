from star_wars_api import starwars_search


def test_load_response():
    api_instance = starwars_search.StarWarsSearch()
    api_instance.load_response('films')
    assert len(api_instance.response_info) > 0


def test_load_next_response():
    api_instance = starwars_search.StarWarsSearch()
    api_instance.load_response('planets')
    api_instance.load_next_response()
    assert len(api_instance.response_info) > 0


def test_attribute_name_marge_films():
    api_instance = starwars_search.StarWarsSearch()
    api_instance.load_response('films')
    api_instance.attribute_name_marge('episode_id', 'films')
    assert len(api_instance.get_output) > 0


def test_attribute_name_marge_any():
    api_instance = starwars_search.StarWarsSearch()
    api_instance.load_response('starships')
    api_instance.attribute_name_marge('manufacturer', 'starships')
    assert len(api_instance.get_output) > 0


def test_get_function_films():
    api_instance = starwars_search.StarWarsSearch()
    api_instance.load_response('films')
    api_instance.get_function('films', 'episode_id')
    assert len(api_instance.get_output) > 0


def test_get_function_any():
    api_instance = starwars_search.StarWarsSearch()
    api_instance.load_response('starships')
    api_instance.get_function('starships', 'manufacturer')
    assert len(api_instance.get_output) > 0


def test_attribute_search():
    api_instance = starwars_search.StarWarsSearch()
    api_instance.load_response('vehicles')
    api_instance.attribute_search('manufacturer', 'Corellia Mining Corporation')
    assert len(api_instance.output) > 0


def test_starwars_search():
    api_instance = starwars_search.StarWarsSearch()
    api_instance.starwars_search('vehicles', 'manufacturer', 'Corellia Mining Corporation')
    assert len(api_instance.output) > 0


def test_asc():
    api_instance = starwars_search.StarWarsSearch()
    api_instance.get_output = {'d': 4, 'b': 2, 'a': 1, 'c': 3}
    expected_output = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    api_instance.asc()
    assert expected_output == api_instance.get_output


def test_desc():
    api_instance = starwars_search.StarWarsSearch()
    api_instance.get_output = {'d': 4, 'b': 2, 'a': 1, 'c': 3}
    expected_output = [(4, 'd'), (3, 'c'), (2, 'b'), (1, 'a')]
    api_instance.desc()
    assert expected_output == api_instance.get_output



























