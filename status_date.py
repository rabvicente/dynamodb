import user_ops as user
import order_ops as order_ops   
from decimal import Decimal

if __name__ == '__main__':
    
    #print(user.query_user_profile("tgrimes1"))
    
    orders = order_ops.query_order_status_date("tgrimes1", "PLACED", "11/18/21")

    for order in orders:
        order_id = order['order_id'][7:] # Remove order prefix
        items = order_ops.query_order_items(order_id)
        print(items)
        for item in items:
            print(item['product_name'])