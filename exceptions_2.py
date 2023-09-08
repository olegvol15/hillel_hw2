def dict_handler(link_on_dict: dict, key, default_value):
    try:
        result = link_on_dict[key]
    except KeyError:
        link_on_dict[key] = default_value
        result = default_value
    except TypeError as e:
        raise Exception(f"TypeError: {e} - Ключ не може бути використаний у словнику")
    finally:
        return result

my_dict = {'name': 'Oleg', 'age': 17}
key = 'name'
default_value = 'Unknown'
result = dict_handler(my_dict, key, default_value)
print(f"Значення за ключем '{key}': {result}")
