import requests
from config.config import HASURA_GRAPHQL_URL, HASURA_GRAPHQL_ADMIN_SECRET

def save_to_db(name: str, done: bool, description: str = "") -> None:
    print(f"saving to db name: {name} done: {done}")
    mutation = """
    mutation InsertTodo($title: String!, $completed: Boolean!, $description: String!) {
        insertTodos(objects: {title: $title, completed: $completed, description: $description}) {
            affectedRows
        }
    }
    """
    variables = {
        'title': name,
        'completed': done,
        'description': description
    }
    headers = {
        'Content-Type': 'application/json',
        'x-hasura-admin-secret': HASURA_GRAPHQL_ADMIN_SECRET
    }
    response = requests.post(HASURA_GRAPHQL_URL, json={'query': mutation, 'variables': variables}, headers=headers)
    print(f"response status: {response.status_code}")
    print(f"response text: {response.text}")
    if response.status_code != 200:
        raise Exception(f"Mutation failed to run by returning code of {response.status_code}. {response.text}")

def delete_from_db(id: int) -> None:
    print("deleting from db")
    mutation = """
    mutation DeleteTodos($id: Int!) {
        deleteTodos(where: {id: {_eq: $id}}) {
            affectedRows
        }
    }
    """
    variables = {
        'id': id
    }
    headers = {
        'Content-Type': 'application/json',
        'x-hasura-admin-secret': HASURA_GRAPHQL_ADMIN_SECRET
    }
    response = requests.post(HASURA_GRAPHQL_URL, json={'query': mutation, 'variables': variables}, headers=headers)
    print(f"response status: {response.status_code}")
    print(f"response text: {response.text}")
    if response.status_code != 200:
        raise Exception(f"Mutation failed to run by returning code of {response.status_code}. {response.text}")

def edit_in_db(id: int, new_name: str, done: bool) -> None:
    mutation = """
    mutation ($id: Int!, $new_title: String!, $completed: Boolean!) {
        updateTodos(where: {id: {_eq: $id}}, _set: {title: $new_title, completed: $completed}) {
            affectedRows
        }
    }
    """
    variables = {
        'id': id,
        'new_title': new_name,
        'completed': done
    }
    headers = {
        'Content-Type': 'application/json',
        'x-hasura-admin-secret': HASURA_GRAPHQL_ADMIN_SECRET
    }
    response = requests.post(HASURA_GRAPHQL_URL, json={'query': mutation, 'variables': variables}, headers=headers)
    print(f"response status: {response.status_code}")
    print(f"response text: {response.text}")
    if response.status_code != 200:
        raise Exception(f"Mutation failed to run by returning code of {response.status_code}. {response.text}")

def fetch_tasks():
    query = """
    query {
        todos {
            id
            title
            completed
        }
    }
    """
    headers = {
        'Content-Type': 'application/json',
        'x-hasura-admin-secret': HASURA_GRAPHQL_ADMIN_SECRET
    }
    response = requests.post(HASURA_GRAPHQL_URL, json={'query': query}, headers=headers)
    print(f"response status: {response.status_code}")
    print(f"response text: {response.text}")
    if response.status_code == 200:
        return response.json()['data']['todos']
    else:
        raise Exception(f"Query failed to run by returning code of {response.status_code}. {response.text}")