


# Переменная "weapon_damage" - значение переменной соответствует Рейтингу Силы персонажа + фиксированный урон оружия + урон абилок (Грозное, либо, Сокрушающее).
# Переменная "result_check" - Количество степеней успеха, выпавшее при проверке. Расчёт ведётся по формуле: Значение персонажа - Результат куба.
# Переменная "modifier" - Модификатор проверки (Расчитывает суммой отрицательных значение и положительных значений модификатора).

# Получаем результат броска куба
dice_result = int(input('Введите результат броска куба: '))

# Получаем силу персонажа и вычисляем модификатор силы
strength = int(input('Введите силу персонажа: '))
r_strength = strength // 10

# Получаем фиксированный урон оружия
damage = int(input('Введите фиксированный урон оружия: '))

# Определяем способности оружия
weapon_abilities = dice_result % 10

# Получаем общий результат навыка
general_value = int(input('Введите общий результат навыка: '))

# Вычисляем урон от оружия
weapon_damage = r_strength + damage + weapon_abilities

# Вычисляем разницу для результата
result_check = (general_value - dice_result) // 10

# Получаем модификаторы
modifier_plus = int(input('Введите положительные модификаторы: '))
modifier_minus = int(input('Введите отрицательные модификаторы: '))
modifier = (modifier_plus + modifier_minus) // 10

# Перевертыш (для определения попадания в голову)
revers_dice_result = 0

while dice_result > 0:
    digit = dice_result % 10
    revers_dice_result = revers_dice_result * 10 + digit
    dice_result = dice_result // 10
# print(revers_dice_result)

# Функция для вычисления итогового результата
def SFD(weapon_damage, result_check, modifier):
    return weapon_damage + result_check + modifier

# Вычисляем итоговый результат
result_ = SFD(weapon_damage, result_check, modifier)

if revers_dice_result < 10:
    print(result_ * 2)
else:
    print(result_)

