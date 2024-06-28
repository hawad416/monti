class Storybook:
    def __init__(self, story_text, comprehension_pauses=None, paths=None):
        self.story_text = story_text  # List of StoryPage objects
        self.comprehension_pauses = comprehension_pauses if comprehension_pauses is not None else []  # List of indices where comprehension questions will appear
        self.paths = paths if paths is not None else []  # List of Storybook objects representing different paths

    def num_pages(self):
        return len(self.story_text)

    def add_path(self, path):
        self.paths.append(path)

    def get_page(self, index):
        return self.story_text[index] if 0 <= index < len(self.story_text) else None

    def is_comprehension_pause(self, index):
        return index in self.comprehension_pauses
