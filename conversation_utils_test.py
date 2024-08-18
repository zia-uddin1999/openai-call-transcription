import unittest
from unittest.mock import MagicMock, patch
from conversation_utils import generate_call_transcript, summarize_transcript, answer_questions

class TestGenerateCallTranscript(unittest.TestCase):
    def test_generate_call_transcript(self):
        # Arrange
        prompt = "Hello, how can I help you today?"
        output_format = "text"
        language = "English"
        expected_transcript = "Hello, how can I help you today?"

        # Mock the OpenAI client and its response
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content=expected_transcript))]
        mock_client.chat.completions.create.return_value = mock_response

        # Act
        actual_transcript = generate_call_transcript(mock_client, prompt, output_format, language)

        # Assert
        self.assertEqual(actual_transcript, expected_transcript)

    def test_summarize_transcript(self):
        # Arrange
        transcript = "This is a long transcript that needs to be summarized."
        language = "English"
        expected_summary = "This is a summary of the transcript."

        # Mock the OpenAI client and its response
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content=expected_summary))]
        mock_client.chat.completions.create.return_value = mock_response

        # Act
        actual_summary = summarize_transcript(mock_client, transcript, language)

        # Assert
        self.assertEqual(actual_summary, expected_summary)

    # AI-Generated Code
    @patch('builtins.input', side_effect=["What is AI?", "quit"])
    @patch('builtins.print')  # Mock print to suppress output during testing
    def test_answer_questions(self, mock_print, mock_input):
        # Arrange
        conversations = []
        language = "English"
        expected_conversations = [
            {"role": "user", "content": "What is AI?"},
            {"role": "assistant", "content": "AI stands for Artificial Intelligence."}
        ]

        # Mock the OpenAI client and its response
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content="AI stands for Artificial Intelligence."))]
        mock_client.chat.completions.create.return_value = mock_response

        # Act
        actual_conversations = answer_questions(mock_client, conversations, language)

        # Assert
        self.assertEqual(actual_conversations, expected_conversations)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)