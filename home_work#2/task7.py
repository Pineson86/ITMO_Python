items_dict = {
    "laptop": (3, 1500),
    "camera": (1, 800),
    "phone": (1, 600),
    "watch": (0.5, 300),
    "headphones": (0.2, 200),
    "tablet": (2, 900),
    "wallet": (0.1, 100)}

max_weight = 25

#Ranging items by cost of 1 kilo
ranged_items = {}
for key, value in items_dict.items():
    ranged_items[key] =int( value[1] / value[0])
ranged_items = dict(sorted(ranged_items.items(), key=lambda item: item[1], reverse=True))
print(ranged_items)

#What items and how many of them will we put in the bag
bag_items = {}
for key, value in ranged_items.items():
    item_amount = max_weight % value
    bag_items[key] = item_amount
    remained_weight = max_weight - (value * item_amount)
    if remained_weight == 0:
        break
    else:
        max_weight = remained_weight
        continue
print(bag_items)