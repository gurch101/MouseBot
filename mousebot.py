import time
import win32api
import win32con
	
def left_click(x=0, y=0):
	set_mouse_position(x, y)
	left_press()
	time.sleep(.1)
	left_release()

def right_click(x=0, y=0):
	set_mouse_position(x, y)
	right_press()
	time.sleep(.1)
	right_release()	
	
def drag_and_drop(drag_x=0, drag_y=0, drop_x=0, drop_y=0):
	set_mouse_position(drag_x, drag_y)
	left_press()
	time.sleep(.15)
	set_mouse_position(drop_x, drop_y)
	left_release()
	
def left_press():
	__trigger_mouse_event(win32con.MOUSEEVENTF_LEFTDOWN)
	
def left_release():
	__trigger_mouse_event(win32con.MOUSEEVENTF_LEFTUP)

def right_press():
	__trigger_mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN)
	
def right_release():
	__trigger_mouse_event(win32con.MOUSEEVENTF_RIGHTUP)
	
def set_mouse_position(x, y):
	win32api.SetCursorPos((x,y))

def get_mouse_position():
	return win32api.GetCursorPos()
	
def __trigger_mouse_event(mouse_event_type):
	win32api.mouse_event(mouse_event_type,0,0)