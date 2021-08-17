TRANS_CHOICES = (
    ('Buy', 'Buy'),
    ('Sell', 'Sell'),
)

BROKER_CHOICES = (
    ('Alice Blue', 'Alice Blue'),
    ('Angel Broking', 'Angel Broking'),
    ('Fyers', 'Fyers'),
    ('Upstox', 'Upstox'),
    ('Zerodha', 'Zerodha'),
)

PRODUCT_TYPE_CHOICES = (
    ('Regular', 'Regular'),
    ('CO', 'CO'),
    ('BO', 'BO'),
    ('AMO', 'AMO'),
)

ADV_PRODUCT_TYPE = (
    ('Intraday', 'Intraday'),
    ('CNC', 'CNC'),
    ('Margin', 'Margin'),
)

ORDER_TYPE_CHOICES = (
    ('Market', 'Market'),
    ('Limit', 'Limit'),
    ('Stop', 'Stop'),
    ('Stop Limit', 'Stop Limit'),
)

VALIDITY_CHOICES = (
    ('Day', 'Day'),
    ('IOC', 'IOC'),
)
