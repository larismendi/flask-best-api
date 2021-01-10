from pytest import fixture
from app.widget.model import Widget
from app.widget.interface import WidgetInterface


@fixture
def interface() -> WidgetInterface:
    return WidgetInterface(widget_id=1, name="Test widget", purpose="Test purpose")


def test_WidgetInterface_create(interface: WidgetInterface):
    assert interface


def test_WidgetInterface_works(interface: WidgetInterface):
    widget = Widget(**interface)
    assert widget