import streamlit as st
import functions

# Custom CSS for better appearance
st.markdown(
    """
    <style>
    .main-title {
        font-size: 30px;
        color: #4CAF50;
        text-align: center;
        margin-top: -50px;
    }
    .input-field {
        margin: 20px 0;
    }
    .completed-todo {
        text-decoration: line-through;
        color: gray;
    }
    .add-button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .add-button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True
)

# Load todos from the file
todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    if todo:
        todos.append(todo)
        update_todo_file(todos)
        st.success(f'Task "{todo}" added!')
        st.session_state["new_todo"] = ""


def complete_todo(index):
    todos.pop(index)
    update_todo_file(todos)


def update_todo_file(todos):
    with open('todos.txt', 'w') as file:
        file.writelines([todo.strip() + "\n" for todo in todos if todo.strip()])

# Main App Layout
st.markdown('<h1 class="main-title">My Todos</h1>', unsafe_allow_html=True)

# Display the list of todos with checkboxes
for index, todo in enumerate(todos):
    clean_todo = todo.strip()
    checkbox = st.checkbox(clean_todo, key=f"{clean_todo}_{index}")

    if checkbox:
        complete_todo(index)
        todo_key = f"{clean_todo}_{index}"
        if todo_key in st.session_state:
            del st.session_state[todo_key]
        st.rerun()

# Input section for adding new To-Dos
st.markdown('<div class="input-field">', unsafe_allow_html=True)
st.text_input(label="", placeholder="Add a new task...", key="new_todo", on_change=add_todo)
st.markdown('</div>', unsafe_allow_html=True)
