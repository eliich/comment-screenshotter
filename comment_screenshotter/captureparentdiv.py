import time
class PlaywrightScraper:
    def __init__(self, page, timeout=60, scroll_delay=2):
        self.page = page
        self.timeout = timeout
        self.scroll_delay = scroll_delay

    def search_text_and_screenshot(self, text_to_find):
        start_time = time.time()
        screenshots_taken = 0

        while time.time() - start_time < self.timeout:
            self.page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(self.scroll_delay)

            text_elements = self.page.locator(f'text="{text_to_find}"')
            element_count = text_elements.count()

            if element_count > 0:
                for i in range(element_count):
                    # Locate the specific ancestor div with the given class
                    ancestor_div = text_elements.nth(i).evaluate_handle("""
                        element => {
                            while (element && !element.classList.contains('tiktok-1i7ohvi-DivCommentItemContainer') && !element.classList.contains('eo72wou0')) {
                                element = element.parentElement;
                            }
                            return element;
                        }
                    """)

                    # Take a screenshot of the ancestor div
                    screenshot_path = f'text-element-screenshot-{screenshots_taken}.png'
                    if ancestor_div:
                        ancestor_div.screenshot(path=screenshot_path)
                        screenshots_taken += 1

                return True  # Return True if at least one element was found and screenshot taken

        return False  # Return False if no elements were found within the timeout period
