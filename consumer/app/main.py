from mysql_connection import *


def insert_in_mysql(doc):
    if doc["type"] == "customer":
        cursor.execute(
            """
            INSERT IGNORE INTO customer
            (type,customerNumber,customerName,contactLastName,contactFirstName,phone,addressLine1,addressLine2,city,
            state,postalCode,country,salesRepEmployeeNumber,creditLimit)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                doc.get("type"),
                doc.get("customerNumber"),
                doc.get("customerName"),
                doc.get("contactLastName"),
                doc.get("contactFirstName"),
                doc.get("phone"),
                doc.get("addressLine1"),
                doc.get("addressLine2"),
                doc.get("city"),
                doc.get("state"),
                doc.get("postalCode"),
                doc.get("country"),
                doc.get("salesRepEmployeeNumber"),
                doc.get("creditLimit"),
            )
        )

    else:
         cursor.execute(
            """
            INSERT IGNORE INTO order
            (type,orderNumber,orderDate,requiredDate,shippedDate,status,comments,customerNumber)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                doc.get("type"),
                doc.get("orderNumber"),
                doc.get("orderDate"),
                doc.get("requiredDate"),
                doc.get("shippedDate"),
                doc.get("status"),
                doc.get("comments"),
                doc.get("customerNumber"),
                
            )
        )
    mysql_conn.commit()
