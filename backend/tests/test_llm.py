from app.utils.llm_client import LLMClient

llm = LLMClient()

response = llm.generate(
    prompt="""
Return JSON only.

{
    "message": "..."
}
""",
    content="Hello!"
)

print(response)