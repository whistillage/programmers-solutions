def solution(wallpaper):
    answer = []
    
    lux, luy, rdx, rdy = 100, -1, -1, -1
    
    row_num = len(wallpaper)
    col_num = len(wallpaper[0])
    
    for row_idx in range(row_num):
        item_exists = False
        
        for col_idx in range(col_num):
            if wallpaper[row_idx][col_idx] == '#':
                item_exists = True
                if col_idx < lux:
                    lux = col_idx
                if col_idx + 1 > rdx:
                    rdx = col_idx + 1
                    
        if item_exists == True:
            if luy < 0:
                luy = row_idx
            rdy = row_idx + 1
            
    answer = [luy, lux, rdy, rdx]
    return answer