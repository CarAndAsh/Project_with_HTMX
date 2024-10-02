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
prod_list = [('Laptop', 890),
             ('Desktop', 1590),
             ('Smartphone', 590),
             ('Fridge', 790),
             ('Dishwasher', 680),
             ('Washing machine', 650),
             ('TV', 520),
             ('Router', 149),
             ('Charger', 55),
             ('Powerbank', 98),
             ('Phone', 59),
             ('OTG', 1),
             ('Flash USB', 12),
             ('Gamepad', 35),
             ('Li-Ion accumulator', 15),
             ('Electric oven', 49),
             ('Gas oven', 349),
             ('Web-caamera', 15),
             ('Video camera', 155),
             ('Photo camera', 125),
             ('Mouse', 12),
             ('Keyboard', 24),
             ('LED-lamp', 3),
             ('Table', 105),
             ('Backpack', 8),
             ('Chair', 37),
             ('E-ink reader', 140),
             ('Tablet PC', 150),
             ('Audio system', 140),
             ('Microphone', 120),
             ('Microoven', 50),
             ('Touchpad', 20),
             ('Stick', 5),
             ('Action cam', 250),
             ('Drone', 300),
             ('Bag', 50),
             ('Clock', 10),
             ('Projector', 140),
             ('Aerator', 50),
             ('HDD', 12),
             ('SSD', 45),
             ('Cooler', 12),
             ('CD/DVD-ROM', 20),
             ('Floppy', 5),
             ('Card-reader', 10),
             ('Scanner', 30),
             ('Printer', 35),
             ('Copier', 23),
             ('Scroll-pad', 40),
             ('Smart TV', 720),
             ('Discount card', 20),
             ('Display', 150),
             ('Portable audio', 220),
             ('Some device', 80),
             ('Some accessoary', 22),
             ]
for name, price in prod_list:
    products_storage.add(name, price)
