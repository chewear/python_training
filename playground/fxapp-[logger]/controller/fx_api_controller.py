from fastapi import APIRouter
from bll.rates_bll import RatesBll
from domain.conversion import Conversion
from domain.rates import Rates
from domain.service_response import ServiceResponse
from util.logger import enable_logger

router = APIRouter(tags=["FX API"], prefix="/api/v1")
fx_bll = RatesBll("json")

@router.get("/rates")
@enable_logger
def retrieve_rates(base:str) -> ServiceResponse[Rates]:
    response = ServiceResponse()
    try:
        response.status_message = "Rates retrieved successfully."
        response.data = fx_bll.get_rates_data(base)
    except ValueError as ve:
        response.status_code = 400
        response.status_message = str(ve)
    except Exception as ex:
        response.status_code = 500
        response.status_message = str(ex)
    return response

@router.get("/convert")
@enable_logger
def convert(source:str, target:str, amount_to_be_converted:float) -> ServiceResponse[Conversion]:
        response = ServiceResponse()
        try:
            response.status_message = "Conversion successful."
            response.data = fx_bll.convert_amount(source, target, amount_to_be_converted)
        except ValueError as ve:
            response.status_code = 400
            response.status_message = str(ve)
        except Exception as ex:
            response.status_code = 500
            response.status_message = str(ex)
        return response