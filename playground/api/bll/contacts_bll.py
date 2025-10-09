from dal.abstract_contacts import ContactsABC
from dal.dal_factory import ContactsFactory
from domain.contact import Contact
from util.logger import enable_logger

class ContactBll:
    def __init__(self, source):
        self.__contact_dao:ContactsABC = ContactsFactory().create_instance(source)

    @enable_logger
    def retrieve_contacts(self):
        result:list[Contact] = []
        for record in self.__contact_dao.retrieve_contacts().get("contacts",[]):
            result.append(Contact(name=record["name"], contact_number=record["contact_number"]))
            raise Exception("Error in business layer")
        return result

    @enable_logger
    def search_contact(self, keyword):
        return self.__contact_dao.search_contact(keyword)
