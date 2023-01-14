
def main():
    fileObj = open('video_clip.txt', 'r')
    
    clip_counter = 0
    all_len_clip = 0

    for line in fileObj:
        clip_counter += 1
        line = line.rstrip('\n')
        print(f'videoclip {clip_counter} : {line}')
        all_len_clip += float(line)
        
    print('len all clips = ', all_len_clip)


main()