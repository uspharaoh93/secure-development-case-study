"""Check local Markdown destinations and prohibited artifact names; no network access."""
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


def validate(root):
    root = Path(root).resolve()
    errors = []
    for path in root.rglob('*'):
        relative = path.relative_to(root)
        if any(part in {'.git', '__pycache__', '.venv'} for part in relative.parts):
            continue
        if not path.is_file():
            continue
        if (path.name.startswith('.env') or path.name == 'credentials.json'
                or path.suffix in {'.sqlite3', '.db', '.pem', '.key'}):
            errors.append(f'{relative}: prohibited local artifact')
        if path.suffix != '.md':
            continue
        content = path.read_text(encoding='utf-8')
        for destination in re.findall(r'\]\(([^)]+)\)', content):
            destination = destination.strip().strip('<>')
            if not destination or destination.startswith('#'):
                continue
            link = urlsplit(destination)
            if link.scheme in {'https', 'http', 'mailto'}:
                continue
            if link.scheme or destination.startswith('/'):
                errors.append(f'{relative}: nonportable link {destination}')
                continue
            target = (path.parent / unquote(link.path)).resolve()
            if not target.is_relative_to(root) or not target.exists():
                errors.append(f'{relative}: missing or escaping link {destination}')
    return errors


if __name__ == '__main__':
    issues = validate(Path(__file__).resolve().parent.parent)
    for issue in issues:
        print(issue)
    if issues:
        raise SystemExit(1)
    print('Documentation checks passed: local links and prohibited artifact names.')
