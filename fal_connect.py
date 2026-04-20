"""Minimal fal.ai connectivity check.

Reads FAL_KEY from the environment (loaded from .env) and submits a small
request to verify the credentials work end-to-end.
"""

import os
import sys

from dotenv import load_dotenv

load_dotenv()

if not os.getenv("FAL_KEY"):
    sys.exit("FAL_KEY is not set. Copy .env.example to .env and fill it in.")

import fal_client


def main() -> None:
    result = fal_client.subscribe(
        "fal-ai/fast-sdxl",
        arguments={"prompt": "a friendly rabbit waving hello, digital art"},
        with_logs=False,
    )
    images = result.get("images", [])
    if not images:
        sys.exit(f"No image returned. Raw response: {result!r}")
    print("Connected to fal.ai successfully.")
    print("Image URL:", images[0]["url"])


if __name__ == "__main__":
    main()
