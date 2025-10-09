from util.file_util import read_json_as_dict
from dal.abstract_contacts import ContactsABC

class ContactsJsonDao(ContactsABC):
    def retrieve_contacts(self):
        return read_json_as_dict("contacts.json")

    def search_contact(self, keyword):
        result = {
            "contacts":[]
        }

        for record in self.retrieve_contacts().get("contacts",[]):
            if record.get("name").find(keyword) >= 0:
                result.get("contacts").append(record)
        
        return result
    