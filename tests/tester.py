from framework.Endpoints.ApiPost import PostApi
from config.testconf import work_with_database


def test_step(work_with_database):
    posts = PostApi()
    posts.get_posts()
    assert posts.check_if_json(), 'not json'
    assert posts.check_if_sorted_by_id(), 'not sorted by id'

