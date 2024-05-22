class FoodDeliverySystem:
    order_id = 0
    orders_log = {"order_id": {"customer_name":"ABC", "order_items":{"item1":10}, "status" : "Placed"}}
    def __init__(self):
        self.menu = {
            "Burger": 150,
            "Pizza": 250,
            "Pasta": 200,
            "Salad": 120,
            "Beverages": 130,
            "Noodles": 150,
            "Sushi": 270,
            "Bakery":350
            # Add more items to the menu
        }
        self.bill_amount = 0
        
    def display_menu(self):

        """
        Return the menu details in the following format:
        {
            "Burger" :  150
            "Pizza"  :  250
            "Pasta"  :  200
            "Salad"  :  120
            "Beverages" :  130
            "Noodles" :  150
            "Sushi"  :  270
            "Bakery" :  350
        }
        """
        return self.menu
        
    def place_order(self, customer_name, order_items):
        """
        Return orders log after order placed by a customer with status as "Placed", otherwise return "order placement failed"
        Format:
        orders_log = {order_id: {"customer_name":"ABC", "order_items":{"item1":"Quantity"}, status : "Placed}}
        """
        if self.orders_log['order_id']['status'] == "Placed":
            return self.orders_log
        else:
            "order placement failed"
        
    def pickup_order(self, order_id):
        """
        status: Picked Up	
        Return the changed status of the order: {order_id: {"customer_name":ABC, "order_items":{"item1":"Quantity"}, status = "Picked Up"}}
        """
        return order_id['status']
        
    def deliver_order(self, order_id):
        """
        status: Delivered
        Return the delivery status of order (delivered or not delivered)
        """
        if  (order_id['status'].lower() in ('delivered','not delivered')):
            return order_id['status']
        
    def modify_order(self, order_id, new_items):
        """
        Return the modified order with items available in menu only if the order is not picked up:
        {order_id: {"customer_name":ABC, "order_items":{"item1":"Quantity", new_items}, status = "Placed"}}
        """
        if order_id['status'] != "Picked Up":
            return order_id['order_items']
    
    def generate_bill(self, order_id):
        """
        if the sum of all items > 1000
        Amount = Sum of all items placed + 10% of total sum
        if sum of all items < 1000
        Amount = Sum of all items placed + 5% of total sum
        Return the total bill amount
        """
        amount = 0
        sum_order = sum(order_id['order_items'].values())
        
        if (sum_order > 1000):
            amount = sum_order + (sum_order * (10 / 100))
        else:
            amount = sum_order + (sum_order * (5 / 100))
        
        return amount
        
    def cancel_order(self, order_id):
        """
        Cancel order items for the customer if the order is not Picked Up and remove order details from orders log
        Return the order logs. For example, if you have 3 orders, but the third order is cancelled, you need remove this from the orders log and just return the first two orders:
        {1: {"customer_name":"clientA", "order_items":{"Burger":1,"Pasta":2},"status":"Delivered"}, 2: {"customer_name":"clientB", "order_items":{"Salad":2,"Sushi":4, "Beverages":6, "Bakery":2},"status":"Placed"}}
        """
        new_orders_log = {}
        for order_id, order_items in self.orders_log.items():
            if order_items["status"] != "Picked Up":
                new_orders_log[order_id] = order_items

        #self.orders_log = new_orders_log;
        return new_orders_log

food = FoodDeliverySystem()
food.display_menu()
food.place_order('Gian',{"item1":1})
food.pickup_order({"customer_name":"ABC", "order_items":{"item1":1}, "status" : "Picked Up"})
food.deliver_order({"customer_name":"ABC", "order_items":{"item1":1}, "status" : "Delivered"})
food.modify_order({"customer_name":"ABC", "order_items":{"item1":1}, "status" : "Picked Up"},{"item1":1})
food.generate_bill({"customer_name":"ABC", "order_items":{"item1":1000,"item2":1000}, "status" : "Picked Up"})
food.cancel_order({"customer_name":"ABC", "order_items":{"item1":1}, "status" : "Picked Up"})
