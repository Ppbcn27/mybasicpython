tilecolor={'red':100,'gold':200,'white':90}
print('---โปรแกรมคำนวณกระเบื้อง---')
try:
    tiles = int(input('คุณต้องการปูกระเบื้องทั้งหมดกี่แผ่น: '))
    row = int(input('1 แถวต้องปูกระเบื้อง: ')) # 3 pieces per row
    color = input('กระเบื้องสีอะไร? [red / gold / white]: ')
except:
    print('กรุณากรอกเป็นตัวเลขเท่านั้น!')
    tiles = int(input('คุณต้องการปูกระเบื้องทั้งหมดกี่แผ่น: '))
    row = int(input('1 แถวต้องปูกระเบื้อง: '))
    color = input('กระเบื้องสีอะไร? [red / gold / white]: ')
    
print('--calculate---')

total_row = tiles // row
remain_tiles = tiles % row
print(total_row,remain_tiles)

buy_more = row - remain_tiles

print(f'There are: {tiles} tiles')
print(f'1 row uses: {row} tiles')
print('---calculate---')
print('Client have to use {} rows'.format(total_row))
print('เหลือกระเบื้องที่ยังไม่ได้ปูเต็มแถว {} แผ่น'.format(remain_tiles))
print('Client have to buy more {} tiles'.format(buy_more))
print('total price: {} baht'.format(buy_more * tilecolor[color]))
# How many tiles does the client have to buy more?
