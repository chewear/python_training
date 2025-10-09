from fastapi import APIRouter
from util.logger import enable_logger, Logger
from bll.contacts_bll import ContactBll
from domain.contact import Contact
from domain.service_response import ServiceResponse

router = APIRouter(tags=["Contacts API"], prefix="/api/v1")
contact_bll = ContactBll("json")

@router.get("/contacts")
@enable_logger
def display_contacts()-> ServiceResponse[list[Contact]]:
    response = ServiceResponse()
    try:
        response.data = contact_bll.retrieve_contacts()
    except Exception as ex:
        # Logger().get_logger().error(ex, exc_info=True)
        response.status_code = 500
        response.status_message = str(ex)
    return response

@router.get("/contacts/search/{keyword}")
@enable_logger
def search_contact(keyword:str)->list[Contact]:
    return contact_bll.search_contact(keyword).get("contacts",[])