from django.utils import timezone

def get_exchange_rate(from_currency, to_currency, transaction_date=None):
    if from_currency == to_currency:
        return 1.0

    if not transaction_date:
        transaction_date = timezone.now().date()

    # Placeholder for actual logic involving a CurrencyExchange model
    return 1.0
