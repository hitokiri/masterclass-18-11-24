#!/usr/bin/env python3
from dataclasses import dataclass, field
from typing import Callable, List

from managment_data.crud import fetch_tasks, save_to_db, delete_from_db, edit_in_db
from nicegui import ui
from config.config import HASURA_GRAPHQL_URL, HASURA_GRAPHQL_ADMIN_SECRET

print(f"hasura_url: {HASURA_GRAPHQL_URL}")
print(f"hasura_secret: {HASURA_GRAPHQL_ADMIN_SECRET}")

@dataclass
class TodoItem:
    id: int
    name: str
    done: bool = False


@dataclass
class ToDoList:
    title: str
    on_change: Callable
    items: List[TodoItem] = field(default_factory=list)

    def add(self, id: int, name: str, done: bool = False, save: bool = True) -> None:
        self.items.append(TodoItem(id, name, done))
        self.on_change()
        if save:
            save_to_db(name, done)
            ui.notify(f'Task "{name}" added successfully!', type='positive', position='top')

    def remove(self, item: TodoItem) -> None:
        self.items.remove(item)
        self.on_change()
        delete_from_db(item.id)
        ui.notify(f'Task "{item.name}" removed successfully!', type='negative', position='top')

    def edit(self, id: int, new_name: str, done: bool) -> None:
        for item in self.items:
            if item.id == id:
                old_name = item.name
                item.name = new_name
                item.done = done
                break
        self.on_change()
        edit_in_db(id, new_name, done)
        ui.notify(f'Task "{old_name}" updated to "{new_name}"!', type='info', position='top')


@ui.refreshable
def todo_ui():
    if not todos.items:
        ui.label('List is empty.').classes('mx-auto')
        return
    ui.linear_progress(sum(item.done for item in todos.items) / len(todos.items), show_value=False)
    with ui.row().classes('justify-center w-full'):
        ui.label(f'Completed: {sum(item.done for item in todos.items)}')
        ui.label(f'Remaining: {sum(not item.done for item in todos.items)}')
    for item in todos.items:
        with ui.row().classes('items-center'):
            ui.checkbox(value=item.done, on_change=lambda e, item=item: todos.edit(item.id, item.name, e.value)).bind_value(item, 'done') \
                .mark(f'checkbox-{item.name.lower().replace(" ", "-")}')
            ui.input(value=item.name).classes('flex-grow').bind_value(item, 'name').on('keydown.enter', lambda e, item=item: todos.edit(item.id, e.sender.value, item.done))
            ui.button(on_click=lambda item=item: todos.remove(item), icon='delete').props('flat fab-mini color=grey')


todos = ToDoList('My Weekend-class', on_change=todo_ui.refresh)

# Fetch tasks from Hasura and add them to the todo list without saving to the database
tasks = fetch_tasks()
for task in tasks:
    todos.add(task['id'], task['title'], task['completed'], save=False)

with ui.card().classes('w-80 items-stretch'):
    ui.label().bind_text_from(todos, 'title').classes('text-semibold text-2xl')
    todo_ui()
    add_input = ui.input('New item').classes('mx-12').mark('new-item')
    add_input.on('keydown.enter', lambda: todos.add(None, add_input.value))
    add_input.on('keydown.enter', lambda: add_input.set_value(''))

if __name__ in {'__main__', '__mp_main__'}:
    ui.run()