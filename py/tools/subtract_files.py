import sys
import os

def subtract_files(exclude_file, source_file, output_file):
    if not os.path.exists(exclude_file):
        print(f"File not found: {exclude_file}")
        return
    if not os.path.exists(source_file):
        print(f"File not found: {source_file}")
        return

    with open(exclude_file, 'r', encoding='utf-8') as f:
        remove_set = set(line.strip() for line in f if line.strip())

    deleted_count = 0
    kept_count = 0
    with open(source_file, 'r', encoding='utf-8') as fin, \
         open(output_file, 'w', encoding='utf-8') as fout:
        for line in fin:
            strriped_line = line.strip()
            if strriped_line in remove_set:
                deleted_count += 1
                continue
            fout.write(line)
            if strriped_line:
                kept_count += 1

    print(f"Completed! Result saved to {output_file}.")
    print(f"Lines deleted: {deleted_count}")
    print(f"Lines kept(valid): {kept_count}")


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python subtract_files.py exclude_file source_file output_file')
    else:
        subtract_files(sys.argv[1], sys.argv[2], sys.argv[3])