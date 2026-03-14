from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Union, Tuple
import math


class MaterialType(Enum):
    """Типы строительных материалов."""
    BRICK = "Кирпич"
    CONCRETE = "Бетон"
    WOOD = "Древесина"
    METAL = "Металл"
    GLASS = "Стекло"
    INSULATION = "Утеплитель"


class ConstructionStatus(Enum):
    """Статусы строительства."""
    PLANNING = "Планирование"
    FOUNDATION = "Заливка фундамента"
    WALLS = "Возведение стен"
    ROOF = "Кровля"
    FINISHING = "Отделка"
    COMPLETED = "Завершено"
    ON_HOLD = "Приостановлено"


class ConstructionProject(ABC):
    """
    Базовый абстрактный класс для всех строительных проектов.

    Предоставляет общую функциональность для управления стройкой:
    планирование, учет материалов, контроль бюджета и сроков.

    Attributes:
        _project_id (str): Уникальный идентификатор проекта (непубличный)
        _name (str): Название проекта
        _address (str): Адрес строительства
        _start_date (datetime): Дата начала строительства
        _end_date (datetime): Планируемая дата окончания
        _status (ConstructionStatus): Текущий статус
        _budget (float): Бюджет проекта
        _total_cost (float): Текущие затраты
        _materials (Dict): Использованные материалы
        _workers (List): Список рабочих
        _safety_violations (int): Количество нарушений техники безопасности
    """

    def __init__(self, project_id: str, name: str, address: str,
                 budget: float, start_date: Optional[datetime] = None) -> None:
        """
        Инициализация строительного проекта.

        Args:
            project_id: Уникальный ID проекта
            name: Название проекта
            address: Адрес строительства
            budget: Бюджет проекта
            start_date: Дата начала
        """
        self._project_id = project_id
        self._name = name
        self._address = address
        self._start_date = start_date or datetime.now()
        self._end_date = self._start_date + timedelta(days=365)
        self._status = ConstructionStatus.PLANNING
        self._budget = budget
        self._total_cost = 0.0
        self._materials: Dict[MaterialType, float] = {}
        self._workers: List[Dict] = []
        self._safety_violations = 0
        self._daily_reports: List[Dict] = []
        self._permit_number = self._generate_permit_number()

    def __str__(self) -> str:
        """Пользовательское строковое представление проекта."""
        progress = (self._total_cost / self._budget * 100) if self._budget > 0 else 0
        return (f"🏗 {self._name} | ID: {self._project_id} | "
                f"Статус: {self._status.value} | "
                f"Бюджет: {self._total_cost:,.0f}/{self._budget:,.0f} руб. ({progress:.1f}%) | "
                f"Адрес: {self._address}")

    def __repr__(self) -> str:
        """Техническое строковое представление для отладки."""
        return (f"{self.__class__.__name__}(project_id='{self._project_id}', "
                f"name='{self._name}', address='{self._address}', "
                f"budget={self._budget}, status='{self._status.value}')")

    def _generate_permit_number(self) -> str:
        """Внутренний метод генерации номера разрешения на строительство."""
        import random
        year = datetime.now().year
        number = random.randint(1000, 9999)
        return f"BUILD-{year}-{number}"

    def _log_daily_report(self, report_type: str, description: str) -> None:
        """
        Внутренний метод логирования ежедневных отчетов.

        Args:
            report_type: Тип отчета
            description: Описание
        """
        self._daily_reports.append({
            'date': datetime.now(),
            'type': report_type,
            'description': description,
            'project_id': self._project_id
        })

    def order_materials(self, material_type: MaterialType, quantity: float,
                        unit_price: float) -> bool:
        """
        Заказать строительные материалы.

        Args:
            material_type: Тип материала
            quantity: Количество
            unit_price: Цена за единицу

        Returns:
            bool: True если заказ успешен
        """
        cost = quantity * unit_price

        if self._total_cost + cost > self._budget:
            print(f" Превышение бюджета! Требуется: {cost:,.0f} руб., "
                  f"доступно: {self._budget - self._total_cost:,.0f} руб.")
            return False

        if material_type in self._materials:
            self._materials[material_type] += quantity
        else:
            self._materials[material_type] = quantity

        self._total_cost += cost
        self._log_daily_report("MATERIALS_ORDERED",
                               f"Заказано {quantity} {material_type.value}")
        print(f" Заказаны материалы: {quantity} {material_type.value} на {cost:,.0f} руб.")
        return True

    def hire_worker(self, name: str, position: str, salary: float) -> None:
        """
        Нанять рабочего.

        Args:
            name: Имя
            position: Должность
            salary: Зарплата
        """
        worker = {
            'name': name,
            'position': position,
            'salary': salary,
            'start_date': datetime.now(),
            'hours_worked': 0,
            'safety_violations': 0
        }
        self._workers.append(worker)
        print(f"👷 Нанят рабочий: {name} - {position}")

    def record_safety_violation(self, worker_name: str, description: str) -> None:
        """
        Зафиксировать нарушение техники безопасности.

        Args:
            worker_name: Имя рабочего
            description: Описание нарушения
        """
        self._safety_violations += 1
        for worker in self._workers:
            if worker['name'] == worker_name:
                worker['safety_violations'] += 1
                break

        self._log_daily_report("SAFETY_VIOLATION",
                               f"{worker_name}: {description}")
        print(f"Нарушение ТБ: {description}")

    def get_project_summary(self) -> Dict:
        """
        Получить сводку по проекту.

        Returns:
            Dict: Сводная информация
        """
        return {
            'project_id': self._project_id,
            'name': self._name,
            'address': self._address,
            'status': self._status.value,
            'budget': self._budget,
            'spent': self._total_cost,
            'remaining': self._budget - self._total_cost,
            'materials': {k.value: v for k, v in self._materials.items()},
            'workers_count': len(self._workers),
            'safety_violations': self._safety_violations,
            'permit_number': self._permit_number,
            'start_date': self._start_date.strftime("%Y-%m-%d"),
            'end_date': self._end_date.strftime("%Y-%m-%d")
        }

    @abstractmethod
    def calculate_foundation_depth(self) -> float:
        """Абстрактный метод расчета глубины фундамента."""
        pass


