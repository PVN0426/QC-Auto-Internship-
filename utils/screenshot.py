import os
from datetime import datetime


def take_screenshot(driver, test_name):

    screenshot_folder = "results/screenshots"

    os.makedirs(
        screenshot_folder,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    screenshot_path = os.path.join(

        screenshot_folder,

        f"{test_name}_{timestamp}.png"

    )

    driver.save_screenshot(
        screenshot_path
    )

    return screenshot_path