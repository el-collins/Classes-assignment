from User import User


class Admin(User):
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges()

    def show_privileges(self):
        self.privileges.show_privileges()


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(privilege)



# Exercise 9-7
admin = Admin("Admin", "User", "admin", "admin@example.com")
admin.show_privileges()

# Exercise 9-8
admin2 = Admin("Best", "Admin", "bestadmin", "bestadmin@example.com")
admin2.show_privileges()