class ResidentialBuilding(ConstructionProject):
    """
    Жилой дом.

    Расширяет базовый класс ConstructionProject, добавляя специфические
    для жилого строительства характеристики: этажность, количество квартир,
    наличие лифта, парковки и т.д.

    Attributes:
        _floors (int): Количество этажей
        _apartments (int): Количество квартир
        _has_elevator (bool): Наличие лифта
        _parking_spots (int): Количество парковочных мест
        _building_type (str): Тип здания (монолит, панель, кирпич)
        _energy_efficiency_class (str): Класс энергоэффективности
    """

    def __init__(self, project_id: str, name: str, address: str, budget: float,
                 floors: int, apartments: int, building_type: str = "Монолит",
                 has_elevator: bool = True, parking_spots: int = 0, **kwargs) -> None:
        """
        Инициализация жилого дома.

        Args:
            project_id: ID проекта
            name: Название
            address: Адрес
            budget: Бюджет
            floors: Количество этажей
            apartments: Количество квартир
            building_type: Тип здания
            has_elevator: Наличие лифта
            parking_spots: Парковочные места
            **kwargs: Дополнительные параметры
        """
        super().__init__(project_id, name, address, budget, **kwargs)

        self._floors = floors
        self._apartments = apartments
        self._building_type = building_type
        self._has_elevator = has_elevator
        self._parking_spots = parking_spots
        self._energy_efficiency_class = "C"
        self._sold_apartments = 0
        self._current_floor = 0

    def __str__(self) -> str:
        """Перегрузка строкового представления."""
        base_str = super().__str__()
        return (f"🏢 ЖИЛОЙ ДОМ {base_str} | "
                f"Этажей: {self._floors} | Квартир: {self._apartments} | "
                f"Тип: {self._building_type} | "
                f"Продано: {self._sold_apartments}/{self._apartments}")

    def __repr__(self) -> str:
        """Перегрузка технического представления."""
        return (f"ResidentialBuilding(project_id='{self._project_id}', "
                f"name='{self._name}', floors={self._floors}, "
                f"apartments={self._apartments})")

    def calculate_foundation_depth(self) -> float:
        """
        Расчет глубины фундамента для жилого дома.

        Returns:
            float: Глубина фундамента в метрах
        """

        base_depth = 1.5
        floor_factor = self._floors * 0.2 + 0.3
        return base_depth + floor_factor

    def construct_floor(self) -> bool:
        """
        Построить один этаж.

        Returns:
            bool: True если этаж построен
        """
        if self._current_floor >= self._floors:
            print(" Все этажи уже построены")
            return False

        self._current_floor += 1
        progress = (self._current_floor / self._floors) * 100
        print(f" Построен этаж {self._current_floor}/{self._floors} ({progress:.0f}%)")

        if self._current_floor == self._floors:
            self._status = ConstructionStatus.ROOF
            print(" Все этажи построены! Переход к кровле")

        return True

    def sell_apartment(self, apartment_number: str, price: float) -> bool:
        """
        Продать квартиру.

        Args:
            apartment_number: Номер квартиры
            price: Цена

        Returns:
            bool: True если продажа успешна
        """
        if self._status != ConstructionStatus.COMPLETED:
            print(" Продажа возможна только после завершения строительства")
            return False

        if self._sold_apartments >= self._apartments:
            print(" Все квартиры проданы")
            return False

        self._sold_apartments += 1
        self._total_cost += price * 0.3
        print(f" Продана квартира {apartment_number} за {price:,.0f} руб.")
        return True


