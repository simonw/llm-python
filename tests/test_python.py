from llm.cli import cli
from click.testing import CliRunner
import tempfile


def test_python_execute(tmpdir):
    runner = CliRunner()

    # tmpdir should be empty
    assert len(tmpdir.listdir()) == 0

    filepath = tmpdir / "test.txt"

    result = runner.invoke(
        cli, ["python", "-c", f"open('{filepath}', 'w').write('Hello World!')"]
    )

    assert result.exit_code == 0
    assert len(tmpdir.listdir()) == 1
    assert filepath.read() == "Hello World!"
