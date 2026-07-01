"""Command-line entry point for LatchBioAgent."""

import logging
import os

from latchbioagent.server import main as server_main

logger = logging.getLogger("LatchBioAgent")


def main() -> None:
    log_level = os.getenv("LATCHBIO_LOG_LEVEL", "INFO")
    logging.basicConfig(level=getattr(logging, log_level.upper(), logging.INFO))
    logger.info("Starting LatchBioAgent")
    server_main(log_level=log_level)


if __name__ == "__main__":
    main()
