from pyscript import document, display

# This code defines a Classmates class with attributes for name, section, and favorite subject. It also includes a method to introduce the classmate. The classmates_list is initialized with some sample classmates. The display_classmates function updates the HTML to show the list of classmates, and the add_classmate function allows users to add new classmates through input fields in the HTML.
class Classmates:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

# The introduce method returns a string introducing the classmate with their name, section, and favorite subject.
    def introduce(self):
        return f"Hi, I'm {self.name} from Grade 10- {self.section}. My favorite subject is {self.favorite_subject}."

# The classmates_list is a list of Classmates.
classmates_list = [
    Classmates("Jairo", "Emerald", "PE"),
    Classmates("Lucas", "Emerald", "Science"),
    Classmates("Shia", "Emerald", "Social Studies"),
    Classmates("Joel", "Emerald", "English"),
    Classmates("Gio", "Emerald", "Math"),
    Classmates("Gavin", "Emerald", "Music"),
]

# The display_classmates function updates the HTML element with id "classmates_output" to show the list of classmates.
def display_classmates(e=None):
    output = document.getElementById("classmates_output")
    output.innerHTML = ""
# The for loop iterates through the classmates_list and appends each classmate's introduction to the output element in the HTML.
    for i, c in enumerate(classmates_list, start=1):
        output.innerHTML += f"<p><b>{i}.</b> {c.introduce()}</p>"

# The add_classmate function retrieves the values from the input fields for name, section, and favorite subject. If any of the fields are empty, it returns without adding a new classmate. Otherwise, it creates a new Classmates object and appends it to the classmates_list. It then clears the input fields and calls display_classmates to update the list of classmates shown in the HTML.
def add_classmate(e):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("favorite_subject").value
# If any of the input fields are empty, the function returns without adding a new classmate.
    if name == "" or section == "" or subject == "":
        return
# A new Classmates object is created with the input values and added to the classmates_list.
    new_classmate = Classmates(name, section, subject)
    classmates_list.append(new_classmate)
# The input fields are cleared after adding the new classmate.
    document.getElementById("name").value = ""
    document.getElementById("section").value = ""
    document.getElementById("favorite_subject").value = ""
# The display_classmates function is called to update the list of classmates shown in the HTML after adding a new classmate.
    display_classmates()

#I used AI to fix the formatting of the code, to add comments for better understanding and to fix any issues.