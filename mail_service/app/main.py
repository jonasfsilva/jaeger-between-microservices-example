from amqp import open_conn
from amqp import start_consumers
from consumers import default_callback


def run_consumers():
    connection = open_conn()
    queue = 'send_email'
    start_consumers(connection, default_callback, queue)


def main():
    run_consumers()


if __name__ == "__main__":
    main()