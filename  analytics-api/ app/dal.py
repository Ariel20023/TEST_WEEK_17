def analytics_top_customers_function():
    return """select c.customerName , o.count(*) as cnt
                from customer as c
                left join order as o 
                on c.customerNumber = o.customerNumber
                group by c.customerName
                order by DESC
                LIMIT 10
                """ 

def analytics_customers_without_orders_function():
    return """select c.customerName , o.count(*) as cnt
                from customer as c
                left join order as o 
                on c.customerNumber = o.customerNumber
                group by c.customerName
                having o.count(*) = 0
                """ 

def analytics_zero_credit_active_customers_function():
    return """select c.customerName , o.count(*) as cnt
                from customer as c
                left join order as o 
                on c.customerNumber = o.customerNumber
                where creditLimit = "0"
                group by c.customerName
                having o.count(*) > 0
                """