#  match对象
import re
pattern = re.compile(r'(\w+)  (\w+)  (?P<word>.*)')
match = re.match(pattern, 'I  love  you!')

# the property of match
print(match.string)
print(match.re)
print(match.pos)
print(match.endpos)
print(match.lastindex)  # 被捕获的最后一个分组后号码 编号从1开始
print(match.lastgroup)

# the method of match
print(match.group())  # 默认是编号0 代表整个匹配的子串 这里的组号是从1 开始的
print(match.group(1, 2))
print(match.groups())  # 返回整个字符串所包含的对象
print(match.groupdict())  # 如果没有dict 那么就是没有dict那么就是没有组名
print(match.start(2))     # 返回指定的分组截获的子串在整个字符串中的起始位置
print(match.end(2))       # 返回指定的分组截获的子串在整个字符串中的结束位置
print(match.span(3))
print(match.expand(r'\g<word> \1 \2'))     # 将匹配得到的字符串在得到的子串中返回