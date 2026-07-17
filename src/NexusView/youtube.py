import re

from IPython.display import HTML, display

from NexusView import logger
from NexusView.custom_exception import InvalidURLException


def render_youtube_video(
    url: str,
    width: int = 780,
    height: int = 440,
):
    try:
        regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
        match = re.search(regex, url)

        if not match:
            raise InvalidURLException("Invalid YouTube URL")

        video_id = match.group(1)
        embed_url = (
            f"https://www.youtube-nocookie.com/embed/{video_id}"
        )

        iframe = f"""
        <iframe
            width="{width}"
            height="{height}"
            src="{embed_url}"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write;
                   encrypted-media; gyroscope;
                   picture-in-picture; web-share"
            referrerpolicy="strict-origin-when-cross-origin"
            allowfullscreen>
        </iframe>
        """

        display(HTML(iframe))

        logger.info(
            " Successfully rendered YouTube video for URL: %s",
            url,
        )

        return "success"

    except Exception:
        raise
