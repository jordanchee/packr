# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""

import pytest
from webtest import TestApp

from packr.app import create_app
from packr.settings import TestConfig


@pytest.yield_fixture(scope='function')
def app():
    """An application for the tests."""
    _app = create_app(config_object=TestConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def testapp(app):
    """A Webtest app."""
    return TestApp(app)
