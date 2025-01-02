from .client import *

class APILLM:
    def __init__(self, api_key=None, api_secret=None, platform="proxy", model="gpt-4"):
        self.api_key = api_key
        self.api_secret = api_secret
        self.platform = platform
        self.model = model
        if self.model== "wenxin":
            self.platform="wenxin"
            self.api_key= "JWXGr1DMcAz4yGPzPtdqHs4G"
            self.api_secret="4J4sAHLH4H6VmyTu3PbGNeqIN8uqqF9Y"
            self.model = "ERNIE-Speed-128K"
        elif 'deepseek' in self.model:
            self.platform = 'deepseek'
            self.api_key = "sk-00f9993881e148b9a9b1773f95231a6c"
        self.client = self._initialize_client()

    def _initialize_client(self):
        if self.platform == "openai":
            return OpenAIClient(self.api_key, self.model)
        elif self.platform == "wenxin":
            return WenxinClient(self.api_key, self.api_secret, self.model)
        elif self.platform == "zhipuai":
            return ZhipuAIClient(self.api_key, self.model)
        elif self.platform == "proxy":
            return ProxyClient(self.model)
        elif self.platform == 'deepseek':
            return DeepSeekClient(self.api_key, self.model)
        else:
            raise ValueError(f"Unsupported platform: {self.platform}")

    def generate(self, instruction, prompt, history=[], *args, **kwargs):
        if instruction is None:
            instruction = "You are a helpful assistant."

        messages = [{"role": "system", "content": instruction}]
        messages.extend(history)
        messages.append({"role": "user", "content": prompt})
        
        return self.client.send_request(messages, *args, **kwargs)
