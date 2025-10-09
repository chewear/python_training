from dal.abstract_contacts import ContactsABC
from dal.dal_factory import ContactsFactory

class ContactBll:
    def __init__(self, source):
        self.__contact_dao:ContactsABC = ContactsFactory().create_instance(source)

    def retrieve_contacts(self):
        return self.__contact_dao.retrieve_contacts()

    def search_contact(self, keyword):
        return self.__contact_dao.search_contact(keyword)
