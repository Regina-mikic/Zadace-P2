import re

email = input("Unesi e-mail (ime.prezime@fpmoz.sum.ba): ")
eduid = input("Unesi eduID (iprezimeX@sum.ba): ")

regex_email = r"^[a-zčćžšđ]+[.][a-zčćžšđ]+@fpmoz\.sum\.ba$"

regex_eduid = r"^[a-zčćžšđ][a-zčćžšđ]+[0-9]*@sum\.ba$"

if re.search(regex_email, email, re.IGNORECASE):
    print("E-mail je ispravan.")
else:
    print("E-mail NIJE ispravan.")

if re.search(regex_eduid, eduid, re.IGNORECASE):
    print("EduID je ispravan.")
else:
    print("EduID NIJE ispravan.")
