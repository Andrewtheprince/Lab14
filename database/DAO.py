from database.DB_connect import DBConnect

class DAO:

    @staticmethod
    def getStore():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        result = []
        query = """ SELECT 
                    FROM """
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result
    
