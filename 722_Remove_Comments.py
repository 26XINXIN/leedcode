class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        block = False
        new_source = list()
        for line in source:
            if not block:
                try:
                    line_comment_idx = line.index('//')
                except:
                    line_comment_idx = -1
                try:
                    block_comment_idx = line.index('/*')
                except:
                    block_comment_idx = -1
                if line_comment_idx == -1 and block_comment_idx == -1:
                    new_source.append(line)
                elif line_comment_idx == -1:
                    try:
                        end_block_idx = line.index('*/')
                    except:
                        end_block_idx = -1
                    if end_block_idx == -1 or end_block_idx < block_comment_idx + 2:
                        block = True
                        new_source.append(line[:block_comment_idx])
                    else:
                        new_source.append(line[:block_comment_idx] + line[end_block_idx + 2 :])
                elif block_comment_idx == -1:
                    new_source.append(line[:line_comment_idx])
                else:
                    if line_comment_idx < block_comment_idx:
                        new_source.append(line[:line_comment_idx])
                    else:
                        block = True
                        new_source.append(line[:block_comment_idx])
            else:
                try:
                    block_comment_idx = line.index('*/')
                except:
                    block_comment_idx = -1
                if block_comment_idx == -1:
                    continue
                else:
                    block = False
                    new_source[-1] += line[block_comment_idx + 2 :]
        
        return list(filter(lambda x: len(x) > 0, new_source))
        