from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait

wa_url = "https://www.wolframalpha.com/widgets/view.jsp?id=87f689e302f4424451632785e8b63e16"

with open("day13.in") as f:
    lines = f.readlines()
    earliest_timestamp = int(lines[0].strip())
    ids = []
    for c in lines[1].strip().split(','):
        try:
            ids.append(int(c))
        except ValueError:
            ids.append(None)

bus_offsets = [(bus, index) for index, bus in enumerate(ids) if bus is not None]
equations = []
for b, o in bus_offsets:
    equations.append(f"(x+{o}) mod {b} = 0")

opts = Options()
opts.headless = True
with Firefox(options=opts) as browser:
    browser.get(wa_url)
    form = browser.find_element_by_id("wolframAlphaWidgetForm119922")
    inputs = form.find_elements_by_tag_name("input")
    for inp, equation in zip(inputs, equations):
        inp.send_keys(equation)
    submit_btn = form.find_element_by_class_name("submit")
    submit_btn.click()

    result_iframe = browser.find_element_by_id("wolframAlphaWidgetResults119922")
    browser.switch_to.frame(result_iframe)
    # wait for the result to load
    WebDriverWait(browser, 30).until(lambda x: x.find_element_by_class_name("pod"))
    result_imgs = browser.find_elements_by_tag_name("img")
    for result_img in result_imgs:
        alt_text = result_img.get_attribute("alt")
        if alt_text.startswith("x = "):
            eqn = alt_text.split(",")[0]
            number = eqn.split(" + ")[1]
            print(number)
            break
