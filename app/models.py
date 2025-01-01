from django.db import models

# Clients Table
class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Orders Table
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="orders")
    order_date = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('pending', 'Pending'),
        ('in_process', 'In Process'),
        ('shipped', 'Shipped'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Order {self.order_id} by {self.client.name}"

# Photos Table
class Photo(models.Model):
    photo_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, related_name='photos', on_delete=models.CASCADE)
    file_path = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    print_size_choices = [
        ('4x6', '4x6'),
        ('5x7', '5x7'),
        ('8x10', '8x10'),
    ]
    print_size = models.CharField(max_length=5, choices=print_size_choices)
    finish_type_choices = [
        ('glossy', 'Glossy'),
        ('matte', 'Matte'),
    ]
    finish_type = models.CharField(max_length=10, choices=finish_type_choices)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Photo {self.photo_id} for Order {self.order.order_id}"

# Print Options Table
class PrintOption(models.Model):
    option_id = models.AutoField(primary_key=True)
    size_choices = [
        ('4x6', '4x6'),
        ('5x7', '5x7'),
        ('8x10', '8x10'),
    ]
    size = models.CharField(max_length=5, choices=size_choices)
    finish_type_choices = [
        ('glossy', 'Glossy'),
        ('matte', 'Matte'),
    ]
    finish_type = models.CharField(max_length=10, choices=finish_type_choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.size} {self.finish_type} - ₱{self.price}"

# Payments Table
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payments")
    payment_method = models.CharField(max_length=20, default='gcash')  # Fixed to GCash
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('completed', 'Completed'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')
    transaction_reference = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Payment {self.payment_id} for Order {self.order.order_id}"
