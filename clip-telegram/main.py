import os
import re

# 匹配标题行（#后跟空格）
header_pattern = re.compile(r'^(#+)(\s+)(.*)$')
# 匹配需要转义的#（前面没有反斜杠）
escape_pattern = re.compile(r'(?<!\\)#')

def process_line(line):
    # 分离内容和换行符
    content = line.rstrip('\r\n')
    line_ending = line[len(content):] if len(line) > len(content) else ''

    # 检查标题行
    header_match = header_pattern.match(content)
    if header_match:
        # 处理标题行内容部分
        parts = header_match.groups()
        processed_content = escape_pattern.sub(r'\\#', parts[2])
        return f"{parts[0]}{parts[1]}{processed_content}{line_ending}"

    # 处理普通行
    processed_content = escape_pattern.sub(r'\\#', content)
    return f"{processed_content}{line_ending}"

def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    processed = [process_line(line) for line in lines]

    with open(filename, 'w', encoding='utf-8', newline='') as f:
        f.writelines(processed)

if __name__ == "__main__":
    for item in os.listdir('.'):
        if os.path.isfile(item) and item != os.path.basename(__file__):
            try:
                process_file(item)
                print(f"Processed: {item}")
            except Exception as e:
                print(f"Error processing {item}: {str(e)}")