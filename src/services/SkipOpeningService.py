from src.utils.TemplateMatcherUtils import TemplateMatcher


class NetflixService:
    def __init__(self):
        self.template_matcher = TemplateMatcher

    def skip(self, template_path: str) -> bool:
        self.template_matcher.locate_and_click(template_path=template_path)
