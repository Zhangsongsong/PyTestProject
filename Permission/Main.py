import os
import sys

# 引入androguard的路径，根据个人存放的位置而定
androguard_module_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'androguard')
if not androguard_module_path in sys.path:
    sys.path.append(androguard_module_path)

from androguard.misc import AnalyzeAPK
from androguard.core.androconf import load_api_specific_resource_module

path = r"/apk"
out_path = r"/out"
files = []
path_list = os.listdir(path)
path_list.sort()
for name in path_list:
    if os.path.isfile(os.path.join(path, name)):
        files.append(name)


def main():
    for apkFile in files:
        file_name = os.path.splitext(apkFile)[0]
        print(apkFile)
        out = AnalyzeAPK(path + '/' + apkFile)
        # apk object 抽象apk对象，可以获取apk的一些信息，如版本号、包名、Activity等
        a = out[0]
        # DalvikVMFormat 数组，一个元素其实对应的是class.dex，可以从DEX文件中获取类、方法或字符串。
        d = out[1]
        # Analysis 分析对象，因为它包含特殊的类，这些类链接有关classes.dex的信息，甚至可以一次处理许多dex文件，所以下面我们从这里面来分析整个apk
        dx = out[2]

        # api和权限映射
        # 输出文件路径
        api_perm_filename = os.path.join(out_path, file_name + "_api-perm.txt")
        api_perm_file = open(api_perm_filename, 'w', encoding='utf-8')
        # 权限映射map
        permissionMap = load_api_specific_resource_module('api_permission_mappings')
        # 遍历apk所有方法
        for meth_analysis in dx.get_methods():
            meth = meth_analysis.get_method()
            # 获取类名、方法名
            name = meth.get_class_name() + "-" + meth.get_name() + "-" + str(
                meth.get_descriptor())

            for k, v in permissionMap.items():
                # 匹配系统权限方法，匹配上就输出到文件中
                if name == k:
                    result = str(meth) + ' : ' + str(v)
                    api_perm_file.write(result + '\n')
        api_perm_file.close()


if __name__ == '__main__':
    main()