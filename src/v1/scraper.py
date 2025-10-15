import time
import settings

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from includes.models import Game
from includes.db import Db
from includes.common import Common

class Scraper:

    def Steam():

        driver = Scraper.InitiateDriver(settings.STEAM_URL)
        driver = Scraper.LazyLoading(driver)

        games = driver.find_elements(By.CLASS_NAME, "search_result_row")

        for g in games:
            link = Scraper.SafeFind(g, By.XPATH, ".", attr="href")
            title = Scraper.SafeFind(g, By.CLASS_NAME, "title", default="Unknown")
            release_date = Scraper.SafeFind(g, By.CLASS_NAME, "search_released", default="Unknown")
            original_price_text = Scraper.SafeFind(g, By.CLASS_NAME, "discount_original_price")
            final_price_text = Scraper.SafeFind(g, By.CLASS_NAME, "discount_final_price")
            tooltip = Scraper.SafeFind(g, By.CLASS_NAME, "search_review_summary", attr="data-tooltip-html")
            rating = tooltip.split("<br>")[0] if tooltip else "No reviews"
            discount_text = Scraper.SafeFind(g, By.CLASS_NAME, "discount_pct")
            discount = float(discount_text.replace("%", "").replace("-", "")) if discount_text else 0.0
            selling_price = Scraper.ParseSteamPrice(final_price_text)
            original_price = (Scraper.ParseSteamPrice(original_price_text) if original_price_text else selling_price)

            platform_list = []
            for p in Scraper.SafeFindAll(g, By.CSS_SELECTOR, ".search_platforms span"):
                classes = p.get_attribute("class").split()
                platform_list += [c for c in classes if c != "platform_img"]

            Scraper.InsertGame(title,'Steam',platform_list,original_price,selling_price,discount,rating,link,release_date)

    def Options():

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        return options
    
    def InitiateDriver(url):

        driver = webdriver.Chrome(options=Scraper.Options())
        driver.get(url)

        return driver
    
    def LazyLoading(driver):

        prev_height = 0

        for i in range(settings.MAX_SCROLL):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            time.sleep(settings.SLEEP_LIMIT)
            
            new_height = driver.execute_script("return document.body.scrollHeight")
            
            if new_height == prev_height:
                break
            
            prev_height = new_height

        return driver
    
    def SafeFind(element, by, selector, attr=None, text=True, default=None):
        
        try:
            found = element.find_element(by, selector)
            if attr:
                return found.get_attribute(attr)
            
            return found.text.strip() if text else found
        
        except:
            return default


    def SafeFindAll(element, by, selector):
        
        try:
            return element.find_elements(by, selector)
        
        except:
            return []

    def InsertGame(title,vendor,platform_list,original_price,selling_price,discount,rating,link,release_date):

        with Db.SessionScope() as session:
            existing_game = session.query(Game).filter(Game.link == link).first()
            
            if existing_game:
                existing_game.title = title
                existing_game.platform = platform_list
                existing_game.original_price = original_price
                existing_game.selling_price = selling_price
                existing_game.discount = discount
                existing_game.rating = rating
                existing_game.release_date = release_date
                existing_game.updated_at = Common.Datetime()
            
            else:
                game = Game(
                    title=title,
                    vendor=vendor,
                    platform=platform_list,
                    original_price=original_price,
                    selling_price=selling_price,
                    discount=discount,
                    rating=rating,
                    link=link,
                    release_date=release_date,
                    updated_at=Common.Datetime(),
                    created_at=Common.Datetime()
                )
            
                session.add(game)

    def ParseSteamPrice(value):
        
        if not value:
            return 0.0
        
        if "Free" in value:
            return 0.0
        
        return float(value.replace("C$", "").replace("$", "").strip())