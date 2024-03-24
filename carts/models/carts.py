from django.db import models

from common.models.base import BaseModel


class Cart(BaseModel):
    """
    Модель Корзины.

    Аттрибуты:
        * `user` (ForeignKey): пользователи.
        * `cart_price` (ForeignKey): пользователи.
        * `preset_id` (ManyToManyField): товары в корзине.
        * `cart_items` (CartPreset: обратное обращение с внешнего ключа cart
                                содержимого корзины.
    """

    # region ------------------------- АТРИБУТЫ КОРЗИНЫ -----------------------------
    user = models.ForeignKey(
        to="users.User",
        on_delete=models.CASCADE,
        related_name="cart",
        verbose_name="Users",
        null=True,
        blank=True,
    )
    products = models.ManyToManyField(
        to="presets.preset",
        related_name="cart_products",
        verbose_name="Products in cart",
        blank=True,
        through="CartItem",
    )

    # endregion ---------------------------------------------------------------------
    # objects = CartManager()
    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"


class CartPreset(BaseModel):
    """
    Модель Содержимого Корзины.

    Аттрибуты:
        * `cart` (ForeignKey): корзина.
        * `product` (ForeignKey): товар.
        * `quantity` (PositiveSmallIntegerField): кол-во товара.
        * `total_price_product` (DecimalField): общая стоимость одного товара
    """

    # region --------------------- АТРИБУТЫ СОДЕРЖИМОГО КОРЗИНЫ ---------------------
    cart = models.ForeignKey(
        to="carts.Cart",
        on_delete=models.CASCADE,
        related_name="products_info",
        verbose_name="User",
        null=True,
        blank=True,
    )
    preset = models.ForeignKey(
        to="preset.Preset",
        on_delete=models.CASCADE,
        related_name="carts_info",
        verbose_name="Preset",
        null=True,
        blank=True,
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name="Presets quantity", default=1
    )
    total_price_product = models.DecimalField(
        verbose_name="General preset price",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    # endregion ---------------------------------------------------------------------

    class Meta:
        verbose_name = "Cart content"
        verbose_name_plural = "Carts content"
        # Товар не должен повторяться в корзине
        # unique_together = ("cart", "product")

    def __str__(self) -> str:
        return f"{self.product.name}({self.quantity})"
