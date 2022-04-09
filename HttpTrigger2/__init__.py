import logging
import requests

import azure.functions as func
from .logica import random_cor
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if req.method =='GET':
        instancia_classe=random_cor()
        data=instancia_classe
        return func.HttpResponse(f'{data}')
    
