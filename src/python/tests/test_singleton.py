from designpatterns_examples.creational.singleton.settings import AppSettings


def test_singleton_same_instance() -> None:
    AppSettings._instance = None  # noqa: SLF001 - reset for test isolation
    a = AppSettings()
    b = AppSettings()
    assert a is b


def test_singleton_shared_state() -> None:
    AppSettings._instance = None  # noqa: SLF001
    s = AppSettings()
    s.set("x", 1)
    t = AppSettings()
    assert t.get("x") == 1
