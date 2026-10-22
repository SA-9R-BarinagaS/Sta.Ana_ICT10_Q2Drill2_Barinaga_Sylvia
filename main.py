
from pyscript import document

# Members already registered
grade_7 = {"Harry Potter", "Hermione Granger", "Ron Weasley"}
grade_8 = {"Percy Jackson", "Annabeth Chase", "Grover Underwood"}
grade_9 = {"Katniss Everdeen", "Peeta Mellark", "Haymitch Abernathy"}
grade_10 = {"Nico di Angelo", "Leo Valdez", "Piper McLean"}

new_members = set()


def show_all_members():
    # Combine the grade-level sets and the newly added members
    all_members = grade_7 | grade_8 | grade_9 | grade_10 | new_members

    # Put each member on a separate line in alphabetical order
    member_list = "<br>".join(
        map(lambda name: "✿ " + name, sorted(all_members))
    )

    # Show the complete list and the number of unique members
    document.getElementById("output").innerHTML = f"""
        <div class="member-heading">All members:</div>
        <div class="member-list">{member_list}</div>
        <div class="member-total">Total members: {len(all_members)}</div>
    """


def result_checker(event):
    # Get the first and last name
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    # Join the first and last names to make the full name
    full_name = first_name + " " + last_name

    # Save the new member in the set
    new_members.add(full_name)

    # Update the list so the new member appears on the page
    show_all_members()

    # Clear the boxes to make room for the next entry
    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""


# Display the original members as soon as the page loads
show_all_members()
