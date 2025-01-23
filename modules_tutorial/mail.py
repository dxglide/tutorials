def send(email, message):
    print(f'Sending "{message}" to {email}')

def _attach_file(filename):  # private function
    print(f'Attach {filename} to the message')


    # or ....
# __all__ = ['send']  # only send function is exported

# def send(email, message):
#     print(f'Sending "{message}" to {email}')

# def attach_file(filename):
#     print(f'Attach {filename} to the message')