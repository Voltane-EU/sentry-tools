from contextlib import contextmanager
try:
    from sentry_sdk import Hub, start_span  # type: ignore # noqa

except ImportError:
    Hub = None

    @contextmanager
    def start_span(span=None, **kwargs):
        yield


def set_tag(key, value):
    try:
        Hub.current.scope.span.set_tag(key, value)

    except AttributeError:
        pass


def set_data(key, value):
    try:
        Hub.current.scope.span.set_data(key, value)

    except AttributeError:
        pass
