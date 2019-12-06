import pkg_resources
import logging
import sys

pkg_resources.declare_namespace(__name__)
logger = logging.getLogger(__name__)

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
