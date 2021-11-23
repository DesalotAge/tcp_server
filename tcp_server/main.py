"""Main project interaction module."""
import socket
from tcp_server.utils import (
    correct_format,
    write_data_to_file
)
from loguru import logger


HOST = "0.0.0.0"
PORT = 8080
BUFFER_SIZE = 1024
# remove log messages from the console
logger.remove()
# settings for logger
logger.add('tcp_server/logs/info.log', format="{time} {level} {message}", level="INFO")


@logger.catch
def main():
    """Start project."""
    # create a server
    server = socket.create_server((HOST, PORT))
    while 1:
        # Waiting for connection
        connect, client_socket = server.accept()

        logger.info(f"Connected to {client_socket}")

        while 1:
            # trying to receive data
            try:
                data = connect.recv(BUFFER_SIZE).decode()

                logger.info(f"Received data: '{data}'")

                formated_data, group_id = correct_format(data)
                logger.info(f"Data was formated to: '{formated_data}'")

                logger.info(f"Writing '{formated_data}' to our data files.")
                write_data_to_file(formated_data, group_id)
            except UnicodeDecodeError:
                # breaking a connection if given data is wrong encoded
                logger.error("During decoding received data an error occured")
                break
            except ValueError:
                # data must be right formated, this exception looking for format errors
                logger.error("During formating data an error occured")
                break


if __name__ == "__main__":
    main()
