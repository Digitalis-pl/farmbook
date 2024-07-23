import stripe

from config.settings import STRIPE_API_KEY

from forex_python.converter import CurrencyRates

stripe.api_key = STRIPE_API_KEY


def convert_rub_to_usd(amount):
    c = CurrencyRates()
    rate = c.get_rate('RUB', 'USD')
    return int(amount * rate)


def create_product(name, data):
    return stripe.Product.create(name=name,
                                 metadata=data)


def create_price(amount, product):
    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product=product['id']
    )


def create_session(quantity, price):
    session = stripe.checkout.Session.create(
        success_url="https://127/0.0.1:8000",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')


def check_sessions(session_id):
    return stripe.checkout.Session.retrieve(
        session_id,
    )

