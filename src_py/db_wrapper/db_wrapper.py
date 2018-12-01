import mysql.connector as mariadb
import argparse


def connect_to_db(user, password):
    return mariadb.connect(
        database="openerfurt",
        user=user,
        password=password,
        host="173.212.211.62",
        port="9006"
    )

def create_table(connection, spec_json):
    pass


def main(args):
    connection = connect_to_db(args.u, args.p)
    connection.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", metavar="user", type=str)
    parser.add_argument("-p", metavar="password", type=str)

    args = parser.parse_args()
    main(args)
