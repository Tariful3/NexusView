import urllib.request

from IPython import display

from NexusView.custom_exception import InvalidURLException
from NexusView.logger import logger


def is_valid(url: str) -> bool:
    try:
        response = urllib.request.urlopen(url)
        return response.getcode() == 200
    except Exception:
        return False


def render_site(
    url: str,
    width: str = "100%",
    height: str = "600",
) -> str:
    try:
        if not is_valid(url):
            raise InvalidURLException("Invalid URL")

        response = display.IFrame(
            src=url,
            width=width,
            height=height,
        )
        display.display(response)

        logger.info(
            "Successfully rendered website: %s",
            url,
        )

        return "success"

    except Exception:
        raise
