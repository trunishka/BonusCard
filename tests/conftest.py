import pytest


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass

@pytest.fixture(autouse=True)
def set_debug(settings):
    """Regardless of the value of the DEBUG setting in your configuration file, all Django tests run with
    DEBUG=False. This is to ensure that the observed output of your code matches what will be seen in a production
    setting. """
    settings.DEBUG = True
    assert settings.DEBUG