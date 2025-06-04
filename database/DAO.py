from database.DB_connect import DBConnect
from model.order import Order
from model.store import Store

class DAO:

    @staticmethod
    def getStore():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        result = []
        query = """ SELECT *
                    FROM stores s"""
        cursor.execute(query)
        for row in cursor:
            result.append(Store(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getOrdini(store):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """ SELECT *
                    FROM orders o
                    WHERE o.store_id = %s"""
        cursor.execute(query, (store,))
        for row in cursor:
            result.append(Order(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(giorniMAx, store, idMap):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """ select o1.order_id as ordine1, o2.order_id as ordine2, (o1.peso + o2.peso) as pesotot
                    from (select o1.order_id, o1.order_date, sum(oi.quantity) as peso
	                        from orders o1, order_items oi 
	                        where o1.order_id = oi.order_id and o1.store_id = %s
	                        group by o1.order_id)	o1, (select o1.order_id, o1.order_date, sum(oi.quantity) as peso
								                         from orders o1, order_items oi 
								                         where o1.order_id = oi.order_id and o1.store_id = %s
								                         group by o1.order_id) o2
                    where  o1.order_id < o2.order_id and ABS(DATEDIFF(o1.order_date, o2.order_date)) <= %s
                    group by o1.order_id, o2.order_id"""
        cursor.execute(query, (store, store, giorniMAx,))
        for row in cursor:
            if row["ordine1"] in idMap and row["ordine2"] in idMap:
                result.append(row)
        cursor.close()
        conn.close()
        return result
