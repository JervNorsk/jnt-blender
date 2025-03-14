import logging

# -----------------------------------------------------------------------------

# # Configure the root logger
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# # Get the root logger
# logger = logging.getLogger(__package__.name)
#
# def show_enabled_loggers():
#     loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
#     enabled_loggers = [logger.name for logger in loggers]
#     print("Enabled loggers:", enabled_loggers)
#
# if __name__ == "__main__":
#     logger.warning("TEST")
#
#     show_enabled_loggers()