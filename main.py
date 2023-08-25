
from czapi.api import LinescorePage

def generate_page()->None:

    page = LinescorePage(cz_event_id=5000,cz_draw_id=1)

    print(page.generate_scraped_boxscores())


if __name__ == '__main__':
    generate_page()