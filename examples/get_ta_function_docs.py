import os

from xquantesis import settings
from xquantesis.xno.ta.docs import get_function_docs

if __name__ == "__main__":
    docs = get_function_docs()
    for doc in docs:
        print(f"- {doc.sig}")
