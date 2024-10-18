import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"  # get the value of text input
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todos")

# Display the To-Dos with checkboxes
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add a new todo...",
              key="new_todo", on_change=add_todo)  # Call back function
