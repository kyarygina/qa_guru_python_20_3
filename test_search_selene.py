from selene import browser, have


def test_successful_search(browser_settings):
    browser.open('https://www.startpage.com/')
    browser.element('[id="q"]').type('qa.guru').press_enter()
    browser.element('html').should(have.text('Web results'))


def test_unsuccessful_search(browser_settings):
    browser.open('https://www.startpage.com/')
    browser.element('[id="q"]').type('ergaegrakjnjhwebfjaw3yhya7rgfawbhe`a').press_enter()
    browser.element('html').should(have.text('Uh-oh, there are no results for this search.'))