from fastapi import APIRouter
from bll.contacts_bll import ContactBll
from domain.contact import Contact

router = APIRouter(tags=["Contacts API"], prefix="/api/v1")
contact_bll = ContactBll("json")

@router.get("/contacts")
def display_contacts()->list[Contact]:
    return contact_bll.retrieve_contacts().get("contacts",[])

@router.get("/contacts/search/{keyword}")
def search_contact(keyword:str)->list[Contact]:
    return contact_bll.search_contact(keyword).get("contacts",[])