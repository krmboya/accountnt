"""Core of the application"""

from collections import namedtuple

# Entities
User = namedtuple('User', ['id', 'name'])
Category = namedtuple('Category', ['name'])
UserCategory = namedtuple('UserCategory', ['user_id', 'categories'])


# Use Cases
class CategoryUsecase(object):
    def add_category(self, name, user_id):

        if not self.category_objects.exists(name):
            category = self.category_objects.add(name)

        user_categories = self.user_category_objects.get(user_id)
        user_categories.categories.append(category)

        # todo: check existing user categories
