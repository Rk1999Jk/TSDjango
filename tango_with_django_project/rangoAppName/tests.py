


from django.test import TestCase
from unittest.mock import patch
import pandas as pd
from django.urls import reverse

class SummaryViewTest(TestCase):

    @patch('pandas.read_csv')
    def test_summary_view(self, mock_read_csv):
        # Create a mock DataFrame to return
        mock_df = pd.DataFrame({
            'NewsArticleId': [1],
            'PegasusCnn': ['test_pegasus_cnn'],
            'PegasusAdam': ['test_pegasus_adam'],
            'PegasusXsum': ['test_pegasus_xsum'],
            'Golden': ['test_golden']
        })

        # Make the read_csv function return the mock DataFrame
        mock_read_csv.return_value = mock_df

        # Call the view
        response = self.client.get(reverse('summary_view')) # Update this with the correct URL name

        # Check that the response contains the expected data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['data']['NewsArticleId'], 1)
        self.assertEqual(response.context['data']['PegasusCnn'], 'test_pegasus_cnn')
        self.assertEqual(response.context['data']['PegasusAdam'], 'test_pegasus_adam')
        self.assertEqual(response.context['data']['PegasusXsum'], 'test_pegasus_xsum')
        self.assertEqual(response.context['data']['Golden'], 'test_golden')
from rangoAppName.models import DataTable  # import your model

class MyFormViewTest(TestCase):

    def test_post_request_form_valid_user1(self):
        
        # Define the URL and POST data
        url = reverse('rangoAppName:my_view')  
        post_data = {
            'S1M1': 'data',
            'S1M2': 'data',
            'S1M3': 'data',
            'S2M1': 'data',
            'S2M2': 'data',
            'S2M3': 'data',
            # ... (other fields)
            'M1Rank': 'rank1',
            'M2Rank': 'rank2',
            'M3Rank': 'rank3',
        }

        # Simulate the POST request
        response = self.client.post(url, post_data)

        # Check that the form is valid and the data is saved
        self.assertEqual(DataTable.objects.count(), 1)
        self.assertEqual(response.status_code, 302)  # redirect should happen
        self.assertRedirects(response, reverse('rangoAppName:form2_view'))  # check the redirect URL

    def test_get_request(self):
        # Define the URL
        url = reverse('rangoAppName:my_view')  

        # Simulate the GET request
        response = self.client.get(url)

        # Check that the form is displayed
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'form')

