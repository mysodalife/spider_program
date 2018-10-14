from bs4 import BeautifulSoup
import re

html_str = """
<html>
    <head><title>The Dormouse's story</title></head>
    <body>
      <p class="title tail"><b>The Dormouse's story</b></p><p class="story">Once upon a time there were three little sisters; and their names were
      <a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>
      <a href="http://example.com/lacie" class="sister" id="link2"><!--Lacie--></a> and
      <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
      and they lived at the bottom of a well.
      </p></body>
    <p class="story">...</p>
</html>
"""
soup = BeautifulSoup(html_str, 'lxml')

# # 打印 所有的 html
# print(soup.prettify())
#
# # 获取到 p 的所有 class 属性
# print(soup.p.get('class'))
#
# # 获取到 p 的所有属性
# print(soup.p.attrs)
#
# # 更改 p 的属性
# soup.p['class'] = ['head', 'sd']
# print(soup.p['class'])

# print(soup.p.contents)
# for child in soup.p.children:
#     print(child)
# print('---------')
# for child in soup.p.descendants: # 这里会递归的遍历所有的节点
#     print(child)
# print(soup.head.contents)
# print(soup.head.string) # 坑： 使用 contents 会把换行符也当作其中一个子节点
# print(soup.title.string)
# print(soup.html.string)
# print('------------')
#
# # strings 是为了应对有多个孩子节点的情况
# for string in soup.head.strings:
#     print(repr(string))
# print('*********')
#
# # stripped_strings 可以省去输出的空格和空行
# for string in soup.head.stripped_strings:
#     print(repr(string))
# print('/////////////////')
# # 通过 parent 属性获取到父节点
# print(soup.title.parent)
#
# # 通过 parents 可以获取到所有的父节点
# print('--------------')
# for parent in soup.a.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)
#
# print('-----------------')
# # 通过 next_sibling 或者 prev_sibling  来获取到下一个或者前一个同胞节点
# print(soup.p.next_sibling)
#
# # 通过 next_siblings 或者 prev_siblings 来获取所有的同胞节点
# print('-------------------')
# for sibling in soup.p.next_siblings:
#     print(repr(sibling))

# # 通过 next_element 和 prev_element 来获取当前节点的前一个节点，不论层次关系
# print(repr(soup.head.next_element))
# print(repr(soup.head))

# for element in soup.a.next_elements:
#     print(repr(element))

# 搜索文档树的用法 name 属性可以传入的类型： 标签号 正则表达式 列表 True 方法
# print(soup.find_all('b'))
# print('-----------')
# print(soup.find_all(re.compile(r'^b')))
# print('-----------')
# print(soup.find_all(['a', 'b']))
# print('-----------')
#
#
# def hasClassId(tag):
#     return tag.has_attr('class') and tag.has_attr('id')
#
# for tag in soup.find_all(True):
#     print(tag.name)
#
# print(soup.find_all(hasClassId))

# print(soup.find_all(id='link2'))
# print(soup.find_all(href=re.compile('elsie')))
# print(soup.find_all(id=['link1', 'link2']))
# print(soup.find_all(id=True))
# print(soup.find_all(class_='sister'))
# print(soup.find_all(href = re.compile('elsie'), id='link1'))


# text 参数搜索文档中的内容  字符串 列表 正则表达式 True
# print(soup.find_all(text='Tillie'))
# print(soup.find_all(text=['Tillie', 'Elsie', 'Lacie']))
# print(soup.find_all(text=re.compile("Dormouse")))
#
# # 虽然 text参数被用来查找字符串 但是还是可以用来过滤标签 (string 与 text 相同)
# print(soup.find_all('a', text='Elsie'))
#
# # 调用 find_all 时默认会返回搜索 tag 的所有子节点， 如果只是想搜索直接子节点 那么就把 recursive 设置成 False
# print(soup.find_all('title'))
# print(soup.find_all('title', recursive=False))

# CSS 选择器 通过CSS来选择元素 通过 select 方法 , 返回 list

# 根据标记名称来查找
# print(soup.select('a'))
# print(soup.select('head > title'))
# print(soup.select('p > #link1'))
# print(soup.select('#link1 ~ .sister'))  # ~ 是匹配所有满足条件的同级元素
# print(soup.select('#link1 + .sister'))  # + 是相邻元素选择器  两者具有相同的父元素 同时且只会匹配第一个

# print('---------------')
# # 根据CSS类名来选择
# print(soup.select('.sister'))
# print(soup.select('[class~=sister]')) # ~= 仅仅要求类型部分匹配
#
# print('*****************')
# # 根据是否存在某个属性值来查找
# print(soup.select('a[href]'))

# 根据属性值来选择
print(soup.select('a[href="http://example.com/elsie"]'))
print(soup.select('a[href^="http://example.com/"]'))
print(soup.select('a[href$="tillie"]'))
print(soup.select('a[href*=".com/e"]'))  # 字符串中只要包含 .com/e 就可以成功获取到
