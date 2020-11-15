"""
This module contains step definitions for web.feature.
It uses Selenium WebDriver for browser interactions:
https://www.seleniumhq.org/projects/webdriver/
Setup and cleanup are handled using hooks.
For a real test automation project,
use Page Object Model or Screenplay Pattern to model web interactions.

Prerequisites:
 - Chrome must be installed.
 - chromedriver must be installed and accessible on the system path.
"""

import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver

# Constants

DUCKDUCKGO_HOME = 'https://duckduckgo.com/'


# Scenarios

scenarios('../features/web.feature')


# Fixtures

@pytest.fixture
def browser():
  # Initialize the ChromeDriver instance
  b = selenium.webdriver.Chrome()

  # Make its calls wait up to 10 seconds for elements to appear
  b.implicitly_wait(10)

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()


# Given Steps

@given('the DuckDuckGo home page is displayed')
def ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)


# When Steps

@when(parsers.parse('the user searches for "{text}"'))
def search_phrase(browser, text):
    search_input = browser.find_element_by_name('q')
    search_input.send_keys(text + Keys.RETURN)


# Then Steps

@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    # Check search result list
    # (A more comprehensive test would check results for matching phrases)
    # (Check the list before the search phrase for correct implicit waiting)
    links_div = browser.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    # Check search phrase
    search_input = browser.find_element_by_name('q')
    assert search_input.get_attribute('value') == phrase
