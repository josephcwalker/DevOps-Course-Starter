from todo_app.data.trello_items import Item
from todo_app.view_model import ViewModel


def test_view_model_todo_items():
    expected_todo_items = [
        Item(1, "thing to do"),
        Item(2, "test 2"),
    ]
    view_model = ViewModel([
        Item(3, "test3", "In Progress"),
        Item(3, "test3", "Done"),
        *expected_todo_items,
    ])

    todo_items = view_model.todo_items

    assert set(todo_items) == set(expected_todo_items)


def test_view_model_in_progress_items():
    expected_in_progress_items = [
        Item(1, "test1", "In Progress"),
        Item(2, "test2", "In Progress"),
    ]
    view_model = ViewModel([
        Item(3, "todo"),
        Item(4, "Done", "Done"),
        *expected_in_progress_items,
    ])

    in_progress_items = view_model.in_progress_items

    assert set(in_progress_items) == set(expected_in_progress_items)


def test_view_model_done_items():
    expected_done_items = [
        Item(2, "test2", "Done"),
    ]
    view_model = ViewModel([
        Item(1, "test1"),
        Item(2, "test2", "In Progress"),
        *expected_done_items,
    ])

    done_items = view_model.done_items

    assert set(done_items) == set(expected_done_items)
