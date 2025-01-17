import math
import random

# Словарь с заклинаниями по аспектам и кругам
spells = {
    "Аспект Иллюзий": {
        1: ["Частичная иллюзия","Мгновенная тьма","Малое приглушение шагов","Чревовещание","Приглушение голоса",
            "Ободрение","Приглушение запаха","Дымка","Сияние","Звуковая ловушка"],
        2: ["Малая иллюзия","Эмпатия","Отчаяние","Приглушение шагов","Успокоение","Магический афродизий","Призрачный фантом",
            "Материальная иллюзия","Ментальный хлыст","Концентрация Ярости"],
        3: ["Сильная иллюзия","Психический вопль","Соблазнение","Страх","Массовая головная боль","Ложные данные",
            "Двойник","Мистический туман","Невидимые заклинания","Укрепление воли"],
        4: ["Туманный щит","Смешаться с толпой","Саван тьмы","Поглощение света","Большая иллюзия","Смещение реальности",
            "Сон","Область слышимости","Дар убеждения","Два Я"],
        5: ["Три Я","Мучитель","Нематериальная форма","Туман иллюзий","Область концентрации","Отрешенность от мира",
            "Царство кошмаров","Ничего не предвещает","Идеальный хамелеон","Это моё!"],
        6: ["Контроль разума","Мастер иллюзий","Дверь измерения","Раскол реальности","Туман войны","Безмятежность",
            "Истинный мучитель","Истинный призрак","Чтение мыслей","Иллюзорное воинство"]
    },
    "Аспект Света": {
        1: ["Малое исцеление","Шар света","Освещенное оружие","Освещенная броня","Чувство скверны","Вспышка света",
            "Семь казней небесных","Флагеллянт","Отрешенность от плотских забот","Освящение жидкости"],
        2: ["Исцеление болезней","Святые путы","Среднее исцеление","Светоносный щит","Телесная бодрость",
            "Освященный круг","Круг сострадания","Стрела света","Путеводная звезда света","Разложение демонов"],
        3: ["Ангельский лик","Благословение солнца","Аура исцеления","Луч света","Щит от демонов","Исцеление травмы",
            "Аура святого","Укрепление здоровья","Восход солнца","Ослабление нечисти"],
        4: ["Песнь небес","Исцеление","Непроницаемый купол","Печать света","Очищение от скверны","Оружие из чистого света",
            "Покров света","Доспехи из чистого света","Солнечные копья","Столп Света"],
        5: ["Небесный колокол","Выжигание скверны","Милость небес","Ангельские крылья","Перст небес","Потоки небес",
            "Ангел-хранитель","Единение со светом","Великое исцеление","Последний шанс"],
        6: ["Форма ангела","Кара небес","Воскрешение","Сила Анаиэля","Дух Нанаэль","Милосердие Миниэль","Призыв Ангела",
            "Стойкость Рахмиэля","Изгнание","Мудрость Ансиэля"]
    },
    "Ведьмовство": {
        1: ['Запечатывание проема','Звуковая изоляция ','Подогрев пищи','Кинетический удар','Незримые помощники',
            'Облегчение веса','Восстановление предмета','Уменьшение боли ','Моментальная готовка','Истина в вине!'],
        2: ['Изоляция комнаты','Магический щит','Сдерживание','Повышение иммунитета','Полное восстановление',
            'Фиксация предмета','Защитный талисман','Понимание языка','Несварение','Усталость'],
        3: ['Магический зонд','Легкая болезнь','Поиск снадобий','Взгляд за черту','Магический симбиоз',
            'Удар первородной магией','Малая телепортация ','Телепортация предмета','Состаривание',
            'Первородное разрушение'],
        4: ['Телепортация','Болезнь','Хождение по снам','Ядовитый поцелуй','Немота','Потусторонняя невидимость',
            'Впитывание','Раскрытие тайн','Материализация присутствия','Магический хлыст'],
        5: ['Смертельная болезнь','Создание зелья','Телекинез ','Бестелесность','Магическое оружие',
            'Показательная смерть','Исцеление болезней','Защитный купол','Подмена силы','Магический дисбаланс'],
        6: ['Опустошение','Манипуляция возрастом','Магический шторм','Видение','Хозяин черты','Управление погодой',
            'Шепот магической бездны','Ты – это я, а я – это ты','Переполняющая мощь','Низвержение']
    },
    "Аспект Воды": {
        1: ['Тучка', 'Наполнение', 'Роса', 'Малое Замораживание', 'Ледяная сосулька', 'Чувство воды',
            'Клинок мороза', 'Преобразование', 'Подогревание воды', 'Поток воды'],
        2: ['Хождение по воде', 'Снег', 'Ледяной щит', 'Укрепление холодом', 'Ледяной шип', 'Горячий пар',
            'Замораживание', 'Сопротивление огню', 'Дождь ледяных слёз', 'Управление водой'],
        3: ['Рассечение', 'Подводное дыхание', 'Ледяное копье', 'Кипячение воды', 'Водяной змей', 'Тотальная заморозка',
            'Метель', 'Чары льда', 'Гейзер', 'Водный покров'],
        4: ['Град ледяных копий', 'Ледяная глыба', 'Водяной элементаль', 'Снежная буря', 'Ледяное кольцо',
            'Водное расчленение', 'Поле ледяных шипов', 'Водяное тело', 'Ледяная тюрьма', 'Аура зимы'],
        5: ['Стена воды', 'Стена льда', 'Превращение в воду', 'Снос', 'Ледниковый период', 'Ледяной доспех',
            'Замораживание жизни', 'Управление потоком', 'Океанский замок', 'Водный вихрь'],
        6: ['Ледяная буря', 'Иссушение', 'Поле гейзеров', 'Цунами', 'Водоворот', 'Ледяная комета',
            '- 200 С', 'Ледяной Великан', 'Холод Космоса']
    },
    "Аспект Воздуха": {
        1: ['Толчок', 'Притяжение', 'Дуновение', 'Воздушный хлопок', 'Прыжок', 'Разряд', 'Свежий воздух',
            'Задержка дыхания', 'Изменение воздуха', 'Легкий шаг'],
        2: ['Щит ветра', 'Парение', 'Воздушное завихрение', 'Легкое как пёрышко', 'Сталь как пух', 'Воздушная плеть',
            'Левитация предметов', 'Удар по воздуху', 'Электрошок', 'Мираж'],
        3: ['Ускорение', 'Ярость ветра', 'Щит молний', 'Спринтер', 'Молния', 'Воздушная ладонь', 'Воздушный щит',
            'Ударная волна', 'Управление воздухом', 'Усиленная левитация предметов'],
        4: ['Небесная молния', 'Воздушный элементаль', 'Уплотнение', 'Область ускорения', 'Тело из воздуха',
            'Цепная молния', '0', '0', '0', '0'],
        5: ['Воздушная стена', 'Град небесных молний', 'Шаровая молния', 'Око Бури', 'Сверхзвуковой рывок',
            'Воля ветров', '0', '0', '0', '0'],
        6: ['Торнадо', 'Вакуум', 'Удушение', 'Грозовой фронт', 'Тайфун', '0', '0', '0', '0', '0']
    },
    "Аспект Тьмы": {
        1: ['Проклятье слабости', 'Демоническое касание', 'Демонический покров', 'Кровавая жажда',
            'Тень террора', 'Проклятые путы', 'Кровавая завеса', 'Демонический клинок', 'Демоническая сила',
            'Длань Астарота'],
        2: ['Сфера разрушения', 'Тёмный пакт', 'Зов Преисподней', 'Метка Гириадоса', 'Крик терзаемой души.',
            'Тёмное копьё', 'Отравленный дождь', 'Юдоль слёз', 'Кровь Астарота', 'Демонический щит.'],
        3: ['Жатва Баала', 'Демоническая броня', 'Нисхождение Тьмы', 'Осквернение', 'Плеть Валахора',
            'Шутка Белиала', 'Чёрные узы', 'Удар демона', 'Аура отчаяния', 'Хватка Уркантоса'],
        4: ['Разрушение уз Судьбы', '«Света здесь нет»', 'Обольщение Лилит', 'Арена Баала', 'Цепи Пыточника',
            'Пламя Инферно', 'Когти Терзателя', 'Демоническое зрение', 'Хаос', 'Терзающие шипы'],
        5: ['Мост в Ад', 'Адская жатва', 'Демоническая маска', 'Комната тьмы', 'Расчленение', 'Метаморфоз',
            'Чужой', 'Демонические крылья', 'Бессмысленная жертва', 'Безумие'],
        6: ['Дверь в Ад', 'Пришествие Апокалипсиса', 'Форма Демона', 'Кровавый апокалипсис', 'Договор',
            'Массовое безумие']
    },
    "Аспект Жизни": {
        1: ['Ядовитые шипы', 'Разговор с животными', 'Найти животное', 'Нюх волка', 'Зоркость сокола',
            'Оживить/Взрастить растение', 'Шерстяной покров', 'Сила древа', 'Целебный цветок', 'Лесной путь'],
        2: ['Путы стеблей', 'Природная регенерация', 'Обращение в птицу', 'Звериная ловкость',
            'Звериная сила', 'Звериная стойкость', 'Звериная скорость', 'Покров Росы', 'Живое растение',
            'Усилить животное '],
        3: ['Клетка из корней', 'Подчинить животное', 'Обращение в копытное', 'Броненосец', 'Поиск растения',
            'Блокировка некромантии', 'Святость жизни', 'Обращение в хищника', 'Громогласный Рёв', 'Заросли'],
        4: ['Лес', 'Слеза Илирии', 'Энт', 'Вмешательство природы', 'Кольцо деревьев',
            'Покрывало матери природы', 'Стая гигантских шершней', 'Гигантский плотоядный цветок',
            'Заряд кислоты', 'Обращение в рыбу'],
        5: ['Длань природы', 'Духи природы', 'Дух Зверя', 'Духи флоры', 'Создание', 'Круг жизни',
            'Спокойствие природы', 'Круг Регенерации', 'От древа к древу', 'Договор с природой'],
        6: ['Победа над Смертью', 'Вам здесь не место!', 'Лесное воинство', 'Кошмарный лес', 'Слияние',
            'Власть Илирии', 'Глобальная сеть']
    },
    # "Аспект Земли": {  # Оставить закомментированным или добавить, когда будет нужный функционал
    #    1: ['', '', '', '', '', '', '', '', '', ''],
    #    2: ['', '', '', '', '', '', '', '', '', ''],
    #    3: ['', '', '', '', '', '', '', '', '', ''],
    #    4: ['', '', '', '', '', '', '', '', '', ''],
    #    5: ['', '', '', '', '', '', '', '', '', ''],
    #    6: ['', '', '', '', '', '', '', '', '', '']
    #},
    "Аспект Смерти": {
        1: ['Некротическое зрение', 'Костяная стрела', 'Малое поднятие нежити', 'Малое подчинение нежити',
            'Малое упокоение нежити', 'Чувство материальной нежити', 'Могильный хлад', 'Поиск трупа',
            'Танец костей', 'Крик банши '],
        2: ['Среднее поднятие нежити', 'Среднее упокоение нежити', 'Среднее подчинение нежити',
            'Некротическое пламя', 'Слёзы забвения', 'Во имя смерти!', 'Перенос сознания', 'Поглощение энергии смерти',
            'Чувство неупокоенных', 'Наложение рук'],
        3: ['Крупное поднятие нежити', 'Крупное подчинение нежити', 'Крупное упокоение нежити', 'Зов нежити',
            'Смертельный союз', 'Коса жнеца', 'Неупокоенный дух', 'Отрешенность от жизни', 'Укрепление',
            'Потустороннее восстановление'],
        4: ['Метка смерти', 'Форма призрака', 'Кавалерия душ', 'Поступь неизбежности', 'Тёмный наббат',
            'Истончение грани', 'Наказание ', 'Реквием душ', 'Непричастие', 'Иссушение жизненных сил'],
        5: ['Глас Смерти', '«Всего-лишь смертная оболочка»', 'Высасывание жизни', 'Хватка нежити',
            'Выталкивание души', 'Катехизис Смерти', 'Сквозь мглу', 'Выстрел эктоплазмы', 'Удар Жнеца',
            'Монумент Смерти'],
        6: ['Цель всей жизни - смерть', 'Врата в посмертие', 'Форма Лича', 'Великое поднятие нежити', 'Щит Смерти',
            'Тёмное пророчество', 'Безмолвие Рока', 'Возвращение души']
    },
    "Аспект Огня": {
        1: ['Факел', 'Согревание', 'Нагрев', 'Огненная стрела', 'Зачаровать одежду', 'Высушивание одежды',
            'Дымовая завеса', 'Огненная струя', 'Унять огонь', 'Огненная плеть'],
        2: ['Управление огнём', 'Усиление', 'Пламенеющий клинок', 'Огненная ловушка', 'Закалка',
            'Танец огня', 'Град огненных стрел', 'Аура огня', 'Печать огня', 'Взрывающийся газ'],
        3: ['Огненный шар', 'Огненный взрыв', 'Огненный змей', 'Раскаление', 'Снаряд из магмы',
            'Огненный купол', 'Кровь феникса', 'Магмовый клинок', 'Огненный лук', 'Касание жара'],
        4: ['Огненный снаряд', 'Огненный столб', 'Огненный саванн', 'Огненный круг', 'Меч чистого пламени',
            'Огненный элементаль', 'Магмовое копье', 'Огненный покров', 'Огненное тело', 'Невосприимчивость к огню'],
        5: ['Стена огня', 'Огненный дождь', 'Расплавление', 'Первородное пламя земли', 'Череда огненных столбов',
            'Путь пламени', 'Магмовый дождь', 'Преобразование в плазму', 'Магмовый доспех', 'Испепеление'],
        6: ['Дыхание дракона', 'Армагеддон', 'Форма феникса', 'Метеоритный дождь', 'Огненный великан',
            'Река магмы']
    }
}

# Веса для кругов заклинаний
circle_weights = [100, 80, 60, 40, 20, 1]

# Для семи аспектов (9 аспектов + "Аспект Земли" в комментариях)
aspect_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10]  # Здесь суммарно только 8 аспектов. Если добавите ещё один, увеличьте до 9.

# Случайный выбор аспекта с учетом весов
selected_aspect = random.choices(list(spells.keys()), weights=aspect_weights)[0]

# Случайный выбор круга внутри выбранного аспекта
selected_circle = random.choices(list(spells[selected_aspect].keys()), weights=circle_weights)[0]

# Случайный выбор заклинания внутри выбранного аспекта и круга
selected_spell = random.choice(spells[selected_aspect][selected_circle])

print(f"Выпало заклинание: {selected_spell} (Аспект: {selected_aspect}, Круг: {selected_circle})")