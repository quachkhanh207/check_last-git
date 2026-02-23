def add_product(products, product):
    products.append(product)


def find_product_by_id(products, product_id):
    for p in products:
        if p["id"] == product_id:
            return p
    return None


def delete_product(products, product_id):
    product = find_product_by_id(products, product_id)
    if product:
        products.remove(product)
        return True
    return False


def update_product(products, product_id, new_data):
    product = find_product_by_id(products, product_id)
    if product:
        product.update(new_data)
        return True
    return False
