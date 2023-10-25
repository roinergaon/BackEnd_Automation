from config import LOG


def build_request_headers(access_token, content_type="application/json", **kwargs):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": content_type
    }
    if "content_type" in kwargs:
        headers["content_type"] = kwargs["content_type"]

        LOG.debug(f"Request headers: {headers}")

    return headers
