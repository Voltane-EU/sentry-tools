from . import decorators

try:
    from sentry_sdk import set_user, set_extra

except ImportError:
    def set_user(data):
        pass

    def set_extra(key, data):
        pass
