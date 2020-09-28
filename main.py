import pyautogui, time, os

OPENING_TIME = 8  # SECONDS

DEFAULT_NUMBER = 1

def open_boxes(number_of_boxes: int) -> None:
    """
    Opens <number_of_boxes> amount of loot boxes.
    PRECONDITIONS:
                - number_of_boxes >= 1
                - You are on the screen for opening loot boxes
    """
    cur_num = check_num()
    for box_num in range(1, number_of_boxes + 1):
        pyautogui.press('space')
        time.sleep(OPENING_TIME)
        get_num = cur_num + box_num
        loot_pic = pyautogui.screenshot()
        loot_pic.save(f'loot\\{get_num}.png')
    
    with open('current_num.txt', 'w') as f:
        f.write(f"{get_num}")

def check_num() -> int:
    """
    Returns the number of lootboxes that have been opened by this program
    """
    with open('current_num.txt', 'r') as f:
        number = int(list(f)[0])
    return number

if __name__ == '__main__':
    number_of_boxes = int(input("Enter the number of boxes you would like opened:\n"))
    time.sleep(5)
    open_boxes(number_of_boxes)