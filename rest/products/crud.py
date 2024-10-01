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

    @property
    def names(self) -> set[str]:
        return {product.name for product in self.products.values()}

    def name_exist(self, product_name: str) -> bool:
        return product_name in self.names

    def add(self, product_name: str, product_price: int) -> Product:
        product = Product(self.next_id, name=product_name, price=product_price)
        self.products[product.id] = product
        return product

    def update(self, product_id: int, product_name: str, product_price: int) -> Product:
        product = self.products[product_id]
        product.name = product_name
        product.price = product_price
        return product

    def delete(self, product_id) -> None:
        self.products.pop(product_id, None)

    def get_list(self) -> list[Product]:
        return list(self.products.values())

    def get_by_id(self, product_id: int) -> Product | None:
        return self.products.get(product_id)


products_storage = ProductStorage()

prod_list = [('Laptop', 1290), ('Desktop', 1990), ('Smartphone', 1090)]
for name, price in prod_list:
    products_storage.add(name, price)
