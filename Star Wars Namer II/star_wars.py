import logging
import azure.functions as func
from swnamer import NameGenerator

def main(request: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python SWNAMER function started...')

    return_name = None
    sw_generator = NameGenerator(lowercase=False, separator=' ', use_characters=False)

    user_name = request.params.get('web_user_name')
    if not user_name:
        try:
            req_body = request.get_json()
        except ValueError:
            return_name = sw_generator.generate()
            pass
        else:
            user_name = req_body.get('web_user_name')
            return_name = sw_generator.generate()

    if user_name:
        return_name = user_name + ' ' + sw_generator.generate()
        return func.HttpResponse(return_name, status_code=200)
    else:
        return func.HttpResponse(
             'Your Star Wars name is ' + return_name + ' was returned, but if you supply \
                  a name, your SW name can be more personalized.',
             status_code=200
        )
