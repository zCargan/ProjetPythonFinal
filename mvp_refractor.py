import csv


class MVP:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def complete_password(self):
        """
        complete the dictionary with all the user's information
        :param: any
        :return: dic completed with the information from the csv file
        """
        try:
            dic = {}
            with open('data.csv') as file:
                file_password = csv.reader(file, delimiter=";")
                for line in file_password:
                    key = line[0]
                    if key not in dic:
                        dic[key] = []
                    for i in range(1, len(line)):
                        dic[key].append(line[i])
            return dic
        except FileNotFoundError:
            print("File not found")

        except IOError:
            print("Error IO.")

    @property
    def identification_user(self):
        """
        if the user is known and the password is correct, the user is identified with all his privileges.

        the index (for the dictionary):
        [0] : password
        [1] : X if the user is an admin

        :return:
            return a string with these informations: if the user is known, the password ok and
            if the user is a admin or not
        """
        if self.username in self.complete_password:
            dic = self.complete_password
            if dic[self.username][0] == self.password:
                if dic[self.username][1] == "X":

# -------------------------------------------- User exist, password OK and admin ----------------------------------------
                    return "Successful authentication, u are admin!\nMusic : Allowed \nSoftware : Allowed " \
                           "\nweather_report : Allowed ""\naccess_management : Allowed"
                else:

# ------------------------------------------ User exist, password OK and not admin -------------------------------------
                    return "Successful authentication, u are a guest\nMusic: Allowed \nSoftware : Allowed " \
                                 "\nweather_report : Allowed ""\naccess_management : Denied"

#--------------------------------------- User exist, password not OK and not admin -------------------------------------
            return "incorrect password"

# ---------------------------------------------------- User doesnt exist -----------------------------------------------
        else:
            return "User not found"


if __name__ == "__main__":

    user_connected = MVP("3", "2")
    response = user_connected.identification_user
    print(response)