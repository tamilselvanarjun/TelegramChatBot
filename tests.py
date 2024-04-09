def test_generate_random_technology_keyword():
    keyword = generate_random_technology_keyword()
    assert keyword in technology_keywords
