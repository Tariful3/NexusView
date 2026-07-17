import urllib.request
from IPython import displayfrom
from NexusView.custom_exception import InvalidURLException
from NexusView.logger import logger

def is_valid(url: str)-> bool:
  try:
    response_status = urllib.request.urlopen(url).getcode()
    assert response_status == 200
    return True
  except Exception as e:
    return False


def render_site(URL: str, width: str = "100%", height: str = "600")-> str:
  try:
    if is_valid(URL):
      response = display.IFrame(src=URL, width=width, height=height)
      display.display(response)
      return "success"
    else:
      raise "error"
  except Exception as e:
    raise
