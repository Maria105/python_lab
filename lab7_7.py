
#!/usr/bin/env python3
# -*- codding:utf-8 -*-

import re

def camel_case(lines: str) -> str:
    """convert from SnakeCase to camel_case"""

    words = lines.split('_')
    camel = words[0]
    camel += ''.join(list(map(str.capitalize, words[1:])))

    return camel

def snakeCase(text: str) -> str:
    """Convert from camel_case to SnakeCase"""

    words = re.sub(r'([A-Z])', r" \1", text).split()
    snake = '_'.join(list(map(str.lower, words)))

    return snake

print(camel_case(input('enter text in camel_case: ')))
print(snakeCase(input('enter text in SnakeCase: ')))


