def get_all_order_history_by_date(self):
        orders = []
        for smybol in self.order_history.keys():
            smybol_orders = self.order_history[smybol]
            smybol_orders = [[smybol] +one for one in smybol_orders]
            orders.extend(smybol_orders)
        orders = sorted(orders, key =lambda x : x[1])
        print(orders[:3])
        print(orders[-3:])
        return orders 