class CommercialBuilding(ConstructionProject):
    """
    Коммерческое здание (офис, ТЦ, склад).

    Расширяет базовый класс ConstructionProject для коммерческой недвижимости.

    Attributes:
        _building_type (str): Тип (офис, ТЦ, склад)
        _floor_area (float): Площадь этажа
        _rentable_area (float): Арендопригодная площадь
        _has_parking (bool): Наличие парковки
        _security_system (bool): Система безопасности
        _floors_above_ground (int): Надземных этажей
        _floors_underground (int): Подземных этажей
    """

    def __init__(self, project_id: str, name: str, address: str, budget: float,
                 building_type: str, floor_area: float, floors_above: int = 1,
                 floors_underground: int = 0, has_parking: bool = True, **kwargs) -> None:
        """
        Инициализация коммерческого здания.
        """
        super().__init__(project_id, name, address, budget, **kwargs)

        self._building_type = building_type
        self._floor_area = floor_area
        self._floors_above_ground = floors_above
        self._floors_underground = floors_underground
        self._has_parking = has_parking
        self._security_system = False
        self._rentable_area = floor_area * floors_above * 0.85
        self._tenants: List[Dict] = []
        self._leased_area = 0

    def __str__(self) -> str:
        """Перегрузка строкового представления."""
        base_str = super().__str__()
        leased_percent = (self._leased_area / self._rentable_area * 100) if self._rentable_area > 0 else 0
        return (f" КОММЕРЧЕСКОЕ {base_str} | "
                f"Тип: {self._building_type} | "
                f"Площадь: {self._floor_area:.0f}м²/этаж | "
                f"Арендовано: {leased_percent:.1f}%")

    def __repr__(self) -> str:
        """Перегрузка технического представления."""
        return (f"CommercialBuilding(project_id='{self._project_id}', "
                f"name='{self._name}', type='{self._building_type}')")

    def calculate_foundation_depth(self) -> float:
        """
        Расчет глубины фундамента для коммерческого здания.

        Причина перегрузки: Коммерческие здания часто имеют подземные этажи
        (паркинги, склады), поэтому фундамент должен быть глубже.

        Returns:
            float: Глубина фундамента в метрах
        """
        base_depth = 2.0
        underground_factor = self._floors_underground * 3.5
        load_factor = 1.5 if self._building_type == "Склад" else 1.0
        return (base_depth + underground_factor) * load_factor

    def install_security_system(self, system_type: str, cost: float) -> None:
        """
        Установить систему безопасности.

        Args:
            system_type: Тип системы
            cost: Стоимость
        """
        if self._total_cost + cost > self._budget:
            print(" Недостаточно бюджета для системы безопасности")
            return

        self._security_system = True
        self._total_cost += cost
        print(f" Установлена система безопасности: {system_type}")

    def lease_space(self, tenant_name: str, area: float, rent_per_month: float,
                    months: int) -> bool:
        """
        Сдать площадь в аренду.

        Args:
            tenant_name: Название арендатора
            area: Арендуемая площадь
            rent_per_month: Арендная плата в месяц
            months: Срок аренды

        Returns:
            bool: True если аренда оформлена
        """
        if self._status != ConstructionStatus.COMPLETED:
            print(" Аренда возможна только после завершения строительства")
            return False

        if self._leased_area + area > self._rentable_area:
            print(" Недостаточно свободной площади")
            return False

        lease = {
            'tenant': tenant_name,
            'area': area,
            'rent': rent_per_month,
            'months': months,
            'start_date': datetime.now(),
            'total_value': rent_per_month * months
        }

        self._tenants.append(lease)
        self._leased_area += area
        self._total_cost += rent_per_month * months * 0.1

        print(f" Сдано в аренду {area}м² компании {tenant_name} "
              f"на {months} мес., общая стоимость: {rent_per_month * months:,.0f} руб.")
        return True

