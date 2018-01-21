def addCrossDomainHeader(response):
    response["Access-Control-Allow-Origin"] = "*"
    # response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


def buildReturnMessage(res, message=False):
    response = {
        'success': res,
        'message': message
    }
    return response

def buildReturnErrorMessage(code=None, error=None):
    return buildReturnMessage(False, {'code': code, 'error': error})