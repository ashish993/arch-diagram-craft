"""Behavioral examples for the synthetic checkout service."""


def test_inventory_rejection_happens_before_payment(checkout_fixture):
    result = checkout_fixture.submit(inventory_available=False, payment_approved=True)
    assert result["reason"] == "inventory_unavailable"
    assert checkout_fixture.payment_calls == 0


def test_declined_payment_releases_inventory(checkout_fixture):
    result = checkout_fixture.submit(inventory_available=True, payment_approved=False)
    assert result["reason"] == "payment_declined"
    assert checkout_fixture.inventory_releases == 1


def test_order_event_contains_only_order_identifier(checkout_fixture):
    checkout_fixture.submit(inventory_available=True, payment_approved=True)
    assert checkout_fixture.last_event == ("OrderPlaced", {"order_id": "order-1"})
