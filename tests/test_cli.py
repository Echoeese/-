# simple smoke test for package import / CLI presence
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))


def test_cli_importable():
    import uniconv.cli as cli

    assert hasattr(cli, 'app')
