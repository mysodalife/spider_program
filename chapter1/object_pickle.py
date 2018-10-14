try:
    import cpickle
except ImportError:
    import pickle
import os
from chapter1.open_file import dir_path

object = dict(url='www.baidu.com', name='sodalife')
try:
    file = open(os.path.join(dir_path, 'pickle.dat'), 'wb')  # 二进制序列化
    s = pickle.dumps(object)
    file.write(s)
finally:
    file.close()
with open(os.path.join(dir_path, 'pickle.dat'), 'rb') as f:
    read_content = pickle.load(f)
print(read_content)
