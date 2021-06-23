# Basically a class defines the attributes that a given object has or is supposed to have. This allows for
# many 'instances' of the 'class' to be created without redefining the attributes each time. Its like
# cloning from a blueprint. Thats the lesson here. The clones are objects

class User:
    # constructor that will 'construct the new object using the parameters that we provide'
    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}")