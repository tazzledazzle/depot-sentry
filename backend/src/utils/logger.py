import logging
import logging.handlers
import os

# Create a custom logger
logger = logging.getLogger(__name__)

# Set the default logging level
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.handlers.TimedRotatingFileHandler(
    filename=os.path.join("logs", "app.log"), when="midnight", interval=1, backupCount=7
)
file_handler.suffix = "%Y-%m-%d"

# Set logging levels for handlers
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.INFO)

# Create formatters and add them to the handlers
console_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Example usage
if __name__ == "__main__":
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
