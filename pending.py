import user_ops as user
import order_ops as order_ops   
from decimal import Decimal

if __name__ == '__main__':
    orders = order_ops.query_order_status('Pending')
    for order in orders:
        order_list = print(order['sk'], order['product_name'], order['quantity'])
