def derive_features(query_result):
    total_orders = len(query_result)
    popular_item = None
    max_orders = 0
    item_counts = {}
    for row in query_result:
        item = row[2]  
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1
        if item_counts[item] > max_orders:
            popular_item = item
            max_orders = item_counts[item]


    return total_orders,popular_item,max_orders
