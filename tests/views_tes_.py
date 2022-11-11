# import pytest
import app


class TestViews:
    """
    Тестируюет views в blueprint
    """

    def test_all_posts(self):
        test_client = app.app.test_client()
        response = test_client.get("/")
        assert response.status_code == 200

    def test_post_pk(self):
        test_client = app.app.test_client()
        response = test_client.get("/posts/1")
        assert response.status_code == 200

    def test_search(self):
        test_client = app.app.test_client()
        response = test_client.get("/search")
        assert response.status_code == 200

    def test_tag(self):
        test_client = app.app.test_client()
        response = test_client.get("/tag/")
        assert response.status_code == 200

    def test_bookmarks(self):
        test_client = app.app.test_client()
        response = test_client.get("/bookmarks/")
        assert response.status_code == 200

    def test_add_bookmarks_page(self):
        test_client = app.app.test_client()
        response = test_client.get("/bookmarks/add/1")
        assert response.status_code == 200

    def test_remove_bookmarks(postid):
        test_client = app.app.test_client()
        response = test_client.get("/bookmarks/remove/1")
        assert response.status_code == 200
