def set_api_client_auth_header(api_instance, token):
    set_api_client_auth_header(api_instance, token)


def set_api_client_request_header(api_instance, key, value):
    api_instance.api_client.set_default_header(api_instance, key, value)


def set_api_client_request_host(api_instance, url):
    # Set API host URI
    api_instance.api_client.configuration.host = url
