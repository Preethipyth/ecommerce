import logging

# Set up logging
logging.basicConfig(filename='example.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def derive_features(query_result):
    try:
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
        
        logging.info("Derived features calculation completed")
        return total_orders, popular_item, max_orders
    
    except Exception as e:
        logging.error(f"Error occurred during feature derivation: {e}")
        return None, None, None  # Return None values in case of error
