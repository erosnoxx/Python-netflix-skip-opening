import cv2
import numpy as np, os
import pyautogui, time


class TemplateMatcher:
    @staticmethod
    def find_template_on_screen(template_path: str) -> tuple[int, int]:
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Template image não encontrado no caminho: {template_path}")

        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        if template is None:
            raise FileNotFoundError(f"Erro ao carregar a imagem no caminho: {template_path}")

        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
        
        template_w, template_h = template.shape[::-1]
        gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= 0.8)
        
        if not loc[0].size > 0:
            return None

        pt = (loc[1][0], loc[0][0])
        return (pt[0] + template_w // 2, pt[1] + template_h // 2)
    
    @staticmethod
    def locate_and_click(template_path: str, offset_x: int=0, offset_y: int=0) -> None:
        location = TemplateMatcher.find_template_on_screen(template_path)
        if not location:
            raise FileNotFoundError(f"Template {template_path} não encontrado na tela.")
        
        click_x = location[0] + offset_x
        click_y = location[1] + offset_y
        pyautogui.click(click_x, click_y)

    @staticmethod
    def locate_click_write(template_path: str, text: str, offset_x: int=0, offset_y: int=0) -> None:
        try:
            TemplateMatcher.locate_and_click(template_path, offset_x, offset_y)
            pyautogui.write(text)
        except FileNotFoundError as e:
            raise FileNotFoundError(str(e))
        
    @staticmethod
    def wait_for_image(image_path: str) -> None:
        try:
            while True:
                if TemplateMatcher.find_template_on_screen(image_path) is not None:
                    break

                time.sleep(1)

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error waiting for image: {e}")
