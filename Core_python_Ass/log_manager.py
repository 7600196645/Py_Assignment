import logging

logging.basicConfig(filename = "transaction.log",level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

def log_transaction(message):
    """log all transaction"""
    logging.info(message)
