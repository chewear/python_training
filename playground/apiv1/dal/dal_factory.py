from dal.contacts_dal import ContactsJsonDao
from dal.contacts_db_dal import ContactsDbDao
from dal.abstract_contacts import ContactsABC

class ContactsFactory:
    def create_instance(self, source) -> ContactsABC:
        obj_map =  {
            "db" : ContactsDbDao,
            "json" : ContactsJsonDao,
            "api" : ContactsJsonDao
        }
        
        obj = obj_map.get(source, None)

        if obj ==  None : raise Exception("Invalid Source")
        else : return obj()