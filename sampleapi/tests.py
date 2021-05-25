from rest_framework.test import APITestCase
from .models import UuidGenerator
from django.utils import timezone
import uuid
from django.urls import reverse
import pdb



class UuidGeneratorTestCase(APITestCase):
    def setUp(self):
        self.test_uuid=uuid.uuid4()
        self.test_timestamp=timezone.now()  
        self.api_url = reverse('uuid-api')      

    def test_create_model_object(self):
        """test the model objects are created successfully"""
        UuidGenerator.objects.create(uuid=self.test_uuid, timestamp=self.test_timestamp)
        get_created_objects = UuidGenerator.objects.get(uuid=self.test_uuid)
        self.assertEqual(get_created_objects.uuid, self.test_uuid)
        self.assertEqual(get_created_objects.timestamp.date(), self.test_timestamp.date())

    def test_model_object_data_types(self):
        """test key value pair generation"""
        UuidGenerator.objects.create(uuid=self.test_uuid, timestamp=self.test_timestamp)
        get_objects = UuidGenerator.objects.get(uuid=self.test_uuid)
        self.assertEqual(type(get_objects.uuid), uuid.UUID)
        self.assertEqual(type(get_objects.timestamp), type(timezone.now()))
    
    def test_endpoint_status(self):
        """test endpoint status"""
        get_response = self.client.get(self.api_url)
        self.assertEqual(get_response.status_code, 200)  

    def test_key_value_pair_generation(self):
        """test key value pair generation"""
        UuidGenerator.objects.create(uuid=self.test_uuid,
        timestamp=self.test_timestamp)
        get_response_data = self.client.get(self.api_url)
        self.assertEqual(type(get_response_data.data), dict)

    def tearDown(self):
        self.test_uuid = None
        self.test_timestamp = None
        self.api_url = None
