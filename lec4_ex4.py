def clean_lyric(lyric):
    lines = lyric.split("\n")
    
    for line in lines:
        new_line = []
        for char in line:
            if char not in string.punctuation and not char.isdigit():
                new_line.append(char)
        print("".join(new_line))
lyric = '''Ngư60ời 'theo hư@ơng' hoa 100mây mù [giăng lối]
Làn 25 sương khó30i phôi phai 90 đưa bư$ớc ai xa rồi 35
100Đơn c#ôi m99ình ta {vấn vương} hồi ức tro^ng ... men say (chiều mưa) buồ80n 
Ng~ăn "giọt lệ" ngừng k2hiến khoé mi sầu bi.1 
'''
clean_lyric(lyric)