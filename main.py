from src.services.SkipOpeningService import TemplateMatcher

image_path = 'assets/netflix-skip-opening.png'

while True:
    TemplateMatcher.wait_for_image(image_path=image_path)
    TemplateMatcher.locate_and_click(template_path=image_path)
