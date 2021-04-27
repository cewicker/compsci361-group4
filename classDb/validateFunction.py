from mymodels import User


def validate_user(a: User):
    new_user = a
    error_list = []
    if a.first_name == "":
        error_list.append("First name can't be empty")
    if a.last_name == "":
        error_list.append("Last name can't be empty")
    if a.email == "":
        error_list.append("Enter a valid email")
    if a.number == "":
        error_list.append("Please enter a valid phone number")
    if a.assignment_ID == "":
        error_list.append("Enter a valid assignment ID")
    if a.role == "":
        error_list.append("User must be given a role")
    if(a.user_id == ""):
        error_list.append("User must be given a user ID")

    return error_list
