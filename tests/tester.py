from framework.Endpoints.ApiPost import PostApi
from config.testconf import first_test


def test_step(first_test):
    posts = PostApi()
    posts.get_posts()
    assert posts.check_if_json(), 'not json'
    assert posts.check_if_sorted_by_id(), 'not sorted by id'

