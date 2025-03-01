import google.generativeai as genai
from ..config import GEMINI_API_KEY

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)

class AIService:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')

    async def generate_response(self, topic: str, query: str) -> str:
        """Generate a response using Gemini based on the topic and query."""
        prompt = self._create_prompt(topic, query)
        
        try:
            response = await self.model.generate_content_async(prompt)
            return response.text
        except Exception as e:
            print(f"Error generating response: {e}")
            return "I'm sorry, I couldn't generate a response at the moment. Please try again later."

    def _create_prompt(self, topic: str, query: str) -> str:
        """Create a prompt based on the topic."""
        prompts = {
            "feng_shui": (
                f"You are a Feng Shui expert. Please provide helpful, accurate advice about Feng Shui "
                f"in response to this query: {query}"
            ),
            "mbti": (
                f"You are an MBTI personality type expert. Please provide helpful, accurate information "
                f"about MBTI personality types in response to this query: {query}"
            ),
            "mythology": (
                f"You are a mythology expert. Please provide helpful, accurate information about "
                f"mythology from various cultures in response to this query: {query}"
            ),
        }
        
        return prompts.get(topic, f"Please respond to this query: {query}")