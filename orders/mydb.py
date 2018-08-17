class MyDB:
    """docstring for MyDB"""
    def __init__(self):
        self.connect = Connection()

    def conn(self):
        print('open db connect...')
        return self.connect

class Connection :

    def __init__(self   ):
        self.cursor = Cursor()
    def cur(self):
        return self.cursor

    def close(self):
        print('close db connect  ....')

class Cursor(object):
    """docstring for Cursor"""
    def execute(self, query):
        if query == 'query1':

            return 1
        elif  query == 'query2':

            return 2
        elif  query == 'query3':

            return 3
        else:
            return -1

    def close(self):
        print('cursor close ....')


