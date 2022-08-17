from functions.search import writeText, searchNclick, search, cleartext
from start import driver
from pages.startpage import stlinks
from pages.register import reglinks
from pages.created import crelinks
from pages.menu import menulinks
from pages.desktops import desklink
from pages.laptops import laplinks
from pages.macbookpro import maclinks
from pages.cart import cartlinks
import functions.prtSc as scr
import functions.generalfunc as gf
import time
from selenium.webdriver.common.action_chains import ActionChains

driver.get('http://tutorialsninja.com/demo/')
driver.maximize_window()

"""
searchNclick(stlinks.get('myAccount'))
gf.checkElement(stlinks.get('linkToRegister'))
searchNclick(stlinks.get('linkToRegister'))

writeText(reglinks.get('firstName'), 'Nik')
writeText(reglinks.get('lastName'), 'Koshkin')
writeText(reglinks.get('email'), 'dla-c@yandex.ru')
writeText(reglinks.get('phone'), '+79025648971')
writeText(reglinks.get('password'), '!QAZxsw2')
writeText(reglinks.get('password2'), '!QAZxsw2')

searchNclick(reglinks.get('subscribeNo'))
searchNclick(reglinks.get('agreement'))
#searchNclick(reglinks.get('continue'))

gf.checkElement(crelinks.get('title'))
searchNclick(crelinks.get('continue'))
"""

'''
# наведение не работает
a = search(menulinks.get('desktops'))
hover = ActionChains(driver).move_to_element(a)
hover.perform()
'''

searchNclick(menulinks.get('desktops'))
searchNclick(menulinks.get('showdesk'))
searchNclick(desklink.get('mychoise'))
scr.screenshot()

gf.checkElement(desklink.get('success'))

searchNclick(desklink.get('laptops'))

searchNclick(laplinks.get('mychoise'))
scr.screenshot()
gf.checkElement(maclinks.get('titlemac'))

cleartext(maclinks.get('quantity')) #сначала очистить строку
writeText(maclinks.get('quantity'), '2')
searchNclick(maclinks.get('add'))
gf.checkElement(maclinks.get('success'))
searchNclick(maclinks.get('cart'))
gf.checkElement(cartlinks.get('title'))
scr.screenshot()



