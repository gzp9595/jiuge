# coding: utf-8
import logging
import redis
import requests
import os


# logging.basicConfig(level=logging.WARNING, filemode="w")


def generate_logger(logger_name):
    """
    # debug/error    
    """
    my_logger = logging.getLogger(logger_name)
    file_name = os.path.join("../", logger_name+".log")
    fh = logging.FileHandler(file_name, "a", encoding="utf-8")
    formatter = logging.Formatter("%(levelname)s - %(asctime)s - %(message)s")
    fh.setFormatter(formatter)
    my_logger.addHandler(fh)
    return my_logger


def generate_output_logger(logger_name):
    my_logger = logging.getLogger(logger_name)
    file_name = os.path.join("../", logger_name+".md")
    fh = logging.FileHandler(file_name, "a", encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    fh.setFormatter(formatter)
    my_logger.addHandler(fh)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    my_logger.addHandler(ch)
    return my_logger
