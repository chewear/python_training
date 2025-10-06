from bll.contacts_bll import retrieve_contacts

def display_contacts(source):
    for record in retrieve_contacts(source).get("contacts",[]):
        print(f"{record.get("name",'')} \t\t {record.get("contact_number")}")

display_contacts()