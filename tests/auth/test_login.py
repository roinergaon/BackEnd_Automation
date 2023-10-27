from lib.auth import Auth
from config import APP_URL, LOG

def test_login():
    LOG.info("test_login")
    response = Auth().login(APP_URL, "admin", "admin")
    LOG.debug(response.json())
    assert response.ok