if __name__ == "__main__":


    print("=" * 70)
    print("  СИСТЕМА УПРАВЛЕНИЯ СТРОИТЕЛЬСТВОМ")
    print("=" * 70)

    # 1. Жилой дом
    print("\n ПРОЕКТ 1: Жилой дом")
    print("-" * 50)

    residential = ResidentialBuilding(
        project_id="R-2024-001",
        name="ЖК 'Солнечный'",
        address="г. Санкт-Петербург, ул. Строителей, 10",
        budget=250_000_000,
        floors=17,
        apartments=120,
        building_type="Монолит-кирпич",
        parking_spots=80
    )
    print(residential)
    print(repr(residential))

    residential.order_materials(MaterialType.CONCRETE, 500, 5000)
    residential.order_materials(MaterialType.BRICK, 100000, 15)
    residential.hire_worker("Иван Петров", "Бетонщик", 80000)
    residential.hire_worker("Петр Сидоров", "Каменщик", 90000)

    for _ in range(5):
        residential.construct_floor()


    print(f" Глубина фундамента: {residential.calculate_foundation_depth():.2f}м")


    print("\n" + "=" * 70)
    print(" ПРОЕКТ 2: Бизнес-центр")
    print("-" * 50)

    commercial = CommercialBuilding(
        project_id="C-2024-045",
        name="БЦ 'Плаза'",
        address="г. Санкт-Петербург, пр. Невский, 150",
        budget=500_000_000,
        building_type="Офисный центр",
        floor_area=1200,
        floors_above=12,
        floors_underground=2,
        has_parking=True
    )
    print(commercial)


    commercial.install_security_system("Видеонаблюдение + СКУД", 3_500_000)


    print(f"📐 Глубина фундамента: {commercial.calculate_foundation_depth():.2f}м")


    commercial._status = ConstructionStatus.COMPLETED
    commercial.lease_space("ООО 'Рога и Копыта'", 450, 1200, 12)
    commercial.lease_space("АО 'ТехноИнвест'", 600, 1500, 24)


    # Итоговый отчет
    print("\n" + "=" * 70)
    print("📊 ИТОГОВЫЙ ОТЧЕТ ПО ПРОЕКТАМ")
    print("=" * 70)

    for project in [residential, commercial]:
        print(f"\n{project}")
        summary = project.get_project_summary()
        print(f"   Разрешение: {summary['permit_number']}")
        print(f"   Остаток бюджета: {summary['remaining']:,.0f} руб.")
        print(f"   Материалы: {', '.join(summary['materials'].keys())}")
        print(f"   Рабочих: {summary['workers_count']}")