import re
s = 'i  say, hello  world!'
p = re.compile(r'(\w+)  (\w+)')
print(re.subn(p, r'\2  \1', s))


def func(m):
    return m.group(2).title() + '  ' + m.group(1).title()


print(re.subn(p, func, s))
