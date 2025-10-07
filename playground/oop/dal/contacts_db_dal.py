from dal.db_dal import DbDaoABC
from dal.abstract_contacts import ContactsABC

class ContactsDbDao(DbDaoABC, ContactsABC):

    def retrieve_contacts(self):
        sql = "select name, contact_number from contacts"
        result = {
            "contacts": []
        }
            
        for row in self.execute_select(sql):
            result.get("contacts").append({
                "name" : row[0],
                "contact_number" : row[1]
            })
            
        return result

    def search_contact(self, keyword):
        raise Exception("Not Implemented")
        

        
        