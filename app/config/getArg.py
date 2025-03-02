import os


# 从环境变量获取 CORS配置, API 密钥、地址以及模型名称
ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS", "*")

IS_ORIGIN_REASONING = os.getenv("IS_ORIGIN_REASONING", "True").lower() == "true"

# DeepSeek 模型参数
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = os.getenv(
    "DEEPSEEK_API_URL", "https://api.deepseek.com/v1/chat/completions"
)
DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-reasoner")
DEEPSEEK_MAX_TOKENS = int(os.getenv("DEEPSEEK_MAX_TOKENS", 8192))
DEEPSEEK_TOP_P = float(os.getenv("DEEPSEEK_TOP_P", 1))
DEEPSEEK_TEMPERATURE = float(os.getenv("DEEPSEEK_TEMPERATURE", 1))

# Claude 模型参数
CLAUDE_MAX_TOKENS = int(os.getenv("CLAUDE_MAX_TOKENS", 199900))
CLAUDE_TOP_P = float(os.getenv("CLAUDE_TOP_P", 1))
CLAUDE_TEMPERATURE = float(os.getenv("CLAUDE_TEMPERATURE", 1))
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
ENV_CLAUDE_MODEL = os.getenv("CLAUDE_MODEL")
CLAUDE_PROVIDER = os.getenv(
    "CLAUDE_PROVIDER", "anthropic"
)  # Claude模型提供商, 默认为anthropic
CLAUDE_API_URL = os.getenv("CLAUDE_API_URL", "https://api.anthropic.com/v1/messages")

# OpenAI Composite
OPENAI_COMPOSITE_MAX_TOKENS = int(os.getenv("OPENAI_COMPOSITE_MAX_TOKENS", 8192))
OPENAI_COMPOSITE_TOP_P = float(os.getenv("OPENAI_COMPOSITE_TOP_P", 1))
OPENAI_COMPOSITE_TEMPERATURE = float(os.getenv("OPENAI_COMPOSITE_TEMPERATURE", 1))
OPENAI_COMPOSITE_API_KEY = os.getenv("OPENAI_COMPOSITE_API_KEY")
OPENAI_COMPOSITE_API_URL = os.getenv("OPENAI_COMPOSITE_API_URL")
OPENAI_COMPOSITE_MODEL = os.getenv("OPENAI_COMPOSITE_MODEL")
