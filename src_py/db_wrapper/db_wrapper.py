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


def main(args):
    connection = connect_to_db(args.user, args.password)

    connection.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("user", metavar="user", type=str)
    parser.add_argument("password", metavar="password", type=str)

    args = parser.parse_args()
    main(args)
