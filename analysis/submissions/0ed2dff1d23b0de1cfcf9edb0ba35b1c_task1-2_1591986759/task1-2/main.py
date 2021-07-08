# Example code, write your program here
import datetime


def main():
    time = datetime.datetime.utcnow() + datetime.timedelta(days=7)
    print(time.strftime('%m-%d-%Y %H:%M'))


if __name__ == '__main__':
    main()
