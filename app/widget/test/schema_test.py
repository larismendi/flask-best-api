from pytest import fixture

from app.widget.model import Widget
from app.widget.schema import WidgetSchema
from app.widget.interface import WidgetInterface


@fixture
def schema() -> WidgetSchema:
    return WidgetSchema()


def test_WidgetSchema_create(schema: WidgetSchema):
    assert schema


def test_WidgetSchema_works(schema: WidgetSchema):
    params: WidgetInterface = schema.load(
        {"widgetId": "123", "name": "Test widget", "purpose": "Test purpose"}
    )
    widget = Widget(**params)

    assert widget.widget_id == 123
    assert widget.name == "Test widget"
    assert widget.purpose == "Test purpose"