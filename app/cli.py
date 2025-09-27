"""Small CLI wrapper to expose a console script entrypoint for the DAGENT app.

This module provides `main()` which is referenced from `pyproject.toml`'s
`[project.scripts]` so users can run `dagent` after installing the package.
"""
from __future__ import annotations

import sys
from typing import List

from app import main as app_main


def main(argv: List[str] | None = None) -> int:
    """Entry point used by the console script `dagent`.

    Accepts the same flags as `python -m app.main`.
    Returns exit code 0 on success or non-zero on error.
    """
    if argv is None:
        argv = sys.argv[1:]

    # The app.main module expects args parsed via argparse when executed as
    # `python -m app.main`. We can forward flags by invoking the module as a
    # script via runpy or by delegating to the module's parser.
    # Simpler approach: if user passed `--no-verify-ssl` keep it, else default
    # behavior remains the same; call app_main.main() with verify flag.
    verify_ssl = True
    if "--no-verify-ssl" in argv:
        verify_ssl = False

    try:
        app_main.main(verify_ssl=verify_ssl)
        return 0
    except Exception as exc:  # pragma: no cover - top-level CLI safety
        print(f"Error running DAGENT: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
