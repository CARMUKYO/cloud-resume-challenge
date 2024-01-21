import unittest
from app import lambda_handler

class TestLambdaHandler(unittest.TestCase):

    def test_lambda_handler_success(self):

        result = lambda_handler({}, {})

        expected_result = {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "http://carmukyo-resume-website.s3-website-ap-southeast-2.amazonaws.com",
                "Access-Control-Allow-Methods": "*",
                "Access-Control-Allow-Headers": "*"
            },
        }

        result.pop("body", None)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
