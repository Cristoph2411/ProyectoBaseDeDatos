import datetime
from database.conexion import conex

class Utils():
    
    @classmethod
    def strtime(self , date):
        return datetime.datetime.strftime( date , '%Y-%m-%d %H:%M:%S')

    @classmethod
    def auto_increment(self):
        try:
            conexion = conex()
            dateAll = []
            id = 0
            with conexion.cursor() as cursor:
                cursor.execute("SELECT id FROM orders")
                date = cursor.fetchall()
                for row in date:
                    dateAll += row
                conexion.close()
            if dateAll == []:
                id  = 1
            if dateAll != []:
                for i in dateAll:
                    id = i + 1
            return id
        except Exception as error:
            return 100
            