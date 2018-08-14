
import  os


if __name__ == '__main__':
    print(os.path.dirname(__file__))
    basedir = os.path.abspath(os.path.dirname(__file__))

    db_path = os.path.join(basedir, '../test.db')
    print(db_path)