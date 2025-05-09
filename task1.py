# Initial list of users
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

# Function to add a new user
def add_user(user_list, user):
    user_list.append(user)
    print(f"User {user['name']} added successfully.")

# Function to retrieve a user by ID
def get_user_by_id(user_list, user_id):
    for user in user_list:
        if user['id'] == user_id:
            print(f"User found: {user}")
            return user
    print(f"User with id {user_id} not found.")
    return None

# Function to update user information by ID
def update_user(user_list, user_id, updated_info):
    for user in user_list:
        if user['id'] == user_id:
            user.update(updated_info)
            print(f"User with id {user_id} updated successfully.")
            return True
    print(f"User with id {user_id} not found.")
    return False

# Function to delete a user by ID
def delete_user(user_list, user_id):
    for user in user_list:
        if user['id'] == user_id:
            user_list.remove(user)
            print(f"User with id {user_id} deleted successfully.")
            return True
    print(f"User with id {user_id} not found.")
    return False

# ------ Example Operations ------
print("Initial users:", users)

# Adding a new user
new_user = {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
add_user(users, new_user)

# Retrieving a user
get_user_by_id(users, 2)

# Updating a user
update_user(users, 1, {"email": "alice_new@example.com"})

# Deleting a user
delete_user(users, 3)

# Final list of users
print("Final users:", users)
