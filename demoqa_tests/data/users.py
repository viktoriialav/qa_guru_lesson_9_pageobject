import dataclasses


@dataclasses.dataclass
class User:
    full_name: str
    email: str
    current_address: str


admin = User(
    full_name='admin adminovich',
    email='adminadmin@gmail.com',
    current_address='123 Broadway, suit 123',
)

guest = User(
    full_name='new guest',
    email='newguest@gmail.com',
    current_address='321 Broadway, suit 321',
)
