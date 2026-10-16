"""Synthetic checkout example used only for skill evaluation."""


def submit_checkout(cart, customer_id, payment_token, inventory, payments, orders, events):
    if not inventory.reserve(cart.items):
        return {"status": "rejected", "reason": "inventory_unavailable"}

    authorization = payments.authorize(payment_token, cart.total)
    if not authorization.approved:
        inventory.release(cart.items)
        return {"status": "rejected", "reason": "payment_declined"}

    order = orders.save(customer_id, cart.items, cart.total, authorization.id)
    events.publish("OrderPlaced", {"order_id": order.id})
    return {"status": "accepted", "order_id": order.id}
