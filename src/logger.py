import logging

## Basic function to init logger. You can modify it especially if you want to add other handlers
def init_logger(logger_name, stream=True, file=True, level="DEBUG", file_path=None):
    """Returns logger initialized with the specified parameters.

    Args:
        logger_name (str): Name of the logger
        stream (bool, optional): Logger will write logs in the console if set to True. Defaults to True.
        file (bool, optional): Logger will write logs in a file if set to True. Defaults to False.
        level (str, optional): Log level (see logging documentation for details). Defaults to "INFO".
        file_path (str, optional): Path of the log file to where to write logs. Must be specified if file is True. Defaults to None.

    Raises:
        ValueError: Raise value if no handler is provided that is you must at least set stream or file to True

    Returns:
        logger: Logger object set with the specified parameters
    """
    # building handlers
    handlers = []
    if file:
        # more parameters on logging.Formatter here: https://docs.python.org/3/library/logging.html#logrecord-attributes
        file_formatter = logging.Formatter(
            "%(asctime)s.%(msecs)03d %(levelname)s %(funcName)s: %(message)s"
        )
        file_handler = logging.FileHandler(file_path)
        file_handler.setFormatter(file_formatter)
        handlers.append(file_handler)
    if stream:
        stream_formatter = logging.Formatter(
            "%(asctime)s.%(msecs)03d %(levelname)s %(funcName)s: %(message)s"
        )
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(stream_formatter)
        handlers.append(stream_handler)
    if len(handlers) == 0:
        raise ValueError(
            "You provide no handler, you must at least set stream or file to True"
        )
    # initilizing logger
    logger = logging.getLogger(logger_name)
    # adding handlers to logger
    for handler in handlers:
        logger.addHandler(handler)  
    # setting level of logger
    logger.setLevel(level)

    return logger