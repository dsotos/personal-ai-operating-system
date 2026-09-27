#!/usr/bin/env python3
"""Basic public-repository safety checks.

This is intentionally conservative. It is not a replacement for a secret scanner.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP = {'.git', '.DS_Store'}
PATTERNS = {
    'private home path': re.compile(r'/Users/[^/]+|/home/[^/]+'),
    'generic secret assignment': re.compile(r'(?i)(api[_-]?key|token|password|secret)\s*[:=]\s*["\']?[^\s"\']{12,}'),
    'private phone-like identifier': re.compile(r'(?<!\d)\+?\d[\d ()-]{8,}\d(?!\d)'),
}

errors = []
for path in ROOT.rglob('*'):
    if not path.is_file() or path.name == Path(__file__).name or any(part in SKIP for part in path.parts):
        continue
    try:
        text = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        continue
    for label, pattern in PATTERNS.items():
        if pattern.search(text):
            errors.append(f'{label}: {path.relative_to(ROOT)}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('public safety checks: passed')
