

# asserts
from requests_ftp.ftp import AuthError


def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price


shoes = {'name': 'Fnacy Shoes', 'price': 12434}
print(apply_discount(shoes, 0.25))
print(apply_discount(shoes, 2.0))


"""Don’t Use Asserts for Data Validation"""


def delete_product(store, prod_id, user):
    assert user.is_admin(), 'Must be admin'
    assert store.has_product(prod_id), 'Unknown product'
    store.get_product(prod_id).delete()

# Checking for admin privileges with an assert statement is dangerous.
# The has_product() check is skipped when assertions are disabled.


# never use assertions to do data validation
def delete_product_2(store, prod_id, user):
    if not user.is_admin():
        raise AuthError('Must be admin to delete')
    if not store.has_product(prod_id):
        raise ValueError('Unknown product id')
    store.get_product(prod_id).delete()

