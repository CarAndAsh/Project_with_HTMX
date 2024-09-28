from dataclasses import dataclass, field


@dataclass
class Product:
    id: int
    name: str
    price: int


@dataclass
class ProductStorage:
    products: dict[int, Product] = field(default_factory=dict)
    last_id: int = 0

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    def add(self, product_name: str, product_price: int) -> Product:
        product = Product(self.next_id, name=product_name, price=product_price)
        self.products[product.id] = product
        return product

    def get_list(self) -> list[Product]:
        return list(self.products.values())


products_storage = ProductStorage()

prod_list = [('Laptop', 1290), ('Desktop', 1990), ('Smartphone', 1090)]
for name, price in prod_list:
    products_storage.add(name, price)
