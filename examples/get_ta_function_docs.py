import os

from xno_sdk import settings
from xno_sdk.xno.ta.docs import get_function_docs

if __name__ == "__main__":
    docs = get_function_docs()
    for doc in docs:
        print(f"- {doc.sig}")
