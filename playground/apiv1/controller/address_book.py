from bll.contacts_bll import ContactBll

class Contacts: 
    def __init__(self, source="json"):
        self.contact_bll = ContactBll(source)

    def display_contacts(self):
        self.__do_display_result(self.contact_bll.retrieve_contacts().get("contacts",[]))

    def search_contact(self, keyword):
        self.__do_display_result(self.contact_bll.search_contact(keyword).get("contacts",[]))

    def __do_display_result(self,records):
        for record in records:
            print(f"Name: {record.get('name','')} \nContact #: {record.get('contact_number')}")