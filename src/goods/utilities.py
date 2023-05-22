from django.core.exceptions import ValidationError


def clean_order_nums(order_nums):
    try:
        order_nums.index(0)
        raise ValidationError('Order num cannot be zero.')
    except ValueError:
        pass

    for i in range(1, len(order_nums) + 1):
        try:
            index = order_nums.index(i)
        except ValueError:
            if i == 1:
                raise ValidationError('Order num must start from one.')
            raise ValidationError(f'Order num must increment one from past order num.')
        del order_nums[index]
