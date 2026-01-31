import logging

logging.basicConfig(
    # level=logging.INFO,
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger=logging.getLogger(__name__)

