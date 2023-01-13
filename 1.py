import subprocess
import locale

# ls = ['разработка', 'сокет', 'декоратор']
# for el in ls:
#     print(f"{el} - тип {type(el)}")
#
# ls_1 = [b'class', b'function', b'method']
# for el in ls_1:
#     print(f"{el} - тип {type(el)} - длина {len(el)}")


# ls_3 = ['разработка', 'администрирование', 'protocol', 'standard']
# for el in ls_3:
#     print(f"{el} - тип {type(el)} - длина {len(el)}")
#     temp = el.encode('utf-8')
#     print(f"{temp} - тип {type(temp)} - длина {len(temp)}")
#     temp_1 = temp.decode('utf-8')
#     print(f"{temp_1} - тип {type(temp_1)} - длина {len(temp_1)}")

# args = ['ping', 'yandex.ru']
# subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
# for line in subproc_ping.stdout:
#     line = line.decode('cp866').encode('utf-8')
#     print(line.decode('utf-8'))

def_coding = locale.getpreferredencoding()
print(def_coding)




