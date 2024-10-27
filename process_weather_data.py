def process_weather_data(records):
    """
    Aggregates weather data by city, handling missing values gracefully.
    
    Args:
        records: List of dictionaries containing city weather data
        
    Returns:
        Dictionary with city-wise aggregated weather metrics
    """
    # Initialize dictionary to store processed data
    processed_data = {}
    
    # Process each record
    for record in records:
        city = record.get('city')
        if not city:
            continue
            
        if city not in processed_data:
            processed_data[city] = {}
            
        # Process each weather metric in the record
        for key, value in record.items():
            if key != 'city' and value is not None:
                try:
                    value = float(value)
                    if key not in processed_data[city]:
                        processed_data[city][key] = {'sum': 0.0, 'count': 0}
                    processed_data[city][key]['sum'] += value
                    processed_data[city][key]['count'] += 1
                except (ValueError, TypeError):
                    continue
    
    # Calculate averages
    average = {}
    for city in processed_data:
        average[city] = {}
        for metric, data in processed_data[city].items():
            if data['count'] > 0:
                average[city][metric] = data['sum'] / data['count']
    
    return average