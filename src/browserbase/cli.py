import sys
import subprocess
from typing import List, Optional


def main(args: Optional[List[str]] = None) -> int:
    if args is None:
        args = sys.argv[1:]

    if not args:
        print("Usage: browserbase <command>")
        return 1

    # Execute the command
    try:
        result = subprocess.run(args, check=True)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        return e.returncode
    except FileNotFoundError:
        print(f"Command not found: {args[0]}")
        return 127


if __name__ == "__main__":
    sys.exit(main())
