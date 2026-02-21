


if __name__ == "__main__":
    print("===Player Inventory System === \n\n")
    alice = dict()
    alice.update({"sword" : {"obj" : "weapon", "rarity" : "rare", "quantity" : 1, "price" : 500},
                  "potion" : {"obj" : "consumable", "rarity": "common", "quantity" : 5, "price" : 50},
                  "shield" : {"obj" : "armor", "rarity" : "uncommon", "quantity" : 1, "price" : 200}
                })
    bob =  dict()
    bob.update({"magic_ring" : {"obj" : "accesory", "rarity" : "rare", "quantity" : 1, "price" : 350}
               })
    categories = dict()
    total = 0
    total_items = 0

    print("=== Alice's Inventory ===")
    for item, info in alice.items():
        obj = info.get("obj")
        rarity = info.get("rarity")
        quantity = info.get("quantity")
        price = info.get("price")

        value = quantity * price
        print(f"{item} ({obj} , {rarity}): {quantity}x @ {price} gold each = {value} gold")
        total += value
        total_items += quantity

        categories[obj] = categories.get(obj, 0) + quantity
    
    cat_string = []
    print(f"\nInventory value: {total} gold")
    print(f"Item count: {total_items} items")
    for cat, count in categories.items():
        cat_string.append(f"{cat}({count})")
    print(f"Categories: {', '.join(cat_string)}")

    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    try:
        item_swap = "potion"
        alice[item_swap]["quantity"] -= 2

        bob.update ({item_swap : {
                    "obj" : alice[item_swap].get("obj"),
                    "rarity" : alice[item_swap].get("rarity"),
                    "quantity" : 2,
                    "price" : alice[item_swap].get("price")}
                    })
        print("Transaction successful!")
    except:
        print("The transaction can't be completed")

    print("\n=== Updated inventories ===")
    print(f"Alice potions: {alice.get('potion').get('quantity')}")
    print(f"Bob potions: {bob.get('potion').get('quantity')}")


    print("\n=== Inventory analytics ===")
    

    bob_values = 0
    bob_items = 0
    for info in bob.values():
        bob_values += info['quantity'] * info['price']
        bob_items += info['quantity']
    if total  > bob_values:
        print(f"Most value player: Alice ({total}) gold")
    else:
        print(f"Most value player: Bob ({bob_values}) gold")
    
    if total_items > bob_items:
        print(f"Most items: Alice ({total_items} items)")
    else:
        print(f"Most items: Bob ({bob_items} items)")
    rarest_list = []
    for name, info in alice.items():
        if info.get('rarity') in ['rare']:
            rarest_list.append(name)
    for name, info in bob.items():
        if info.get('rarity') in ['rare']:
            rarest_list.append(name)
    print(f"Rarest items: {', '.join(rarest_list)}")


    