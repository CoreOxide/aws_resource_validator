import time
from requests.models import Response


def check_rate_limit(response: Response) -> None:
    """
    Checks the rate limit from the response headers. If the rate limit is exceeded,
    the function will pause execution until the rate limit is reset.

    :param response: The response object to check the rate limit from.
    """
    if 'X-RateLimit-Remaining' in response.headers and int(response.headers['X-RateLimit-Remaining']) == 0:
        reset_time: int = int(response.headers['X-RateLimit-Reset'])
        sleep_time: float = reset_time - time.time() + 10  # Adding 10 seconds to ensure limit is reset
        # TODO: use logging instead of print
        print(f"Rate limit exceeded. Sleeping for {sleep_time} seconds.")
        time.sleep(sleep_time)
