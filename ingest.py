import json

import redis


def get_message_from_edge() -> dict:
    """
    Retuns data from super complex undocumented system. Consider it
    non mutable (you can rename it, move it, but don't change the contents).
    :return: json converted to dictionary
    """
    return json.load(open("example.json"))


def store_message_in_database(timestamp: str, message: str) -> bool:
    """
    Stores given CSV string in propriateary database. Consider it non mutable
    (you can rename it, move it, but don't change the contents).
    :param timestamp: Datetime in format: "2020-01-21T09:32:34" as string
    :param message: CSV represented as string
    :return: boolean result of the call
    """
    r = redis.Redis()
    r.set(timestamp, message)


if __name__ == "__main__":
    message = get_message_from_edge()
    values = message["Values"]
    csv_message = "%s,%s,%s,%s,%s,%s" % (
        values["FACTORY"],
        values["ZONE"],
        values["CELL"],
        values["MACHINE_GROUP"],
        values["MACHINE"],
        values["MACHINE_ID"],
    )
    store_message_in_database(values["TIMESTAMP"], csv_message)
