from django.test import TestCase

from posts.models import EventPost
from posts.repository.smoladmin import SmoladminRepository, CategoryCardItem


class SmoladminRepositoryTestCase(TestCase):
    repository: SmoladminRepository = SmoladminRepository()

    # def test_get_sub_categories(self):
    #     response = self.repository.get_all_subcategories_card()
    #     # print(response)
    #
    # def test_get_items(self):
    #     response = self.repository._get_items(CategoryCardItem("asd", 'sdsd', 'https://www.smoladmin.ru/o-smolenske/turizm/obekty-obschestvennogo-pitaniya/restorany/'))
    #     print(response)
    #     EventPost.objects.bulk_create(response)
    #
    #     print(EventPost.objects.all())


    def test_get_all_items(self):
        response = self.repository.get_subcategories()
        items = []
        for i in response:
            print(f"Parse {i}...")
            items += self.repository.get_items_from_subcategory(i)

        print(len(items))
        EventPost.objects.bulk_create(items)
        print(EventPost.objects.all())
        print(EventPost.objects.count())


