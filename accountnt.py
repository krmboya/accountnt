"""Core of the application"""

from collections import namedtuple

# Entities
User = namedtuple('User', ['uid', 'name'])
UserCategory = namedtuple('UserCategory', ['user_id', 'category_id'])


class Category(object):

    def __init__(self, name, uid=None):
        self.uid = uid
        self.name = name

    @staticmethod
    def normalized_name(name):
        """Standardizes category name format"""

        return " ".join(name.split()).title()


# Use Cases
class AddCategoryUsecase(object):

    def __init__(self):
        pass

    def execute(self, category_name, user_id):

        category_name = Category.normalized_name(category_name)
        category, __ = self.category_objects.get_or_create(category_name)

        if self.user_category_objects.exists(
                user_id, category.uid):
            return "You've already added '{}'".format(category.name)

        self.user_category_objects.add(user_id, category.uid)
        return "Category '{}' has been added".format(category.name)
