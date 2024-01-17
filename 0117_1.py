import cv2 as cv

img = cv.imread('images\\i3.png')

imgContour = img.copy() # 複製圖片

# 1 - 轉成灰階 (因為在檢測輪廓上不需要用到顏色)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 2 - 檢測圖片的邊緣 (依狀況調整參數)
canny = cv.Canny(img, 150, 200)

# 3 - 偵測圖片的輪廓
contours, hierarchy = cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE) # (圖片，找外輪廓，不做壓縮)
'''
.findContours
(參數1: 要偵測的圖片
參數2: 要使用的模式，例如找外輪廓、內輪廓，或是內外都要
參數3: 要使用的近似方法，可以壓縮水平或垂直的輪廓點。) 

結果會回傳兩個值
-1 輪廓 
-2 階層 (這邊用不到)
'''

# 4 - 利用 for 迴圈去跑輪廓
for cnt in contours:
    # 4-1 印出輪廓點(這些點連起來就是輪廓)
    #print(cnt) 

    # 4-2 畫出輪廓
    cv.drawContours(imgContour, cnt, -1, (255,0,0), 4)
    '''
    .drawContours
    (參數1: 要畫在什麼圖形上
    參數2: 要畫的輪廓
    參數3: 要畫第幾個輪廓，-1是指全畫
    參數4: 要用什麼顏色畫
    參數5: 畫的線條粗度)
    '''

    # 4-3-1 得到輪廓面積
    #print(cv.contourArea(cnt))
    area = cv.contourArea(cnt)
    '''
    如果看到面積是0，那點可能是個雜訊，直接可以忽略不理
    '''

    # 4-3-2 利用面積大小去過濾圖形
    if (area > 300):

        # 4-4 取得輪廓的邊長 (外框總長)
        #print(cv.arcLength(cnt, True))
        peri = cv.arcLength(cnt, True)
        '''
        .arcLength
        (參數1: 輪廓
        參數2: 填入輪廓是否為閉合，使用布林值)

        如果看到邊長是0，那點可能是個雜訊(噪點)，直接可以忽略不理
        '''

        # 4-5 用多邊形近似輪廓
        vertices = cv.approxPolyDP(cnt, peri*0.02, True)
        #print(len(vertices))
        corners = len(vertices) # 儲存頂點數目
        '''
        .approxPolyDP 會回傳多邊形的頂點，算出來頂點特多的可能就是圓形
        (參數1: 要近似的輪廓
        參數2: 近似值，值越大邊越多，值越小邊越少。值要自行調整到合適的
        參數3: 填入輪廓是否為閉合，使用布林值)
        '''

        # 4-5-1 將圖形用方框框出
        x, y, w, h = cv.boundingRect(vertices)
        '''
        .boundingRect 回傳四個值 -> (左上x，左上y，方框寬，方框高)
        '''

        cv.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 4)
        '''
        .rectangle (要畫的圖片，方框左上座標，方框右下座標，框線顏色，框線粗細)
        '''

        # 4-6 圖形依形狀分類並做標記
        if (corners == 3):
            cv.putText(imgContour, 'triangle', (x, y-5), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif (corners == 4):
            cv.putText(imgContour, 'rectangle', (x, y-5), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif (corners ==5):
            cv.putText(imgContour, 'pentagon', (x, y-5), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            cv.putText(imgContour, 'circle', (x, y-5), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        '''
        .putText (要畫的圖片，要寫的字，字的起始座標，字型，文字大小，字的顏色，文字粗度)
        '''



cv.imshow('img', img)
cv.imshow('canny', canny)
cv.imshow('imgContour', imgContour)
cv.waitKey(0)

cv.imwrite('images\\img0117-1.png',img)
cv.imwrite('images\\img0117-2.png',canny)
cv.imwrite('images\\img0117-3.png',imgContour)
