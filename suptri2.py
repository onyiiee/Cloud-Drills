from twilio.rest import Client

# Twilio account credentials
account_sid = 'your sid'
auth_token = 'your auth token'
twilio_number = '+123456789'

# List of suppliers and their product inventory
suppliers = {
    'Supplier A': {
        'product_name': 'Product 1',
        'inventory_level': 10
    },
    'Supplier B': {
        'product_name': 'Product 2',
        'inventory_level': 5
    }
}

# Loop through suppliers and check inventory levels
for supplier, product_data in suppliers.items():
    product_name = product_data['product_name']
    inventory_level = product_data['inventory_level']
    
    # Check if inventory level is below a certain threshold
    if inventory_level <= 5:
        # Send SMS notification to supplier
        client = Client(account_sid, auth_token)
        message = 'Hello, {}. Your product {} is running low on inventory. Please restock as soon as possible.'.format(supplier, product_name)
        client.messages.create(to='+123456789', from_=twilio_number, body=message)
