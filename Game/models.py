from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.CharField(max_length=500)  # store URL or file path
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.game.cost * self.quantity

    def __str__(self):
        return self.game.name