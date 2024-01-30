from django.core.management import BaseCommand

from main_app.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        students_list = [
            {'last_name': 'Иванов', 'first_name': 'Семен'},
            {'last_name': 'Петров', 'first_name': 'Александр'},
            {'last_name': 'Сергеев', 'first_name': 'Дмитрий'},
            {'last_name': 'Дмитриев', 'first_name': 'Сергей'},
            {'last_name': 'Александров', 'first_name': 'Петр'},
            {'last_name': 'Семенов', 'first_name': 'Иван'}
        ]

        """Для маленького списка"""
        # for student in students_list:
        #     Student.objects.create(**student)

        """Если данных много - пакетное добавление"""
        students_for_create = []   #  пакет, который будем добавлять
        for student in students_list:
            students_for_create.append(Student(**student))
        """до вызава команды через консоль данные будут находиться в оперативной памяти
        (при создании экземпляра класса не обращаемся к менеджеру объекта и не
        вызываем метод create)"""

        Student.objects.bulk_create(students_for_create)

        # # Очистка таблицы Student
        # Student.objects.all().delete()
        #
        #
        # # Сброс автоинкремента для поля `pk` в таблице Category
        # with connection.cursor() as cursor:
        #     cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1")
        #
        # # Сброс автоинкремента для поля `pk` в таблице Product
        # with connection.cursor() as cursor:
        #     cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1")