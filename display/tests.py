from django.db.models import F
from django.test import TestCase

from .models import Cache

EXPECTED_CACHE_ID: int = 7919

# Create your tests here.
class CacheModelTests(TestCase):
    def setUp(self):
        print('\nSetup for CacheModelTests')
        # Start each test with an empty Cache
        print(f'Inserting the pk={EXPECTED_CACHE_ID} Cache...')
        cache = Cache(id=EXPECTED_CACHE_ID, quarters=0)
        cache.save()

    def tearDown(self):
        print('\nTear Down for CacheModelTests')
        try:
            # Try to retrieve what's in the cache
            cache = Cache.objects.get(pk=EXPECTED_CACHE_ID)
            cache.delete()
            print(f'Deleted the pk={EXPECTED_CACHE_ID} Cache!')
        except Cache.DoesNotExist:
            pass

    def test_when_get_cache_with_invalid_pk_expect_cache_is_none(self):
        # Arrange
        INVALID_PK: int = -1
        class_under_test: Cache = None

        # Act
        try:
            # Try to retrieve what's in the cache
            class_under_test = Cache.objects.get(pk=INVALID_PK)
        except Cache.DoesNotExist:
            pass
        else:
            self.fail(f'No expected exception was raised.')

        # Assert
        self.assertIsNone(class_under_test)

    def test_when_get_cache_has_0_expect_cache_returns_0(self):
        # Arrange
        class_under_test = Cache.objects.get(pk=EXPECTED_CACHE_ID)

        # Act
        actual = class_under_test.quarters

        # Assert
        self.assertEqual(actual, 0)

    def test_when_get_cache_has_37_expect_cache_returns_37(self):
        # Arrange
        cache = Cache.objects.get(pk=EXPECTED_CACHE_ID)
        cache.quarters = F('quarters') + 37
        cache.save()

        class_under_test = Cache.objects.get(pk=EXPECTED_CACHE_ID)

        # Act
        actual = class_under_test.quarters

        # Assert
        self.assertEqual(actual, 37)


class HomeViewTests(TestCase):

    def test_home_view_when_load_expect_template_is_index_html(self):
        # Act
        response = self.client.get('/', follow=True)

        # Assert
        self.assertTemplateUsed(response, 'index.html')


class CoinReturnViewTests(TestCase):
    def setUp(self):
        print('\nSetup for CoinReturnViewTests')
        # Start each test with an empty Cache
        print(f'Inserting the pk={EXPECTED_CACHE_ID} Cache...')
        cache = Cache(id=EXPECTED_CACHE_ID, quarters=0)
        cache.save()

    def test_coin_return_when_load_expect_template_is_index_html(self):
        # Act
        response = self.client.get('/return', follow=True)

        # Assert
        self.assertTemplateUsed(response, 'return.html')
