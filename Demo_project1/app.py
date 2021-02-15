import sys #pass path at run time from Config
from config import DB_DETAILS


# def main():
#     for arg in sys.argv:
#         print(arg)   """To check the environment path at runtime """

def main():
    """By Defuat argv takes one arguments"""
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    print(db_details)

if __name__ == '__main__':
    main()