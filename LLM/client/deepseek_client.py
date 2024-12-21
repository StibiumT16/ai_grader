import requests
import json
from .base_client import BaseClient
from openai import OpenAI
from typing import List, Dict, Optional, Union

class DeepSeekClient(BaseClient):
    def __init__(self, api_key : str, model: str):
        self.api_key = api_key
        self.model = model
        self.url = 'https://api.deepseek.com/v1'
        
    def send_request(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.0,
        max_tokens: float = 2048,
        **kwargs,
    ):
        
        openai_client = OpenAI(api_key=self.api_key, base_url=self.url )
        
        response = openai_client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs,
        )
        
        return response.choices[0].message.content