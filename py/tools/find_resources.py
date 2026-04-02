import os
import win32api
import win32con
import pandas as pd

def search_string_in_dll(dll_path, keyword):
    """在 DLL 里查找字符串资源，返回匹配的 (id, text) 列表"""
    matches = []
    try:
        hinst = win32api.LoadLibraryEx(dll_path, 0, win32con.LOAD_LIBRARY_AS_DATAFILE)
    except Exception as e:
        print(f"[错误] 无法加载 {dll_path}: {e}")
        return matches

    try:
        # 常见的字符串资源 ID 一般在 1 - 65535 之间
        for string_id in range(1, 65536):
            try:
                text = win32api.LoadString(hinst, string_id)
                if keyword in text:
                    matches.append((string_id, text))
            except Exception:
                pass
    finally:
        win32api.FreeLibrary(hinst)

    return matches


def search_in_folder(folder, keyword):
    """在文件夹下的所有 DLL 中查找"""
    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(".dll"):
                dll_path = os.path.join(root, file)
                results = search_string_in_dll(dll_path, keyword)
                if results:
                    print(f"\n[发现] {dll_path}")
                    for sid, text in results:
                        print(f"  ID={sid}, 内容={text}")


def dump_string_in_dll(dll_path):
    """导出 DLL 中的所有字符串资源 (id, text)"""
    results = []
    try:
        hinst = win32api.LoadLibraryEx(dll_path, 0, win32con.LOAD_LIBRARY_AS_DATAFILE)
    except Exception as e:
        print(f"[错误] 无法加载 {dll_path}: {e}")
        return results

    try:
        for string_id in range(1, 65536):
            try:
                text = win32api.LoadString(hinst, string_id)
                if text:  # 只记录非空字符串
                    results.append((string_id, text))
            except Exception:
                pass
    finally:
        win32api.FreeLibrary(hinst)

    return results

def dump_string(dll_path, output_file):
    data = dump_string_in_dll(dll_path)

    # 转成 DataFrame
    df = pd.DataFrame(data, columns=["StringID", "Text"])

    # 保存 Excel
    df.to_excel(output_file, index=False)

    print(f"已导出 {len(df)} 条字符串到 {output_file}")


if __name__ == "__main__":
    # search_in_folder(r"D:\Program Files\Autodesk\AutoCAD 2024", "控件") # 搜索 “控件” 出现在哪些 DLL
    dump_string(r"D:\Program Files\Autodesk\AutoCAD 2024\zh-CN\acadres.dll", "acadres_strings.xlsx")
