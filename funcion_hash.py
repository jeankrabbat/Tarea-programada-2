def funcion_hash(date, quarter, team_name):
    data_str = f"{date}--{quarter}--{team_name}"
    hash_value = sum(ord(char) for char in data_str)
    hash_value = (hash_value * 31) % 750 
    return hash_value