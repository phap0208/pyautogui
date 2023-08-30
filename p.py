import pyautogui
import time
coor = pyautogui.locateOnScreen('1.png', grayscale=True, confidence=0.9)
coor_center = pyautogui.center(coor)
print(coor_center)
pyautogui.click((coor_center.x),(coor_center.y))
time.sleep(5)
coor = pyautogui.locateOnScreen('2.png',grayscale=True, confidence=0.9)
coor_center = pyautogui.center(coor)
print(coor_center)
pyautogui.click((coor_center.x)+50,(coor_center.y))
pyautogui.typewrite("facebook.com")
pyautogui.press('enter')
time.sleep(3)
create_post_button = pyautogui.locateOnScreen('3.png', grayscale=True, confidence=0.9)
if create_post_button:
    create_post_center = pyautogui.center(create_post_button)
    pyautogui.click(create_post_center.x, create_post_center.y)
    time.sleep(3)

    # Đợi một lúc để cửa sổ tạo bài viết mở lên
    # Tiến hành nhập nội dung bài viết
    pyautogui.write("ok ok ")

    # Đăng bài viết
    post_button = pyautogui.locateOnScreen('4.png', grayscale=True, confidence=0.9)
    if post_button:
        post_button_center = pyautogui.center(post_button)
        pyautogui.click((post_button_center.x)+70, (post_button_center.y))
        time.sleep(3)
        pyautogui.press('enter')
    else:
        print("Không tìm thấy nút Đăng bài")
else:
    print("Không tìm thấy nút Tạo bài viết")
