from db_management import get_db_connection


def add_user(firstname, lastname, username, email, dob, password, gender, profile):
    """
    Adds a new user to the database.
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""INSERT INTO User 
            (firstName, lastName, username, email, DOB, password, gender, profile) 
            VALUES (%s, %s, %s, %s, %s, %s. %s, %s """, [firstname, lastname, username, email, dob, password, gender, profile])
            return


def username_available(username):
    """
    NEEDS MORE WORK
    Finds whether a particular username already exists in the database.
    *(Tables involved: users u)*
    :param username: the username to check the availability of
    :type username: str
    :return: <code>True</code> if the username is available, or <code>False</code> otherwise
    :rtype: bool
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            # Temporary code
            user = None
            return True if user is None else False


def get_user_with_credentials(username, password):
    """
    Finds the id of the user with a specific username and pin combination.
    *(Tables involved: users u)*
    :param username: the username of the user
    :type username: str
    :param pin: the pin of the user
    :type pin: str
    :return: the id of the user, if found
    :rtype: int or None
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT u.id
                              FROM User AS u
                              WHERE u.username = %s
                              AND u.password = %s""", [username, password])
            user = cursor.fetchone()
            if user is not None:
                return user['id']


def get_user_details(user_id):
    """
    NEEDS MORE WORK
    Gets details of a specific user.
    *(Tables involved: users u)*
    :param user_id: the id of the user to get details for
    :type user_id: int
    :return: a dictionary of the form
        <code>{'id': u.id, 'username': u.username, 'display_name': u.display_name, 'is_admin': u.is_admin}</code>
        representing a user
    :rtype: dict
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            # Temporary code
            user = {'id': user_id, 'username': 'somebody', 'display_name': 'Some Body', 'is_admin': True}
            return user