from NexusView.logger import logger
from NexusView.cutom_exception import InvalidURLException
try:
       raise InvalidURLException()

except Exception as e:
       logger.error(f"An error Occurred: {e}")